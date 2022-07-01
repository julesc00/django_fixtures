import pytest

from django.test import TestCase
from django.contrib.auth.models import Group


class MyTest(TestCase):
    fixtures = ["group.json"]

    def test_should_create_group(self):
        group = Group.objects.filter(pk=1).first()
        self.assertEqual(group.name, "appusers")


class MyTest2(TestCase):
    fixtures = ["group.json"]

    def test_with_pytest(self):
        group = Group.objects.filter(pk=1).first()

        assert group.name == "appusers"
