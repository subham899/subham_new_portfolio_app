from django.db import models

class portfolio_project(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    img = models.ImageField(upload_to='Media')
    url = models.URLField(blank=True)

