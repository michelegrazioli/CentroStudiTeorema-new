from django.db import models
from Teorema.models import *

# Create your models here.

class Corso(models.Model):
    DDF = "1"
    EXTRAOBBLIGO = "2"
    SPECIALIZZAZIONE = "3"
    FORMAZIONECONTINUA = "4"

    CORSI = (
        (DDF, "DDF"),
        (EXTRAOBBLIGO, "Extra Obbligo"),
        (SPECIALIZZAZIONE, "Specializzazione"),
        (FORMAZIONECONTINUA, "Formazione Continua"),
    )

    codice = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    descrizione = models.CharField(max_length=300)
    tipologia = models.CharField(max_length=20, choices=CORSI)


    def __str__(self):
        return self.nome


#class DDF(Corsi):



#class ExtraObbligo(Corsi):


#class Specializzazione(Corsi):



#class FormazioneContinua(Corsi):



class AnnoDiCorso(models.Model):
    corso = models.ForeignKey(Corso)
    qualifica = models.CharField(max_length=20, null=True)
    precedente = models.ForeignKey('self', null=True)




class AnnoScolastico(models.Model):

    TIPOLOGIA = ("Scolastico", "Contabile")
    nome = models.CharField(max_length=30)
    inizio = models.DateField()
    fine = models.DateField()
    #tipologia = models.CharField(max_length=12, choices=TIPOLOGIA)



class Insegnante(models.Model):
    nome = models.CharField(max_length=25)
    cognome = models.CharField(max_length=25)
    costo_orario = models.DecimalField(max_digits=12, decimal_places=2)
    valuta = models.ForeignKey(Valuta)






class PianoDiStudi(models.Model):
    corso = models.ForeignKey(Corso)




class SuperamentoAnno(models.Model):
    alunno = models.ForeignKey(Cliente)
    anno_corso = models.ForeignKey(AnnoDiCorso)
    anno_scolastico = models.ForeignKey(AnnoScolastico)



class Iscrizione(models.Model):
    alunno = models.ForeignKey(Cliente)
    anno_corso = models.ForeignKey(AnnoDiCorso)
    anno_scolastico = models.ForeignKey(AnnoScolastico)




class Classe(models.Model):
    corso = models.ForeignKey(Corso)
    anno = models.ForeignKey(AnnoDiCorso)
    anno_scolatico = models.ForeignKey(AnnoScolastico)





class Materia(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    nome = models.CharField(max_length=20)
    tipologia = models.CharField(max_length=20)



class Lezione(models.Model):
    materia = models.ForeignKey(Materia)
    insegnante = models.ForeignKey(Insegnante)
    classe = models.ForeignKey(Classe)
    inizio = models.DateTimeField()
    fine = models.DateTimeField()



class Presenza(models.Model):
    lezione = models.ForeignKey(Lezione)
    alunno = models.ForeignKey(Cliente)
    firma = models.ForeignKey(Insegnante)




#class Calendario(models.Model):



class Voto(models.Model):
    data = models.DateField()
    voto = models.DecimalField(max_digits=4, decimal_places=1)
    materia = models.ForeignKey(Materia)
    alunno = models.ForeignKey(Cliente)
    firma = models.ForeignKey(Insegnante)
