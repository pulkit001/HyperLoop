from django.shortcuts import render
from .models import Product , Material

AllProducts = Product.objects.all()
AllMaterials = Material.objects.all()
context = {"Products" : AllProducts , "Material" : AllMaterials}

# Create your views here.
def index(request):
    return render(request , 'Work/index.html' ,context)

def about(request , slugID):
    ProductF = Product.objects.get(id=slugID)
    return render(request , "Work/AboutProduct.html" , {"Product" : ProductF ,"Products" : AllProducts , "Material" : AllMaterials })

def comp(request, slugID):
    MaterialF = Material.objects.get(id=slugID)
    return render(request , "Work/AboutMat.html" , {"Material" : MaterialF , "Products" : AllProducts , "Material" : AllMaterials})
