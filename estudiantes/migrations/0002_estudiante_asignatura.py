# Generated by Django 2.2.14 on 2020-11-22 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignatura', '0001_initial'),
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='asignatura',
            field=models.ManyToManyField(related_name='estudiantes', to='asignatura.Asignatura'),
        ),
    ]
