from django.db import models
from django.contrib.auth import get_user_model


class MembershipLevel(models.Model):
    name = models.CharField(max_length=50)
    discount_percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class UserMembership(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    level = models.ForeignKey(MembershipLevel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user} - {self.level}"
