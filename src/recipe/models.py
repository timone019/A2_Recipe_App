from django.db import models

# Create your models here.
# Recipe Model
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def calculate_difficulty(self):
        # Example logic for difficulty based on cooking time
        if self.cooking_time < 30:
            self.difficulty = "Easy"
        elif self.cooking_time < 60:
            self.difficulty = "Medium"
        else:
            self.difficulty = "Hard"
        self.save()
        