from django.db import models

# Create your models here.

from tinymce import models as tinymce_models

class Page(models.Model):
    body = tinymce_models.HTMLField(default="")
    url = models.TextField(default="")
