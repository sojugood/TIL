# Generated by Django 4.2.5 on 2023-09-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]
