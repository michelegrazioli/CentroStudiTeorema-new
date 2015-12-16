from django.db import models

# Create your models here.

class CategoriaArticolo(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome


class CategoriaAcquisto(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class CategoriaVendita(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome