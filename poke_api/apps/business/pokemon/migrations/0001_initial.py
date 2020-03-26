# Generated by Django 3.0.4 on 2020-03-25 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stats', '0001_initial'),
        ('pokemon_species', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('species', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='pokemon_species.PokemonSpecies', verbose_name='species')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_stat', models.IntegerField()),
                ('effort', models.IntegerField()),
                ('pokemon', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='stats', to='pokemon.Pokemon', verbose_name='pokemon')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_stat', to='stats.Stat', verbose_name='stat')),
            ],
        ),
    ]