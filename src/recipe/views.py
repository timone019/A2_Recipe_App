from django.shortcuts import render, get_object_or_404
from .models import Recipe

#to protect function-based view
from django.contrib.auth.decorators import login_required #to access Book model

from .forms import RecipeSearchForm

# Create your views here.

def home(request):
    # recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html')

@login_required
def recipe_list(request):
    # create an instance of RecipeSearchForm defined in recipe/forms.py
    form = RecipeSearchForm(request.POST or None)
    recipes = Recipe.objects.all()
    
    if form.is_valid():
        recipe_title = form.cleaned_data.get('recipe_title')
        recipes = recipes.filter(name__icontains=recipe_title)
    
    #pack up data to be sent to template in the context dictionary
    context={
            'form': form,
            'recipes': recipes
    }
    
    return render(request, 'recipe/recipe_list.html', context)

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})


# def success(request):
#     #do nothing, simply display page    
#     return render(request, 'recipe/success.html')


