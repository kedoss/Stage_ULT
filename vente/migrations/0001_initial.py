# Generated by Django 5.0.4 on 2024-04-24 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=31)),
                ('unite', models.CharField(max_length=31)),
                ('quantite', models.FloatField(editable=False, null=True)),
                ('prix_vente', models.FloatField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vente.category')),
            ],
        ),
    ]
