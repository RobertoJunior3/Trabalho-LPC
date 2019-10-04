from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    departamento = models.CharField(max_length=128)

    def __str__(self):
        return self.departamento

class Pessoa(models.Model):
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone Celular', max_length=15, 
    help_text='Número de Telefone celular no formato (99) 99999-9999', null=True, blank=True)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'

    numeroProcesso = models.CharField('Número', max_length=128)
    funcionario = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)
    interessados = models.ManyToManyField(Pessoa, related_name='Interessados')
    investigados = models.ManyToManyField(Pessoa, related_name='Investigados')
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)

    
    def __str__(self):
        return self.numeroProcesso

class Documento(models.Model):

    numeroDocumento = models.CharField('Número', max_length=128)
    titulo = models.CharField('Título do Processo', max_length=128)
    data = models.DateField('Data')
    texto = models.TextField('Texto')
    usuario = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)
    local = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)
    processo = models.ForeignKey(Processo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.numeroDocumento
        
class PortariaDeInstauracao(Documento):
    class Meta:
        verbose_name = 'Portaria de Instauração'
        verbose_name_plural = 'Portarias de Instauração'

    iniciou = models.BooleanField('Processo iniciado?')

    def __str__(self):
        return self.processo.numeroProcesso + ' - Processo Iniciado'

class PedidoDePrazo(Documento):
    class Meta:
        verbose_name = 'Pedido de Prazo'
        verbose_name_plural = 'Pedidos de Prazo'

    justificativa = models.TextField('Justificativa')
    data_anterior = models.DateField('Data Anterior')
    novo_prazo = models.DateField('Novo Prazo')

    def __str__(self):
        return self.processo.numeroProcesso +' - '+ str(self.novo_prazo)

class EnvioDeProcesso(Documento):
    class Meta:
        verbose_name = 'Envio de Processo'
        verbose_name_plural = 'Envio de Processos'

    departamento_tramite = models.ManyToManyField(Departamento, related_name='Departamento')
    data_mudanca = models.DateField('Data Mudança')

    def __str__(self):
        return self.processo.numeroProcesso + ' - ' + str(self.data_mudanca)

class Tramitacoes(models.Model):
    class Meta:
        verbose_name = 'Tramitação'
        verbose_name_plural = 'Tramitações'

    processo = models.ForeignKey(Processo, null=True, blank=True, on_delete=models.SET_NULL)
    origem = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL, related_name='Origem')
    destino = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL, related_name='Destino')
    data_movimentacao = models.DateField('Data Movimentação')

    def __str__(self):
        return self.processo.numeroProcesso