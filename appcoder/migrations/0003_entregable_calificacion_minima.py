# Generated by Django 4.0.3 on 2022-03-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0002_remove_curso_id_alter_curso_camada'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregable',
            name='calificacion_minima',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
