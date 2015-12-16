
from Teorema.models import *
from Teorema.categorie.models import CategoriaVendita

# Create your models here.

class Vendita(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    scadenza = models.DateField()
    centro_cr = models.ForeignKey(CentroCR)
    categoria_vendita = models.ForeignKey(CategoriaVendita)
    budget_netto = models.DecimalField(max_digits=12, decimal_places=2)
    budget_iva = models.DecimalField(max_digits=12, decimal_places=2)
    budget_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)


    def __str__(self):
        return self.nome


class RecordVendita(models.Model):
    vendita = models.ForeignKey(Vendita)
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

class PreventivoVendita(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    scadenza = models.DateField()
    cliente = models.ForeignKey(Cliente)
    centro_cr = models.ForeignKey(CentroCR)
    categoria_vendita = models.ForeignKey(CategoriaVendita)
    budget_netto = models.DecimalField(max_digits=12, decimal_places=2)
    budget_iva = models.DecimalField(max_digits=12, decimal_places=2)
    budget_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    vendita = models.ForeignKey(Vendita)


    def __str__(self):
        return self.nome


class RecordPreventivoVendita(models.Model):
    preventivo = models.ForeignKey(PreventivoVendita)
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




class OrdineVendita(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    scadenza = models.DateField()
    centro_cr = models.ForeignKey(CentroCR)
    cliente = models.ForeignKey(Cliente)
    categoria_acquisto = models.ForeignKey(CategoriaVendita)
    costo_netto = models.DecimalField(max_digits=12, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=12, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    vendita = models.ForeignKey(Vendita)
    preventivo = models.ForeignKey(PreventivoVendita, null=True)


    def __str__(self):
        return self.nome


class RecordOrdineVendita(models.Model):
    ordine = models.ForeignKey(OrdineVendita)
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


class DDTVendita(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    consegna = models.DateField()
    cliente = models.ForeignKey(Cliente)
    centro_cr = models.ForeignKey(CentroCR)
    categoria_vendita = models.ForeignKey(CategoriaVendita)
    costo_netto = models.DecimalField(max_digits=12, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=12, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    vendita = models.ForeignKey(Vendita)
    preventivo = models.ForeignKey(PreventivoVendita, null=True)
    ordine = models.ForeignKey(OrdineVendita)


    def __str__(self):
        return self.nome


class RecordDDTVendita(models.Model):
    ddt = models.ForeignKey(DDTVendita)
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



class FatturaAttiva(models.Model):
    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    note = models.TextField(max_length=800)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente)
    centro_cr = models.ForeignKey(CentroCR)
    categoria_acquisto = models.ForeignKey(CategoriaVendita)
    costo_netto = models.DecimalField(max_digits=12, decimal_places=2)
    costo_iva = models.DecimalField(max_digits=12, decimal_places=2)
    costo_totale = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)
    vendita = models.ForeignKey(Vendita)
    preventivo = models.ForeignKey(PreventivoVendita, null=True)
    ordine = models.ForeignKey(OrdineVendita)
    ddt = models.ForeignKey(DDTVendita)


    def __str__(self):
        return self.nome


class RecordFatturaAttiva(models.Model):
    fattura = models.ForeignKey(FatturaAttiva)
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