# Generated by Django 5.1.4 on 2024-12-20 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_othermodel_childb_childa'),
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Second',
            fields=[
                ('first_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_one.first')),
                ('age', models.IntegerField()),
            ],
            bases=('app_one.first',),
        ),
    ]
