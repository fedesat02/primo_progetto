from django.db import models

# Create your models here.
class Genere_SF(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Genere'
        verbose_name_plural = 'Generi'


class Autore_SF(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    nazione = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'


class Libro_SF(models.Model):
    titolo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    autore = models.ForeignKey(Autore_SF, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere_SF)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libri'