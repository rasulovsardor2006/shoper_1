from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from app.form import ProdctModelForm, LoginForm, RegisterForm, ForgotPasswordForm
from app.models import Product, Category


def index(request):
    products = Product.objects.order_by('-id')
    context = {
        "products": products
    }
    return render(request, 'app/index.html', context)


def product_details(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    context = {
        'product': product
    }
    return render(request, 'app/product_details.html', context)


def shop_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'app/shop.html', context)


def shopping_cart(request):
    return render(request, 'app/shopping_cart.html')

def contact(request):
    return render(request, 'app/contact.html')

def checkout(request):
    return render(request, 'app/checkout.html')

def create_product(request):
    category = Category.objects.all()
    if request == 'POST':
        form = ProdctModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ProdctModelForm()
    context = {
        'form' : form,
        'sizes' : Product.ChoiceSize,
        'colors' : Product.ChoiceColor,
        'price' : Product.price,
        'categories' : category
    }
    return render(request, 'app/create_product.html', context)


def update_product(request, product_id):
    category = Category.objects.all()
    product = Product.objects.filter(id=product_id).first()
    if request.method == 'POST':
        form = ProdctModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = ProdctModelForm(instance=product)
    context = {
        "form":form,
        'sizes': Product.ChoiceSize,
        'colors': Product.ChoiceColor,
        'categories': category
    }
    return render(request, 'app/update_product.html', context)


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')

    return render(request, 'app/auth/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return render(request, 'app/auth/logout.html')


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    return render(request, 'app/auth/register.html', {'form':form})


class ForgotPasswordView(FormView):
    template_name = 'app/auth/forgot_password.html'
    success_url = reverse_lazy('login')
    form_class = ForgotPasswordForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


