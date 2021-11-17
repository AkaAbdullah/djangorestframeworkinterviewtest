from django.db import models

class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name