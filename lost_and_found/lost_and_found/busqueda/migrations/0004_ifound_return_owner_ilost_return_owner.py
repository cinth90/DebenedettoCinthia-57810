# Generated by Django 5.0.6 on 2024-07-01 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0003_alter_ifound_options_alter_ilost_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ifound',
            name='return_owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ilost',
            name='return_owner',
            field=models.BooleanField(default=False),
        ),
    ]
