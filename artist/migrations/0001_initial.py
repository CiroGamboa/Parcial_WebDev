# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('idautor', models.AutoField(db_column='idAutor', primary_key=True, serialize=False)),
                ('nombreart', models.CharField(db_column='nombreArt', max_length=200, unique=True)),
                ('artpassword', models.CharField(db_column='artPassword', max_length=128)),
                ('nombres', models.CharField(db_column='nombres', max_length=200)),
                ('apellidos', models.CharField(db_column='apellidos', max_length=200)),
                ('email', models.CharField(db_column='email', max_length=200, unique=True)),
            ],
            options={
                'db_table': 'Autor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('idestilo', models.AutoField(db_column='idEstilo', primary_key=True, serialize=False)),
                ('estilo', models.CharField(db_column='estilo', max_length=100, unique=True)),
            ],
            options={
                'db_table': 'Estilo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('idobra', models.AutoField(db_column='idObra', primary_key=True, serialize=False)),
                ('nombreobra', models.CharField(db_column='nombreObra', max_length=200)),
                ('imgobra', models.ImageField(upload_to='photos')),
                ('fechaobra', models.DateTimeField(blank=True, db_column='fechaObra', default=django.utils.timezone.now)),
                ('idautor', models.ForeignKey(db_column='idautor', on_delete=django.db.models.deletion.DO_NOTHING, related_name='obras_autor', to='artist.Autor')),
                ('idestilo', models.ForeignKey(db_column='idestilo', on_delete=django.db.models.deletion.DO_NOTHING, related_name='obras_estilo', to='artist.Estilo')),
            ],
            options={
                'db_table': 'Obra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoObra',
            fields=[
                ('idtipoobra', models.AutoField(db_column='idTipoObra', primary_key=True, serialize=False)),
                ('tipoobra', models.CharField(db_column='tipoObra', max_length=200, unique=True)),
            ],
            options={
                'db_table': 'TipoObra',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='obra',
            name='idtipoobra',
            field=models.ForeignKey(db_column='idtipoobra', on_delete=django.db.models.deletion.DO_NOTHING, related_name='obras_tipo', to='artist.TipoObra'),
        ),
    ]
