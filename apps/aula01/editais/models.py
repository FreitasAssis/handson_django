from django.db.models import Model, CharField, ForeignKey, CASCADE

# Create your models here.


class Edital(Model):
    tipo = CharField("Tipo", max_length=15, null=False, blank=False)
    programa = CharField("Programa", max_length=15, null=False, blank=False)
    numero = CharField("Número", max_length=3, null=False, blank=False)
    siglaUO = CharField("Sigla", max_length=3, null=False, blank=False)
    linkEdital = CharField("Link", max_length=255, null=False, blank=False)
    descricao = CharField("Descrição", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Edital"
        verbose_name_plural = "Editais"

    def __str__(self):
        return self.linkEdital


# class UF(Model):
#     sigla = CharField("Sigla", max_length=2, null=False, blank=False, primary_key=True)
#     codigo = CharField("Código", max_length=2, null=False, blank=False)
#     nome  = CharField("Nome", max_length=255, null=False, blank=False)
#
#     class Meta:
#         verbose_name = "UF"
#         verbose_name_plural = "UFs"
#
#     def __str__(self):
#         return self.sigla
#
#
# class Municipio(Model):
#     codigo = CharField("Código", max_length=7, null=False, blank=False)
#     nome  = CharField("Nome", max_length=255, null=False, blank=False)
#     uf  = ForeignKey(UF, null=False, blank=False, on_delete=CASCADE)
#
#     class Meta:
#         verbose_name = "Município"
#         verbose_name_plural = "Municípios"
#
#     def __str__(self):
#         return "%s (%s)" % (self.nome, self.uf)
