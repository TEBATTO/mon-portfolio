from django.db import models

# Création des modèles.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title