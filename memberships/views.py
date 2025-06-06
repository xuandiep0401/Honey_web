from django.shortcuts import render
from .models import UserMembership
from django.contrib.auth.decorators import login_required


@login_required
def my_membership(request):
    membership = UserMembership.objects.filter(user=request.user).first()
    return render(request, 'memberships/detail.html', {'membership': membership})
