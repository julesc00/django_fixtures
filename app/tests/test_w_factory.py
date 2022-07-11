import pytest
from typing import List, Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

"""
Using a factory
"""


def create_app_user(
        username: str,
        password: Optional[str] = None,
        first_name: Optional[str] = "first name",
        last_name: Optional[str] = "last name",
        email: Optional[str] = "example@somewhere.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
        groups: List[Group] = [],
) -> User:
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=is_staff,
        is_superuser=is_superuser,
        is_active=is_active
    )
    user.groups.add(*groups)
    return user


@pytest.fixture
def user_a(db, app_user_group: Group) -> User:
    user = User.objects.create_user(
        username="A",
        password="secret",
        first_name="Charbelito",
        last_name="Briones",
        email="chulito@chulos.com",
        is_staff=False,
        is_superuser=False,
        is_active=True
    )
    user.groups.add(app_user_group)
    return user
