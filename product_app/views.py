'''from django.shortcuts import render
from .models import Product

def add_product(request):

    if request.method == "POST":

        p_name = request.POST.get('p_name')
        p_type = request.POST.get('p_type')
        p_price = request.POST.get('p_price')
        p_quantity = request.POST.get('p_quantity')

        Product.objects.create(
            p_name=p_name,
            p_type=p_type,
            p_price=p_price,
            p_quantity=p_quantity
        )

        return render(request, "success.html")

    return render(request, "product_form.html")
def view_all_products(request):
    data=Product.objects.all().values()
    print(list(data))
    return render(request, "view_all_products.html")
from django.shortcuts import render, redirect
from .models import Product


# Display Products

def display_products(request):

    data = Product.objects.all()

    return render(request, "display.html", {"data": data})


# Delete Product

def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    return redirect('/product/display/')


# Update Product

def update_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == "POST":

        product.p_name = request.POST.get('p_name')
        product.p_type = request.POST.get('p_type')
        product.p_price = request.POST.get('p_price')
        product.p_quantity = request.POST.get('p_quantity')

        product.save()

        return redirect('/product/display/')

    return render(request,
                  "update.html",
                  {"product": product})'''
from django.shortcuts import render, redirect

from .models import Product, Cart


# Add Product

def add_product(request):

    if request.method == "POST":

        p_name = request.POST.get('p_name')

        p_type = request.POST.get('p_type')

        p_price = request.POST.get('p_price')

        p_quantity = request.POST.get('p_quantity')

        Product.objects.create(
            p_name=p_name,
            p_type=p_type,
            p_price=p_price,
            p_quantity=p_quantity
        )

        return redirect('/product/display/')

    return render(request, "product_form.html")


# Display Products

def display_products(request):

    data = Product.objects.all()

    return render(request,
                  "display.html",
                  {"data": data})


# Add To Cart

def add_to_cart(request, id):

    product = Product.objects.get(id=id)

    Cart.objects.create(product=product)

    return redirect('/product/cart/')

# View Cart

def cart_page(request):

    cart_data = Cart.objects.all()

    return render(request,
                  "cart.html",
                  {"cart_data": cart_data})


# Delete Product

def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    return redirect('/product/display/')


# Update Product

def update_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == "POST":

        product.p_name = request.POST.get('p_name')

        product.p_type = request.POST.get('p_type')

        product.p_price = request.POST.get('p_price')

        product.p_quantity = request.POST.get('p_quantity')

        product.save()

        return redirect('/product/display/')

    return render(request,
                  "update.html",
                  {"product": product})