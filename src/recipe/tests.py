from django.test import TestCase
from .models import Recipe
from ingredient.models import Ingredient  # Import Ingredient model


class RecipeModelTest(TestCase):
    def setUp(self):
        # Create a sample recipe to be used in the tests
        self.recipe = Recipe.objects.create(
            name="Pasta",
            cooking_time=30,
        )
        self.recipe.ingredients.create(name="Tomato")
        self.recipe.ingredients.create(name="Pasta")

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, "Pasta")
        self.assertEqual(self.recipe.cooking_time, 30)

    def test_recipe_str_method(self):
        # Test the __str__ method
        self.assertEqual(str(self.recipe), "Pasta")

    def test_ingredient_relationship(self):
        # Test the relationship with Ingredient model
        ingredients = self.recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
        self.assertIn("Tomato", [ingredient.name for ingredient in ingredients])

    def test_calculate_difficulty(self):
        # Test the calculate_difficulty method
        self.recipe.cooking_time = 20
        self.recipe.calculate_difficulty()
        self.assertEqual(
            self.recipe.difficulty, "Easy"
        )  # Adjust the expected value based on your logic
