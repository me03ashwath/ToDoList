# Generated by Django 4.2.13 on 2024-07-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='deadline',
            field=models.DateField(),
        ),
    ]
