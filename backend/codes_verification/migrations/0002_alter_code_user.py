# Generated by Django 4.0.3 on 2022-04-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes_verification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='user',
            field=models.EmailField(blank=True, max_length=55),
        ),
    ]