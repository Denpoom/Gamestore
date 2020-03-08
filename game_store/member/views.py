from builtins import object

from django.shortcuts import render
# ดึงข้อมูล
from data.models import User


# Create your views here.
def member(request):
    user = User.objects.all()
    return render(request, 'home_member.html', context={'user': user})
