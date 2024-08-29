from django.urls import path
from .views import home, recipe_list, recipe_detail

app_name = 'recipe' 

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]