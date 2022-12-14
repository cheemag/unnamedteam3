# Generated by Django 4.1 on 2022-09-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0008_remove_profile_unique_profiles'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ability',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='move',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='pokemon',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='ability',
            constraint=models.UniqueConstraint(fields=('name', 'profile'), name='unique_abilities'),
        ),
        migrations.AddConstraint(
            model_name='location',
            constraint=models.UniqueConstraint(fields=('name', 'profile'), name='unique_locations'),
        ),
        migrations.AddConstraint(
            model_name='move',
            constraint=models.UniqueConstraint(fields=('name', 'profile'), name='unique_moves'),
        ),
        migrations.AddConstraint(
            model_name='pokemon',
            constraint=models.UniqueConstraint(fields=('name', 'profile'), name='unique_pokemons'),
        ),
        migrations.AddConstraint(
            model_name='profile',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_profiles'),
        ),
    ]
