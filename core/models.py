from django.db import models

class Produto(models.Model):
	nome = models.CharField('Nome', max_length=60)
	preco = models.DecimalField('Preço', max_digits=12, decimal_places=2)
	estoque = models.IntegerField('Quantidade em estoque')

	def __str__(self):
		return self.nome


class Cliente(models.Model):
	nome = models.CharField('Nome', max_length=60)
	sobrenome = models.CharField('Sobrenome', max_length=60)
	email = models.EmailField('E-mail', max_length=60)

	def __str__(self):
		return f'{self.nome} {self.sobrenome}'

