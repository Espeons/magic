# Generated by Django 5.0.6 on 2024-07-07 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alex', '0002_alter_card_name_alter_deck_commander_alter_deck_name'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='players',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.player'),
        ),
    ]
