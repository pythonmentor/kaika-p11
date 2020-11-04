from accounts.models import CustomUser, AwaitingData


def validate_subscription(request, guid, messages):
    try:
        CustomUser.objects.create_user(
            username=AwaitingData.objects.get(guid=guid, key="login").value,
            password=AwaitingData.objects.get(guid=guid, key="password").value,
            first_name=AwaitingData.objects.get(guid=guid, key="first_name").value,
            last_name=AwaitingData.objects.get(guid=guid, key="last_name").value,
            email=AwaitingData.objects.get(guid=guid, key="email").value,
        )

        messages.add_message(
            request,
            25,
            f"L'utilisateur "
            f"{AwaitingData.objects.get(guid=guid, key='login').value}"
            f" a bien été créé, vous pouvez dès à présent vous connecter",
        )

    except Exception as error:
        messages.add_message(
            request, 40, f"Echec lors de la création du compte: {error}, "
                         f"si le problème se reproduit, veuillez contacter"
                         f" le support"
        )
