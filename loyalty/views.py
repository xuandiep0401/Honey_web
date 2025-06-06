from django.shortcuts import render
from .models import LoyaltyPoint
from django.contrib.auth.decorators import login_required


@login_required
def my_points(request):
    lp = LoyaltyPoint.objects.filter(user=request.user).first()
    return render(request, 'loyalty/points.html', {'points': lp})
