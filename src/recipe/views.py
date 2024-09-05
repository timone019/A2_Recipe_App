from django.shortcuts import render, get_object_or_404
from .models import Recipe

#to protect function-based view
from django.contrib.auth.decorators import login_required #to access Book model

# Create your views here.

def home(request):
    # recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html')

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})


# def success(request):
#     #do nothing, simply display page    
#     return render(request, 'recipe/success.html')

