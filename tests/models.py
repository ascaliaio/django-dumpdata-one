from django.db import models


class OneModel(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    time_is = models.DateTimeField(auto_now_add=True)
    decimal_value = models.DecimalField(max_digits=5, decimal_places=2)
    integer_value = models.IntegerField(default=1)
    document = models.FileField(blank=True, null=True)


class ChildModel(models.Model):
    one = models.ForeignKey(OneModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
