# Generated by Django 4.1 on 2022-09-08 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_learnable_remove_pokemon_learnable_pokemon_can_learn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Findable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='found_in',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='can_find_in',
            field=models.ManyToManyField(blank=True, through='pokedex.Findable', to='pokedex.location'),
        ),
        migrations.AddField(
            model_name='findable',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.pokemon'),
        ),
    ]
