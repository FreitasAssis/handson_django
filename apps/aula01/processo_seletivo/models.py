from django.db.models import Model, CharField, ForeignKey, CASCADE, URLField, PositiveIntegerField, DateField, BooleanField, DecimalField, TextField
from django.contrib.auth.models import User


class Tipo(Model):
    nome = CharField("Tipo", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome


class Programa(Model):
    nome = CharField("Tipo", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome

class Edital(Model):
    PERIODO = (
        (1, '1º Período'),
        (2, '2º Período'),
    )

    tipo = ForeignKey(Tipo, verbose_name='Tipo', on_delete=CASCADE)
    programa = ForeignKey(Programa, verbose_name='Programa', on_delete=CASCADE)
    numero = CharField('Número', max_length=50)
    sigla_uo = CharField('Unidade organizacional', max_length=100, help_text='Ex.: DG-EAD/IFRN')
    link_edital = URLField('URL', max_length=300, help_text='Informe o LINK onde está o edital')
    grupo = CharField('Grupo', max_length=200, null=True)
    descricao = CharField('Descrição', max_length=300)
    ano = PositiveIntegerField('Ano', help_text='Digite o ano')
    periodo = PositiveIntegerField('Período letivo', choices=PERIODO)
    data_publicacao = DateField('Data de publicação')
    existe_taxa = BooleanField('Existe taxa?', default=False)
    valor_taxa = DecimalField('Valor da taxa', max_digits=7, decimal_places=2)
    vencimento_boleto = DateField('Vencimento do boleto')
    anotacoes = TextField('Anotações')

    class Meta:
        verbose_name = "Edital"
        verbose_name_plural = "Editais"
        unique_together = ("numero", "sigla_uo")


    def nome_curto(self):
        return "%s %s-%s" % (self.tipo, self.numero, self.sigla_uo)
    nome_curto.short_description = 'Identificação'

    def nome_longo(self):
        return "%s %s" % (self.nome_curto(), self.descricao)
    nome_longo.short_description = 'Nome'

    def __str__(self):
        return self.nome_curto()


class Vaga(Model):
    edital = ForeignKey(Edital, on_delete=CASCADE)
    curso = CharField('Curso', max_length=200)
    vaga = CharField('Vaga', max_length=100)
    numero_vagas = PositiveIntegerField('Número de vagas')

    def __str__(self):
        return "%s %s %s %d" % (self.edital, self.curso, self.vaga, self.numero_vagas)


class Coordenador(Model):
    usuario = ForeignKey(User, on_delete=CASCADE)
    edital = ForeignKey(Edital, on_delete=CASCADE)

    def __str__(self):
        return "%s, coordenador %s" % (self.usuario, self.edital)
