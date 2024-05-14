from django.db import models

# Create your models here.
class Plat(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    categorie = models.ForeignKey('CategoriePlat', on_delete=models.SET_NULL, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class CategoriePlat(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nom


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plats = models.ManyToManyField(Plat, through='LigneCommande')
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande {self.id} - Client: {self.client.nom}"


class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"Ligne de commande {self.id} - Plat: {self.plat.nom}, Quantité: {self.quantite}"


