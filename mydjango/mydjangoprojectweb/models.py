"""Module providing a function printing python version."""
from django.db import models

class Blog(models.Model):   # this class inherits from Model base class which helps to interacts directly with our database.
    title = models.CharField(max_length=200)  # Charfield is a field where you'll store short strings (upto max length of 200).
    email = models.CharField(max_length=200, default="youremail@somewhere.net")
    content = models.TextField()   # Text Field can be used for large amount of text like blog posts etc..