# Generated by Django 2.2.14 on 2020-11-23 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_estudiante_clase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='clase',
        ),
    ]