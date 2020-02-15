# Generated by Django 2.2 on 2020-02-15 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
        ('inv', '0002_subcategoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('clasemodelo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bases.ClaseModelo')),
                ('descripcion', models.CharField(help_text='Descripción de la marca', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Marca',
            },
            bases=('bases.clasemodelo',),
        ),
    ]