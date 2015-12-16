from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IVA(models.Model):
    nome = models.CharField(max_length=25)
    valore = models.DecimalField(max_digits=6, decimal_places=4)
    percentuale = models.CharField(max_length=7)


class UM(models.Model):
    nome = models.CharField(max_length=20)
    simbolo = models.CharField(max_length=5)




class Valuta(models.Model):
    nome = models.CharField(max_length=15)
    nome_breve = models.CharField(max_length=5)
    simbolo = models.CharField(max_length=4)




class Lingua(models.Model):
    nome = models.CharField(max_length=20)
    nome_breve = models.CharField(max_length=5)





class Nazione(models.Model):
    nome = models.CharField(max_length=25)
    nome_breve = models.CharField(max_length=5)
    lingua = models.ForeignKey(Lingua)
    valuta = models.ForeignKey(Valuta)


    def __str__(self):
        return self.nome



class CentroCR(models.Model):
    nome = models.CharField(max_length=25)



class Cliente(models.Model):

    AZIENDA = "1"
    PRIVATO = "2"

    TIPOLOGIE = (
        (AZIENDA, 'Azienda'),
        (PRIVATO, 'Privato'),
    )

    nome = models.CharField(max_length=25)
    cognome = models.CharField(max_length=25)
    ragione_sociale = models.CharField(max_length=40)
    tipologia = models.CharField(max_length=12, choices=TIPOLOGIE, default=PRIVATO)
    nazione = models.ForeignKey(Nazione)
    citta = models.CharField(max_length=30)
    indirizzo = models.CharField(max_length=35)
    indirizzo_n = models.CharField(max_length=6)
    cap = models.CharField(max_length=12)
    lingua = models.ForeignKey(Lingua)
    valuta = models.ForeignKey(Valuta)
    partita_iva = models.CharField(max_length=15)
    codice_fiscale = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    cellulare = models.CharField(max_length=15)
    mail = models.CharField(max_length=25)
    mailpec = models.CharField(max_length=30)
    fax = models.CharField(max_length=15)

    def __str__(self):
        #questa funzione restituisce il nome con cui si identifica l'oggetto a seconda che si tratti di un'azienda o di un privato
        if self.tipologia == 1:
            return self.ragione_sociale
        else:
            nome_completo = self.nome + " " + self.cognome
            return nome_completo






class Fornitore(models.Model):

    ragione_sociale = models.CharField(max_length=40)
    nazione = models.ForeignKey(Nazione)
    citta = models.CharField(max_length=30)
    indirizzo = models.CharField(max_length=35)
    indirizzo_n = models.CharField(max_length=6)
    cap = models.CharField(max_length=12)
    lingua = models.ForeignKey(Lingua)
    valuta = models.ForeignKey(Valuta)
    partita_iva = models.CharField(max_length=15)
    codice_fiscale = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    cellulare = models.CharField(max_length=15)
    mail = models.CharField(max_length=25)
    mailpec = models.CharField(max_length=30)
    fax = models.CharField(max_length=15)


    def __str__(self):
        return self.ragione_sociale




class Articolo(models.Model):
    nome = models.CharField(max_length=25)
