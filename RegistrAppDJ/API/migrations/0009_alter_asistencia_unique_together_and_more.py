# Generated by Django 5.0.6 on 2024-10-30 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_asistencia'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='asistencia',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='asistencia',
        ),
    ]