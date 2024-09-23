import os
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipeSearchForm
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class RecipeModelTest(TestCase):
    def setUp(self):
        # Create a sample recipe to be used in the tests
        self.recipe = Recipe.objects.create(
            name="Pasta",
            cooking_time=30,
        )
        self.recipe.ingredients.create(name="Tomato", quantity=1.00)
        self.recipe.ingredients.create(name="Pasta", quantity=2.00)

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

class RecipeSearchFormTest(TestCase):
    def test_form_valid_data(self):
        form = RecipeSearchForm(data={
            'recipe_title': 'Pasta',
            'chart_type': '#1',
            'show_all': True
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipeSearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # recipe_title and chart_type are required

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username=os.getenv('TEST_USER_USERNAME'),
            password=os.getenv('TEST_USER_PASSWORD')
        )
        self.client.login(
            username=os.getenv('TEST_USER_USERNAME'),
            password=os.getenv('TEST_USER_PASSWORD')
        )
        self.recipe = Recipe.objects.create(
            name="Pasta",
            cooking_time=30,
        )
        self.recipe.ingredients.create(name="Tomato", quantity=1.00)
        self.recipe.ingredients.create(name="Pasta", quantity=2.00)
        self.recipe_list_url = reverse('recipe:recipe_list')
        self.recipe_detail_url = reverse('recipe:recipe_detail', args=[self.recipe.id])

    def test_recipe_list_view(self):
        response = self.client.get(self.recipe_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/recipe_list.html')

    def test_recipe_list_view_post(self):
        response = self.client.post(self.recipe_list_url, {
            'recipe_title': 'Pasta',
            'chart_type': '#1',
            'show_all': True
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pasta')

    def test_recipe_detail_view(self):
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/recipe_detail.html')
        self.assertContains(response, 'Pasta')