from django.contrib.admin import ModelAdmin, TabularInline, StackedInline, register
from .models import Edital, Programa, Tipo, Vaga, Coordenador


class VagaInline(StackedInline):
    model = Vaga


class CoordenadorInline(TabularInline):
    model = Coordenador
    extra = 1


@register(Tipo)
class TipoAdmin(ModelAdmin):
    list_display = ['id', 'nome']
    list_editable = ('nome', )


@register(Programa)
class ProgramaAdmin(ModelAdmin):
    list_display = ['nome']


@register(Edital)
class EditalAdmin(ModelAdmin):
    list_display = ('nome_curto', 'programa', 'link_edital', 'descricao')
    list_filter = ('tipo', 'programa', 'numero', 'sigla_uo')
    search_fields = ('numero', 'sigla_uo')
    inlines = [CoordenadorInline, VagaInline]
    date_hierarchy = 'data_publicacao'

