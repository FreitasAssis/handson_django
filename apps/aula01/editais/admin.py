from django.contrib.admin import ModelAdmin, register
from .models import Edital


@register(Edital)
class EditalAdmin(ModelAdmin):
    list_display = ('numero', 'linkEdital', 'descricao')
    list_editable = ('descricao',)
    list_filter = ('numero', )
    search_fields = ('numero', 'linkEdital')
