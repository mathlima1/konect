# Generated by Django 3.1.5 on 2021-01-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidade',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Atalho'),
        ),
    ]
