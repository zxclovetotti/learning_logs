from django.db import models

# Create your models here.

class Topic(models.Model):
    # Learning Topics
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return string
        return self.text

class Entry(models.Model):
    # knowledge about one topic
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return string
        if len(self.text) >= 50:
            return self.text[:50] + "..."
        else:
            return self.text                                                                                   