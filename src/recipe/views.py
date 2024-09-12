from django.shortcuts import render, get_object_or_404
from .models import Recipe

#to protect function-based view
from django.contrib.auth.decorators import login_required #to access Recipe model
import pandas as pd
from .forms import RecipeSearchForm
from .utils import get_chart


# Create your views here.

def home(request):
    return render(request, 'recipe/home.html')

@login_required
def recipe_list(request):
    # create an instance of RecipeSearchForm defined in recipe/forms.py
    form = RecipeSearchForm(request.POST or None)
    recipe_df_html = None #initialize
    chart = None #initialize 
    chart_type = None #initialize
    recipes = Recipe.objects.all()
    
    # Convert all recipes to a DataFrame for the chart
    all_recipes_df = pd.DataFrame(recipes.values('name', 'cooking_time', 'difficulty'))
    
    if form.is_valid():
        recipe_title = form.cleaned_data.get('recipe_title')
        chart_type = form.cleaned_data.get('chart_type')
        print(f"Search Query: {recipe_title}, Chart Type: {chart_type}")  # Print the search query & chart type
        print(f"Recipe Title: {recipe_title}")  # Print the recipe title
        # Apply filter to extract data
        filtered_recipes = Recipe.objects.filter(name__icontains=recipe_title)
        
        # Exploring QuerySets
        print('Exploring querysets:')
        
        print('Case 1: Output of Recipe.objects.all()')
        qs = Recipe.objects.all()
        print(qs)
        
        print('Case 2: Output of Recipe.objects.filter(name__icontains=recipe_title)')
        print(filtered_recipes)
        
        print('Case 3: Output of qs.values()')
        print(filtered_recipes.values())
        
        print('Case 4: Output of qs.values_list()')
        print(filtered_recipes.values_list())
        
        print('Case 5: Output of Recipe.objects.get(id=1)')
        try:
            obj = Recipe.objects.get(id=1)
            print(obj)
        except Recipe.DoesNotExist:
            print('Recipe with id=1 does not exist') 

        # Convert the filtered QuerySet to a Pandas DataFrame
        if filtered_recipes.exists():
            recipe_df = pd.DataFrame(filtered_recipes.values('id', 'name', 'cooking_time', 'difficulty')) 
            print(recipe_df)
            recipe_df_html = recipe_df.to_html(classes='table table-striped', index=False)  # Convert DataFrame to HTML
            recipes = filtered_recipes # Update recipes to use the filtered results
            
    # Generate the chart using all recipes
    chart = get_chart(chart_type, all_recipes_df, labels=all_recipes_df['name'].values)  

    #pack up data to be sent to template in the context dictionary
    context={
            'form': form,
            'recipes': recipes,
            'recipe_df_html': recipe_df_html, # Include the DataFrame HTML in the context
            'chart': chart # Include the chart in the context
    }
    
    return render(request, 'recipe/recipe_list.html', context)

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})


# def success(request):
#     #do nothing, simply display page    
#     return render(request, 'recipe/success.html')


