# Recipe Application

Welcome to the Recipe Application! This app allows users to browse, search, and manage a collection of recipes. Users can add new recipes, view details, and edit existing ones.

See Live Site: https://timone019.pythonanywhere.com

## Features

- **Recipe Management**: Create, update, and delete recipes.
  
- **Ingredient Management**: Add ingredients with quantity details.
  
- **Search Functionality**: Easily find recipes by name or ingredient.
  
- **User Authentication**: Secure login and registration for users.
  
- **Responsive Design**: Mobile-friendly interface.
  
## Tech Stack

- **Frontend**:
  - HTML
  - CSS
  - JavaScript

- **Backend**:
  - Python
  - Django

- **Database**:
  - PostgreSQL

- **Deployment**:
  - PythonAnywhere
  - Gunicorn
  - Whitenoise

- **Other Libraries**:
  - Matplotlib
  - Pandas
  - Pillow

## Screenshots

![Home Page](src/media/screenshots/recipeHomeScreenshot.png)
![Recipe Detail](src/media/screenshots/recipeDetailsScreenshot.png)

## Installation

To get started with this project, follow these steps:

### Prerequisites

- Python 3.8+
- Django 3.2+
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/recipe-app.git
   cd recipe-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open your browser and navigate to http://localhost:8000 to start using the app.

8. To access admin panel, go to http://localhost:8000/admin

## Usage
- Browse Recipes: View a list of all recipes.
  
- Search Recipes: Use the search bar to find recipes by name or ingredient.
  
- Add Recipes: Click on "Add Recipe" to create a new recipe.
  
- Edit Recipes: Click on a recipe and select "Edit" to update it.
  
- Delete Recipes: Click on a recipe and select "Delete" to remove it.