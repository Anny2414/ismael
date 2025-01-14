# Generated by Django 3.2 on 2024-09-01 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('num_identificacion', models.IntegerField(unique=True)),
                ('correo', models.EmailField(max_length=80)),
                ('telefono', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estudiante', models.CharField(max_length=20)),
                ('apellido_estudiante', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=1)),
                ('correo_estudiante', models.EmailField(max_length=200)),
                ('telefono', models.CharField(max_length=11, unique=True)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_profesor', models.CharField(max_length=20)),
                ('apellido_profesor', models.CharField(max_length=20)),
                ('correo_profesor', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=20)),
                ('codigo_curso', models.IntegerField(unique=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad__.departamento')),
            ],
        ),
    ]
