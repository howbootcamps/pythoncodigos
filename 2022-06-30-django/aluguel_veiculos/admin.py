from django.contrib import admin
from aluguel_veiculos.models import Aluguel, Cliente, Veiculo


class ClienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco', 'telefone', 'tipo')
    list_display = ('tipo', 'nome')


class AluguelAdmin(admin.ModelAdmin):
    pass
    

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa',)


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Aluguel, AluguelAdmin)
