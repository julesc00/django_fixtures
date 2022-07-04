import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


# db fixture is injected in the function in order to have db access, else it creates an error.
def test_should_create_user_with_username(db) -> None:
    user = User.objects.create_user("Jemima")

    assert user.username == "Jemima"


def test_should_check_password(db) -> None:
    user = User.objects.create_user("A")
    user.set_password("secret")

    assert user.check_password("secret") is True


def test_should_not_check_unusable_password(db) -> None:
    user = User.objects.create_user("A")
    user.set_password("secret")
    user.set_unusable_password()

    assert user.check_password("secret") is False
