from django.db import models
from Teorema.models import *
from Teorema.categorie.models import CategoriaAcquisto

# Create your models here.

class Acquisto(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    scadenza = models.DateField()
    centro_cr = models.ForeignKey(CentroCR)
    categoria_acquisto = models.ForeignKey(CategoriaAcquisto)
    budget_netto = models.DecimalField(max_digits=12, decimal_places=2)
    budget_iva = models.DecimalField(max_digits=12, decimal_places=2)
    budget_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)


    def __str__(self):
        return self.nome


class RecordAcquisto(models.Model):
    acquisto = models.ForeignKey(Acquisto)
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=60)
    descrizione = models.CharField(max_length=240)
    note = models.TextField(max_length=800)
    articolo = models.ForeignKey(Articolo, null=True)
    um = models.ForeignKey(UM)
    quantita = models.DecimalField(max_digits=10, decimal_places=2)
    budget_cad = models.DecimalField(max_digits=10, decimal_places=2)
    budget_netto = models.DecimalField(max_digits=10, decimal_places=2)
    budget_iva = models.DecimalField(max_digits=10, decimal_places=2)
    budget_totale = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nome
#End Purchases Section

#Start Estimates Section

class PreventivoAcquisto(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    scadenza = models.DateField()
    fornitore = models.ForeignKey(Fornitore)
    centro_cr = models.ForeignKey(CentroCR)
    categoria_acquisto = models.ForeignKey(CategoriaAcquisto)
    budget_netto = models.DecimalField(max_digits=12, decimal_places=2)
    budget_iva = models.DecimalField(max_digits=12, decimal_places=2)
    budget_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    acquisto = models.ForeignKey(Acquisto)


    def __str__(self):
        return self.nome


class RecordPreventivoAcquisto(models.Model):
    preventivo = models.ForeignKey(PreventivoAcquisto)
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=60)
    descrizione = models.CharField(max_length=240)
    note = models.TextField(max_length=800)
    articolo = models.ForeignKey(Articolo, null=True)
    um = models.ForeignKey(UM)
    quantita = models.DecimalField(max_digits=10, decimal_places=2)
    budget_cad = models.DecimalField(max_digits=10, decimal_places=2)
    budget_netto = models.DecimalField(max_digits=10, decimal_places=2)
    budget_iva = models.DecimalField(max_digits=10, decimal_places=2)
    budget_totale = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nome
#End Purchases Section


#Start Orders Section




class OrdineAcquisto(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    scadenza = models.DateField()
    centro_cr = models.ForeignKey(CentroCR)
    fornitore = models.ForeignKey(Fornitore)
    categoria_acquisto = models.ForeignKey(CategoriaAcquisto)
    costo_netto = models.DecimalField(max_digits=12, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=12, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    acquisto = models.ForeignKey(Acquisto)
    preventivo = models.ForeignKey(PreventivoAcquisto, null=True)


    def __str__(self):
        return self.nome


class RecordOrdineAcquisto(models.Model):
    ordine = models.ForeignKey(OrdineAcquisto)
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=60)
    descrizione = models.CharField(max_length=240)
    note = models.TextField(max_length=800)
    articolo = models.ForeignKey(Articolo, null=True)
    um = models.ForeignKey(UM)
    quantita = models.DecimalField(max_digits=10, decimal_places=2)
    costo_cad = models.DecimalField(max_digits=10, decimal_places=2)
    costo_netto = models.DecimalField(max_digits=10, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=10, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nome

#End Orders Section

#Start Delivery Notes Section


class DDTAcquisto(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    consegna = models.DateField()
    fornitore = models.ForeignKey(Fornitore)
    centro_cr = models.ForeignKey(CentroCR)
    categoria_acquisto = models.ForeignKey(CategoriaAcquisto)
    costo_netto = models.DecimalField(max_digits=12, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=12, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    acquisto = models.ForeignKey(Acquisto)
    preventivo = models.ForeignKey(PreventivoAcquisto, null=True)
    ordine = models.ForeignKey(OrdineAcquisto)


    def __str__(self):
        return self.nome


class RecordDDTAcquisto(models.Model):
    ddt = models.ForeignKey(DDTAcquisto)
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=60)
    descrizione = models.CharField(max_length=240)
    note = models.TextField(max_length=800)
    articolo = models.ForeignKey(Articolo, null=True)
    um = models.ForeignKey(UM)
    quantita = models.DecimalField(max_digits=10, decimal_places=2)
    costo_cad = models.DecimalField(max_digits=10, decimal_places=2)
    costo_netto = models.DecimalField(max_digits=10, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=10, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nome

#End Delvery Notes Section



class FatturaPassiva(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    fornitore = models.ForeignKey(Fornitore)
    centro_cr = models.ForeignKey(CentroCR)
    categoria_acquisto = models.ForeignKey(CategoriaAcquisto)
    costo_netto = models.DecimalField(max_digits=12, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=12, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    acquisto = models.ForeignKey(Acquisto)
    preventivo = models.ForeignKey(PreventivoAcquisto, null=True)
    ordine = models.ForeignKey(OrdineAcquisto)
    ddt = models.ForeignKey(DDTAcquisto)


    def __str__(self):
        return self.nome


class RecordFatturaPassiva(models.Model):
    fattura = models.ForeignKey(FatturaPassiva)
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=60)
    descrizione = models.CharField(max_length=240)
    note = models.TextField(max_length=800)
    articolo = models.ForeignKey(Articolo, null=True)
    um = models.ForeignKey(UM)
    quantita = models.DecimalField(max_digits=10, decimal_places=2)
    costo_cad = models.DecimalField(max_digits=10, decimal_places=2)
    costo_netto = models.DecimalField(max_digits=10, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=10, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nome