# Generated by Django 4.1 on 2022-08-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='type',
            field=models.CharField(choices=[('NOR', 'Normal'), ('FIG', 'Fighting'), ('FLY', 'Flying'), ('POI', 'Poison'), ('GRO', 'Ground'), ('ROC', 'Rock'), ('BUG', 'Bug'), ('GHO', 'Ghost'), ('STE', 'Steel'), ('FIR', 'Fire'), ('WAT', 'Water'), ('GRA', 'Grass'), ('ELE', 'Electric'), ('PSY', 'Psychic'), ('ICE', 'Ice'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('FAI', 'Fairy'), ('???', '???')], max_length=3),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type_one',
            field=models.CharField(choices=[('NOR', 'Normal'), ('FIG', 'Fighting'), ('FLY', 'Flying'), ('POI', 'Poison'), ('GRO', 'Ground'), ('ROC', 'Rock'), ('BUG', 'Bug'), ('GHO', 'Ghost'), ('STE', 'Steel'), ('FIR', 'Fire'), ('WAT', 'Water'), ('GRA', 'Grass'), ('ELE', 'Electric'), ('PSY', 'Psychic'), ('ICE', 'Ice'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('FAI', 'Fairy'), ('???', '???')], max_length=3),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type_two',
            field=models.CharField(blank=True, choices=[('NOR', 'Normal'), ('FIG', 'Fighting'), ('FLY', 'Flying'), ('POI', 'Poison'), ('GRO', 'Ground'), ('ROC', 'Rock'), ('BUG', 'Bug'), ('GHO', 'Ghost'), ('STE', 'Steel'), ('FIR', 'Fire'), ('WAT', 'Water'), ('GRA', 'Grass'), ('ELE', 'Electric'), ('PSY', 'Psychic'), ('ICE', 'Ice'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('FAI', 'Fairy'), ('???', '???')], max_length=3),
        ),
    ]
