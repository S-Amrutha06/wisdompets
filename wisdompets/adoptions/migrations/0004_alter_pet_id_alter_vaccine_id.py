# Generated by Django 5.0.2 on 2024-03-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0003_pet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]