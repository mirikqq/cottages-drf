# Generated by Django 4.2 on 2024-06-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cottages', '0004_cottage_is_ready'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cottage',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
