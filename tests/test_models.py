import pytest
from memberships.models import MembershipLevel, UserMembership
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_membership_level_str():
    level = MembershipLevel.objects.create(name="Gold", discount_percent=10)
    assert str(level) == "Gold"

@pytest.mark.django_db
def test_user_membership_str():
    user = get_user_model().objects.create(username="u")
    level = MembershipLevel.objects.create(name="Silver")
    um = UserMembership.objects.create(user=user, level=level)
    assert str(um) == f"{user} - {level}"
