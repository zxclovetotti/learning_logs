from django.db import models

# Create your models here.

class Camera(models.Model):
    # Enter brand of camera
    brand = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return string
        return self.brand

class Model(models.Model):
    # Topping of pizza
    model = models.ForeignKey(Camera)
    model_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return string
        if len(self.model_name) >= 50:
            return self.model_name[:50] + "..."
        else:
            return self.model_name