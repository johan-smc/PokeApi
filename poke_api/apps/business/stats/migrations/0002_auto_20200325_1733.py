# Generated by Django 3.0.4 on 2020-03-25 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]