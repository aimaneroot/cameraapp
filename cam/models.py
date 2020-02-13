from django.conf import settings
from django.db import models
from django.utils import timezone


class Site(models.Model):
    nom = models.CharField(max_length=300)
    def __str__(self):
        return self.nom


class Emplacement(models.Model):
    nom = models.CharField(max_length=300)
    site = models.ForeignKey(Site, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom



class Fournisseur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    société = models.CharField(max_length=200)
    fonction = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    date_livraison = models.DateTimeField(blank=True, null=True)

def __str__(self):
        return self.nom




class Camera(models.Model):
    nom = models.CharField(max_length=300)
    reference = models.CharField(max_length=300,blank=True, null=True)
    emplacements = models.ManyToManyField(Emplacement, through='EmplacementCamera')
    date_installaion= models.DateTimeField(blank=True, null=True)
    frais = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fournisseur = models.ForeignKey(Fournisseur, blank=True, null=True, on_delete=models.CASCADE)
    def get_emplacements(self):
       return "\n".join([p.nom for p in self.emplacements.all()])
    def get_emplaceme(self):
        return self.emplacements.emplacements
    def __str__(self):
        return " - "+self.nom



class Reparation(models.Model):
    camera = models.ForeignKey(Camera, related_name='Camera', null=True, on_delete=models.CASCADE)
    date_reparation = models.DateTimeField(blank=True, null=True)
    frais = models.DecimalField(max_digits=10, decimal_places=2)
    descriptif = models.TextField() 

def __str__(self):
        return self.camera  


class EmplacementCamera(models.Model):
    camera = models.ForeignKey(Camera, blank=True, null=True, on_delete=models.CASCADE)
    emplacement = models.ForeignKey(Emplacement, blank=True, null=True, on_delete=models.CASCADE)
def __str__(self):
        return self.camera



