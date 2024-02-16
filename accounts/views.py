from django.shortcuts import render
from .models import CustomUser
# Create your views here.
def index(request):
    obj = CustomUser.objects.all()
    for i in obj:
        print(i.password)
    return render(request,"index.html")