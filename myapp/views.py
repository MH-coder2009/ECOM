from django.shortcuts import render
from ecom.myapp.models import Product


def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})


# Create your views here.
