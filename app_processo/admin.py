from django.contrib import admin
from .models import *

@admin.register(Departamento)
class Departamento(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class Pessoa(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    pass

@admin.register(Processo)
class Processo(admin.ModelAdmin):
    pass

@admin.register(Documento)
class Documento(admin.ModelAdmin):
    pass

@admin.register(PortariaDeInstauracao)
class PortariaDeInstauracao(admin.ModelAdmin):
    pass

@admin.register(PedidoDePrazo)
class PedidoDePrazo(admin.ModelAdmin):
    pass

@admin.register(EnvioDeProcesso)
class EnvioDeProcesso(admin.ModelAdmin):
    pass

@admin.register(Tramitacoes)
class Tramitacoes(admin.ModelAdmin):
    pass
