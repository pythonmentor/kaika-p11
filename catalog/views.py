"""Views for catalog"""
import ast
from typing import List
from uuid import UUID

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import redirect, render

from search.navbar_decorator import navbar_search_decorator

from . import NUTRISCORE
from .commands.commands import get_better_products, get_delete_info, get_favorite_info
from .models import Favorite, Product


@navbar_search_decorator
def aliment(request, product_id):
    """View for aliments"""
    product = Product.objects.get(id=product_id)
    nutriments: List = ast.literal_eval(product.nutriments)
    return render(
        request, "aliment.html", {"product": product, "nutriments": nutriments}
    )


@navbar_search_decorator
@login_required
def favorites(request, user: str):
    """View for favorites"""
    products: List[Product] = [
        Product.objects.get(id=favorite.substitute.id)
        for favorite in Favorite.objects.filter(user=user)
    ]
    paginator = Paginator(products, 6)

    page = request.GET.get("page")

    page_obj = paginator.get_page(page)

    context = {"products": products, "nutriscores": NUTRISCORE, "page_obj": page_obj}

    return render(request, "favorites.html", context)


@navbar_search_decorator
def results(request, base_product):
    """View for results"""
    products, base_product = get_better_products(base_product)

    paginator = Paginator(products, 6)

    page = request.GET.get("page")

    page_obj = paginator.get_page(page)

    context = {
        "base_product": base_product,
        "products": products,
        "nutriscores": NUTRISCORE,
        "page_obj": page_obj,
    }

    return render(request, "results.html", context)


@login_required
def save(request, base_product: UUID, substitute_product: UUID):
    """Save a product in favorite"""
    user = request.user

    new_favorite, substitute = get_favorite_info(base_product, substitute_product, user)

    try:
        new_favorite.save()

    except IntegrityError as error:
        messages.add_message(
            request,
            40,
            f"Le substitut {substitute.product_name_fr} n'a pas pu être enregistré "
            f"suite à l'erreur suivante: {error}",
        )
        return redirect("catalog:results", base_product=base_product)

    messages.add_message(
        request,
        25,
        f"Le produit {substitute.product_name_fr} a correctement été ajouté "
        f"à vos favoris",
    )
    return redirect("catalog:results", base_product=base_product)


@login_required
def delete_favorite(request, product_id: UUID):
    """Delete a favorite"""
    user = request.user

    to_delete, product_name = get_delete_info(product_id, user)

    try:
        to_delete.delete()
    except IntegrityError as error:
        messages.add_message(
            request,
            40,
            f"Nous n'avons pas réussis à supprimer le produit "
            f"{product_name} pour la raison suivante: {error}",
        )

    messages.add_message(
        request,
        25,
        f"Le produit {product_name} est correctement supprimé de vos favoris",
    )
    return redirect("catalog:favorites", user=user.id)
