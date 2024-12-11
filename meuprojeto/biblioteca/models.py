from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo

