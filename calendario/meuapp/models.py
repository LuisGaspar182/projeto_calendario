from django.db import models

class Tatuador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Tatuagem(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='tatuagens')
    tatuador = models.ForeignKey(Tatuador, on_delete=models.CASCADE, related_name='tatuagens')
    data = models.DateField()
    horas = models.TimeField()

    class Meta:
        unique_together = ('tatuador', 'data', 'horas')  # Impede horários duplicados para o mesmo tatuador

    def __str__(self):
        return f"Tatuagem de {self.cliente.nome} com {self.tatuador.nome} em {self.data} às {self.horas}"
