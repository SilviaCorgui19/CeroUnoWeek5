# Generated by Django 2.2.7 on 2019-11-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='area',
            field=models.CharField(choices=[('MA', 'MECATRONICA'), ('MI', 'MANTENIMIENTO'), ('TI', 'TECNOLOGIAS DE LA INFORMACION'), ('DN', 'DESARROLLO DE NEGOCIOS'), ('LI', 'LENGUA INGLESA')], max_length=2),
        ),
    ]
