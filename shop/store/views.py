from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render,get_object_or_404
from django.template import RequestContext, loader
from store import models
from carton.cart import Cart
# Create your views here.
def index(request):
    context = {
        'product_list': models.Product.objects.order_by('-category')[:5]
        }
    return render(request, 'store/index.html', context)

def details(request, id):
    product =get_object_or_404(models.Product, pk=id)
    return render(request, 'store/product-details.html',{'product':product})

def shop(request):
#    context = {
#        'product_list': models.Product.objects.order_by('-id')[:10]
#        }
    return render(request, 'store/shop.html')

def checkout(request):
    context = {
        'product_list': models.Product.objects.order_by('-category')[:10]
        }
    return render(request, 'store/checkout.html', context)

def showcard(request):
    return render(request, 'store/cart.html')

def login(request):
    return render(request, 'store/login.html')

def add(request):
    cart = Cart(request.session)
    product = models.Product.objects.get(id=request.GET.get('id'))
    cart.add(product, price=product.price)
    return render(request, 'store/cart.html')

def remove_single(request):
    cart = Cart(request.session)
    product = models.Product.objects.get(id=request.GET.get('id'))
    cart.remove_single(product)
    return render(request, 'store/cart.html')

def remove(request):
    cart = Cart(request.session)
    product = models.Product.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return render(request, 'store/cart.html')

def add_to_cart(request, id):
    cart = Cart(request.session)
    product =get_object_or_404(models.Product, pk=id)
    cart.add(product, price=product.price)
    return HttpResponsePermanentRedirect('/')
    #return render(request, 'store/product-details.html',{'product':product})
    #return render(request, 'store/product-details.html',{'product':product})