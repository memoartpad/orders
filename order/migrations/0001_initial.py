# Generated by Django 3.1.1 on 2020-09-24 06:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_supply', models.DateTimeField()),
                ('urgent', models.BooleanField(default=False)),
                ('warehouse', models.CharField(blank=True, max_length=64, null=True)),
                ('reference', models.CharField(blank=True, max_length=64, null=True)),
                ('office_code', models.IntegerField(blank=True, null=True)),
                ('partner_code', models.IntegerField(blank=True, null=True)),
                ('order_datails', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), default=None, null=True, size=None)),
                ('quantity', models.IntegerField()),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.article')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
