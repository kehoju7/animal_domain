from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    """An animal under discussion"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
        
        
class Description(models.Model):
    """Description of a particular animal"""
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'descriptions'
        
        
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
