from django.db import models

<<<<<<< HEAD
# Recipe Model
class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    
    name = models.CharField(max_length=50)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
=======
# Create your models here.
# Recipe Model
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20)
>>>>>>> 0dbf1a9c7f88e5af25e02f89b59da443e70065f8

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
        