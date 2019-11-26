# Generated by Django 2.2.7 on 2019-11-23 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('Apellido', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('rfc', models.CharField(max_length=13)),
                ('sexo', models.CharField(choices=[('F', 'FEMENINO'), ('M', 'MASCULINO')], max_length=1)),
                ('edo_civil', models.CharField(choices=[('S', 'SOLTER@'), ('C', 'CASAD@'), ('D', 'DIVORCIAD@'), ('V', 'VIUD@'), ('EC', 'EN UNA RELACION COMPLICADA')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Persona')),
                ('matricula', models.CharField(max_length=19)),
                ('grado', models.CharField(choices=[('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'), ('6', 'Sexto'), ('EST', 'Estadias')], max_length=2)),
                ('area', models.CharField(choices=[('MA', 'MECATRONICA'), ('MI', 'MANTENIMIENTO'), ('TI', 'TECNOLOGIAS DE LA INFORMACION'), ('DN', 'DESARROLLO DE NEGOCIOS'), ('LI', 'LENGUA INGLESA')], max_length=1)),
                ('promedio', models.FloatField()),
            ],
            bases=('personas.persona',),
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Persona')),
                ('noEmpleado', models.CharField(max_length=20)),
                ('antiguedad', models.IntegerField(blank=True)),
                ('areat', models.CharField(choices=[('AC', 'ACADEMIA'), ('LE', 'LENGUAS EXTRANJERAS'), ('MI', 'MANTENIMIENTO'), ('AD', 'ADMINISTRATIVAS')], max_length=2)),
                ('t_jornada', models.CharField(choices=[('TC', 'TIEMPO COMPLETO'), ('MD', 'MEDIO TIEMPO')], max_length=2)),
                ('tiene_oficio', models.BooleanField(default=False)),
            ],
            bases=('personas.persona',),
        ),
        migrations.CreateModel(
            name='Egresados',
            fields=[
                ('estudiante_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Estudiante')),
                ('generacion', models.CharField(max_length=19)),
                ('no_cedula', models.CharField(max_length=39)),
                ('titulo', models.CharField(max_length=4)),
            ],
            bases=('personas.estudiante',),
        ),
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('trabajador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Trabajador')),
                ('oficio_n', models.CharField(max_length=30)),
                ('experiencia', models.IntegerField()),
            ],
            bases=('personas.trabajador',),
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('trabajador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Trabajador')),
                ('hrs_laboradas', models.IntegerField()),
                ('sueldo_hr', models.FloatField()),
            ],
            bases=('personas.trabajador',),
        ),
    ]