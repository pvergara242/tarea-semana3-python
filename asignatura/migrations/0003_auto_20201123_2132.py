# Generated by Django 2.2.14 on 2020-11-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignatura', '0002_asignatura_name_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='aforo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
