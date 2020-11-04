"""Define the toolbar search for all templates"""
from search.forms import SearchForm


def toolbar_search(request):
    """Pass toolbar to all views"""
    toolbar_form: SearchForm = SearchForm(request.POST)

    form_parameters = toolbar_form.fields["produit"]

    form_parameters.label = ""
    form_parameters.required = False

    return {"toolbar_form": toolbar_form}
