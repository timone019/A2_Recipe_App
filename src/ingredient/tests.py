from django.test import TestCase
from .models import Ingredient
from recipe.models import Recipe

class IngredientModelTest(TestCase):
    def setUp(self):
        # Create a sample recipe to be used in the tests
        self.recipe = Recipe.objects.create(
            name="Pasta",
            cooking_time=30,
        )
        self.ingredient = Ingredient.objects.create(name="Cheese", quantity=1.00, recipe=self.recipe)

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.name, "Cheese")
        self.assertEqual(self.ingredient.quantity, 1.00)

    def test_ingredient_str_method(self):
        # Test the __str__ method
        self.assertEqual(str(self.ingredient), "Cheese (1.00) (unit)")