# Generated by Django 4.0.6 on 2022-12-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_carousel',
            field=models.BooleanField(default=False),
        ),
    ]