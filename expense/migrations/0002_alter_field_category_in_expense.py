# Generated by Django 5.0.6 on 2024-06-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('E', 'Entertainment'), ('H', 'Household'), ('B', 'Bill'), ('M', 'Medicine'), ('T', 'Travel')], max_length=255),
        ),
    ]
