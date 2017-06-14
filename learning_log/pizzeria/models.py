from django.db import models

# Create your models here.

class Pizza(models.Model):
    # Pizza
    name = models.CharField(max_length=40)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return string
        return self.name

class Topping(models.Model):
    # Topping of pizza
    Pizza = models.ForeignKey(Pizza)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return string
        if len(self.name) >= 50:
            return self.name[:50] + "..."
        else:
            return self.name          