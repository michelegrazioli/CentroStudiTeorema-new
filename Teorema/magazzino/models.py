from Teorema.categorie.models import CategoriaArticolo
from Teorema.models import *
# Create your models here.

class Articolo(models.Model):
    codice = models.CharField(max_length=25)
    nome = models.CharField(max_length=30)
    descrizione = models.CharField(max_length=300)
    note = models.TextField(max_length=800)
    categoria = models.ForeignKey(CategoriaArticolo, null=True)


    def __str__(self):
        return self.nome


class Prodotto(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    descrizione = models.CharField(max_length=300, null=True)
    note = models.TextField(max_length=800, null=True)
    prezzo_netto = models.DecimalField(max_digits=12, decimal_places=4, null=True)
    valuta = models.ForeignKey(Valuta, null=True)

    def __str__(self):
        return  self.nome


#services class
class Service(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return  self.nome




class MovimentoMagazzinoArticolo(models.Model):
    #questa classe rappresenta le movimentazioni che si presentano negli ordini
    CARICO = "1"
    SCARICO = "2"
    MOVIMENTO = (
        (CARICO, 'Carico'),
        (SCARICO, 'Scarico'),
    )

    data = models.DateTimeField(null=True)
    articolo = models.ForeignKey(Articolo)
    quantita = models.DecimalField(max_digits=12, decimal_places=4)
    um = models.ForeignKey(UM)
    movimento = models.CharField(max_length=7, choices=MOVIMENTO, null=False)
    #ordine_acquisto = models.ForeignKey()
    #ordine_vendita = models.ForeignKey()
    #ddt_acquisto
    #ddt_vendita
    #fattura_attiva
    #fattura_passiva




class MovimentoMagazzinoProdotto(models.Model):
    #questa classe rappresenta le movimentazioni che si presentano negli ordini
    CARICO = "1"
    SCARICO = "2"
    MOVIMENTO = (
        (CARICO, 'Carico'),
        (SCARICO, 'Scarico'),
    )

    data = models.DateTimeField(null=True)
    prodotto = models.ForeignKey(Prodotto)
    quantita = models.DecimalField(max_digits=12, decimal_places=4)
    um = models.ForeignKey(UM)
    movimento = models.CharField(max_length=7, choices=MOVIMENTO, null=False)
    #ordine_acquisto = models.ForeignKey()
    #ordine_vendita = models.ForeignKey()
    #ddt_acquisto
    #ddt_vendita
    #fattura_attiva
    #fattura_passiva
