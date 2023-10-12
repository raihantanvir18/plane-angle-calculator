from django.db import models

class Equation(models.Model):
    equation1 = models.TextField()
    equation2 = models.TextField()
    result = models.FloatField(null=True, blank=True)

    class Meta:
        app_label = 'calculator'
