# Generated by Django 3.1.5 on 2021-01-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210116_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('subtitulo', models.CharField(max_length=100, verbose_name='Subtítulo')),
                ('texto', models.TextField(max_length=500, verbose_name='Texto')),
            ],
            options={
                'verbose_name': 'Cadastro',
                'verbose_name_plural': 'Cadastro',
            },
        ),
    ]