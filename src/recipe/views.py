from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Create your views here.
def home(request):
    # recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})