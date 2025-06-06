from django.db import models
from django.contrib.auth import get_user_model


class LoyaltyPoint(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    points_balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.points_balance}"


class LoyaltyTransaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    change = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.change}" 
