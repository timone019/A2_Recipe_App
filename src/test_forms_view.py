from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from recipe.forms import RecipeSearchForm  # Use absolute import
from recipe.models import Recipe  # Use absolute import

class RecipeFormTest(TestCase):

    def test_recipe_search_form_valid(self):
        form_data = {'recipe_title': 'Test Recipe', 'chart_type': '#1', 'show_all': True}
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_search_form_invalid(self):
        form_data = {'recipe_title': '', 'chart_type': '#1', 'show_all': True}
        form = RecipeSearchForm(data=form_data)
        self.assertFalse(form.is_valid())

class RecipeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(username='testuser', password='12345')
        # Create some recipes
        Recipe.objects.create(name='Recipe 1', cooking_time=30, difficulty='Easy')
        Recipe.objects.create(name='Recipe 2', cooking_time=45, difficulty='Medium')

    def setUp(self):
        self.client = Client()

    def test_recipe_list_view_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertRedirects(response, '/login/?next=/recipes/')

    def test_recipe_list_view_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/recipe_list.html')

    def test_recipe_list_view_context_data(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTrue('recipes' in response.context)
        self.assertTrue('recipe_df_html' in response.context)
        self.assertTrue('chart' in response.context)
        self.assertTrue('chart_type' in response.context)

    def test_recipe_list_view_pagination(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['recipes']) <= 10)  # Assuming pagination limit is 10