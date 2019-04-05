from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)