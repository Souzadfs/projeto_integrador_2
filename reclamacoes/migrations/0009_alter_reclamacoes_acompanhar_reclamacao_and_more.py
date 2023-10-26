# Generated by Django 4.2.4 on 2023-10-26 18:43

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moradores', '0003_morador_bairro'),
        ('reclamacoes', '0008_rename_acompanhareclamacao_reclamacoes_acompanhar_reclamacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacoes',
            name='acompanhar_reclamacao',
            field=models.BooleanField(default=False, verbose_name='ACOMPANHAR RECLAMAÇÃO'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='bairro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moradores.bairro', verbose_name='BAIRRO'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='cep',
            field=models.CharField(max_length=100, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='COMPLEMENTO'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='DATA DA RECLAMAÇÃO'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='historico',
            field=models.TextField(blank=True, default='', null=True, verbose_name='RESPOSTA'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='nome',
            field=models.CharField(max_length=100, null=True, verbose_name='NOME'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='numero_casa',
            field=models.CharField(blank=True, max_length=10, verbose_name='NÚMERO DA CASA'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='observacao',
            field=models.TextField(max_length=500, verbose_name='DETALHES DA RECLAMAÇÃO'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='referencia',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='PONTO DE REFERÊNCIA'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='rua',
            field=models.CharField(blank=True, max_length=200, verbose_name='RUA'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('verificando', 'Verificando'), ('resolvido', 'Resolvido')], default='pendente', max_length=20, verbose_name='STATUS'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='TELEFONE'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='tipo_reclamacao',
            field=models.CharField(choices=[('nao_recebi_saco', 'NÃO RECEBI O SACO VERDE'), ('caminhao_nao_passou', 'CAMINHÃO NÃO PASSOU'), ('saco_rasgado', 'SACO VERDE RASGADO'), ('saco_insuficiente', 'SACO VERDE INSUFICIENTE'), ('sugestao', 'SUGESTÃO'), ('outros', 'OUTRO')], max_length=20, verbose_name='TIPO DE RECLAMAÇÃO'),
        ),
    ]
