from django.db import models
from estados.models import Estados

class Cidades(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE,default='SP')

    def __str__(self):
        return self.nome