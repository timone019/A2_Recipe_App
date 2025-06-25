from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# define a function view called login_view that takes a request from user


@require_http_methods(["GET", "POST"])
def login_view(request):
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('recipe:recipe_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('recipe:recipe_list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

#define a function view called logout_view that takes a request from user
@login_required
def logout_view(request):
    """Handle user logout"""
    if request.method == 'POST' or request.method == 'GET':  # Handle both GET and POST
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('logout_success')
    return redirect('recipe:recipe_list')


def demo_login_view(request):
    """View for demo user login"""
    if request.user.is_authenticated:
        return redirect('recipe:recipe_list')
        
    # Demo user credentials
    demo_username = 'demo_user'
    demo_password = 'demopassword123!@#'  # Strong password for demo
    
    # Check if demo user exists, create if not
    if not User.objects.filter(username=demo_username).exists():
        try:
            User.objects.create_user(
                username=demo_username,
                email='demo@example.com',
                password=demo_password,
                is_active=True
            )
            messages.info(request, 'Demo account created successfully.')
        except Exception as e:
            messages.error(request, 'Failed to create demo account. Please contact support.')
            return redirect('login')
    
    # Authenticate and login the demo user
    user = authenticate(request, username=demo_username, password=demo_password)
    
    if user is not None:
        login(request, user)
        messages.success(request, 'You are now logged in as a demo user. Welcome!')
        return redirect('recipe:recipe_list')
    else:
        messages.error(request, 'Failed to login as demo user. Please try again.')
        return redirect('login')


def logout_success_view(request):
    """Display success message after logout"""
    return render(request, 'auth/success.html')
