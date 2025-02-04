# Generated by Django 5.1.4 on 2024-12-17 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0004_other_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='One_One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='One_Two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.OneToOneField(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='second_app.one_one')),
            ],
        ),
    ]
