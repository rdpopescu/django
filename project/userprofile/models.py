from django.db import models

class Pontaj(models.Model):


    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
