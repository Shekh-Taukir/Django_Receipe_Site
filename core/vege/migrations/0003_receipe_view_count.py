# Generated by Django 5.0.2 on 2024-04-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='view_count',
            field=models.IntegerField(default=1),
        ),
    ]
