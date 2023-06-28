from django.db import models


class Box(models.Model):
    Box_ID=models.IntegerField(primary_key=True)
    Box_material=models.CharField(max_length=50)
    QTY_material=models.CharField(max_length=50)

    def __str__(self):
        return self.Box_material
