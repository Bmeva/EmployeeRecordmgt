# Generated by Django 5.1 on 2024-08-18 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_skill_skill_validity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(blank=True, max_length=120, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_head', to='API.employeedetails'),
        ),
    ]
