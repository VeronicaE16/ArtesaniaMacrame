# Generated by Django 4.0.4 on 2022-09-15 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='ganancia',
        ),
    ]
