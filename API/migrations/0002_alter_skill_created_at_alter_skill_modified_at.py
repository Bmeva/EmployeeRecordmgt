# Generated by Django 5.1 on 2024-08-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
