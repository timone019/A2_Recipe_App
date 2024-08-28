from django.db import models

# Create your models here.
# Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=20, default='unit')
    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f"{self.name} ({self.quantity}) ({self.unit})"
=======
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f"{self.name} ({self.quantity})"
>>>>>>> 0dbf1a9c7f88e5af25e02f89b59da443e70065f8
