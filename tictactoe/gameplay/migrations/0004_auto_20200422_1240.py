# Generated by Django 3.0.5 on 2020-04-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0003_auto_20200421_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(editable=False),
        ),
    ]
