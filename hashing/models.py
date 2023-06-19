from django.db import models


class Hash(models.Model):
    """
    This model stores the text and its hash in lower case
    """
    text = models.TextField()
    hash = models.CharField(max_length=64)
