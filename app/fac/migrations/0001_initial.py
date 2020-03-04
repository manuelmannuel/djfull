# Generated by Django 2.2 on 2020-03-04 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('clasemodelo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bases.ClaseModelo')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('tipo', models.CharField(choices=[('Natural', 'Natural'), ('Juridica', 'Juridica')], default='Natural', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
            bases=('bases.clasemodelo',),
        ),
    ]
