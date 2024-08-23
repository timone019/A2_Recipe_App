from django.test import TestCase
from .models import Ingredient
from recipe.models import Recipe

# Create your tests here.


class IngredientModelTest(TestCase):
    def setUp(self):
        # Create a sample ingredient
        self.recipe = Recipe.objects.create(name="Pizza", cooking_time=20)
        self.ingredient = Ingredient.objects.create(name="Cheese", quantity="1 cup", recipe=self.recipe)

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.name, "Cheese")
        self.assertEqual(self.ingredient.quantity, "1 cup")
        self.assertEqual(self.ingredient.recipe.name, "Pizza")

    def test_ingredient_str_method(self):
        # Test the __str__ method
        self.assertEqual(str(self.ingredient), "Cheese (1 cup)")
