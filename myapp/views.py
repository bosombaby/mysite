from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product


# Create your views here.
def index(request):
    context = {
        "text": 'Hello Django'
    }
    return render(request, 'myapp/hello.html', context)


def products(request):
    product_list = Product.objects.all()

    product_name = request.GET.get('product_name')
    print(product_name)
    if product_name != None and product_name != '':
        product_list = product_list.filter(name__icontains=product_name)

    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(request, 'myapp/index.html', context)


# Class based view for above products view [ListView]
class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product
    }
    return render(request, 'myapp/detail.html', context)


# Class based view for above product detail view [DetailView]
class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/detail.html'
    context_object_name = 'product'


@login_required
def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user
        print(request.user)
        product = Product(name=name, price=price, desc=desc, image=image, seller_name=seller_name)
        product.save()
        return redirect('/myapp/products/mine')

    return render(request, 'myapp/product_add.html')


# Class based view for creating a product
class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'desc', 'image', 'seller_name']


@login_required
def product_update(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        if request.FILES:
            product.image = request.FILES['upload']
            print(request.FILES)
        product.save()
        return redirect('/myapp/products/mine')

    context = {
        'product': product
    }

    return render(request, 'myapp/product_update.html', context)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'desc', 'image', 'seller_name']
    template_name_suffix = '_update_form'


@login_required
def product_delete(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products/mine')
    context = {'product': product}

    return render(request, 'myapp/product_delete.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:product_mine')


@login_required
def product_mine(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {'products': products}

    return render(request, 'myapp/product_mine.html', context)
