# Generated by Django 5.0.2 on 2024-05-11 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0008_reportcard'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_generation')},
        ),
    ]