# Generated by Django 5.1.1 on 2024-09-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=100)),
                ('brandmodel', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('milage', models.CharField(max_length=100)),
                ('perdayrent', models.IntegerField()),
            ],
        ),
    ]
