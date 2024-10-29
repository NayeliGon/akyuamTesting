# Generated by Django 5.1.1 on 2024-10-09 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_dependenciaadictiva_escolaridad_estadocivil_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bienes',
            fields=[
                ('id_bien', models.AutoField(primary_key=True, serialize=False)),
                ('bien', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAntecedente',
            fields=[
                ('id_antecedente', models.AutoField(primary_key=True, serialize=False)),
                ('antecedente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_expediente', models.CharField(max_length=50)),
                ('referente', models.CharField(max_length=100)),
                ('hora_ingreso', models.TimeField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('dpi', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('lectura_escritura', models.BooleanField()),
                ('profesion', models.CharField(max_length=100)),
                ('ocupacion', models.CharField(max_length=100)),
                ('direccion_trabajo', models.CharField(max_length=100)),
                ('telefono_trabajo', models.CharField(max_length=15)),
                ('antecedentes_enfermedad', models.BooleanField()),
                ('enfermedad', models.CharField(max_length=100)),
                ('presenta_discapacidad', models.BooleanField()),
                ('discapacidad', models.CharField(max_length=100)),
                ('estado_gestacion', models.BooleanField()),
                ('tiempo_gestacion', models.CharField(max_length=15)),
                ('dependencia_adictiva', models.BooleanField()),
                ('apoyo_familiar', models.BooleanField()),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.dependenciaadictiva')),
                ('escolaridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.escolaridad')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.estadocivil')),
                ('estado_vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.estadovivienda')),
                ('etnia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.etnia')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.idioma')),
                ('municipio_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direccion', to='sistema.municipio')),
                ('municipio_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nacimiento', to='sistema.municipio')),
                ('relacion_afinidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.relacionafinidad')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.religion')),
            ],
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=10)),
                ('es_reconocido', models.BooleanField()),
                ('es_estudiante', models.BooleanField()),
                ('establecimiento', models.CharField(max_length=100)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.genero')),
                ('participante_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.participante')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenciaFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('participante_familiar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.participante')),
                ('relacion_afinidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.relacionafinidad')),
            ],
        ),
        migrations.CreateModel(
            name='Hecho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_violencia', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('descripcion_hecho', models.TextField()),
                ('denuncias', models.BooleanField()),
                ('fecha_denuncia', models.DateField()),
                ('institucion_denuncia', models.TextField()),
                ('municipio_acontecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.municipio')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.participante')),
                ('tipo_violencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.tipoantecedente')),
            ],
        ),
        migrations.CreateModel(
            name='Agresor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('dpi', models.CharField(max_length=20)),
                ('caracteristicas_fisicas', models.TextField()),
                ('lectura_escritura', models.BooleanField()),
                ('direccion', models.CharField(max_length=100)),
                ('actividad_laboral', models.CharField(max_length=100)),
                ('nombre_lugar_trabajo', models.CharField(max_length=50)),
                ('direccion_trabajo', models.CharField(max_length=100)),
                ('telefono_trabajo', models.CharField(max_length=20)),
                ('ingreso_mensual', models.CharField(max_length=50)),
                ('posee_bienes', models.BooleanField()),
                ('otros_bienes', models.TextField()),
                ('antecedentes_conflictividad', models.BooleanField()),
                ('otros_antecedentes_conflic', models.TextField()),
                ('antecedentes_enfermedad', models.BooleanField()),
                ('descripcion_enfermedad', models.TextField()),
                ('dependencias_adictivas', models.BooleanField()),
                ('otras_dependencias', models.TextField()),
                ('usa_armas', models.BooleanField()),
                ('descripcion_armas', models.TextField()),
                ('referencias_personales', models.TextField()),
                ('observaciones', models.TextField()),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.dependenciaadictiva')),
                ('escolaridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.escolaridad')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.estadocivil')),
                ('etnia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.etnia')),
                ('municipio_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nacimiento_agresor', to='sistema.municipio')),
                ('relacion_afinidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.relacionafinidad')),
                ('bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.bienes')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.participante')),
                ('tipo_antecedente_conflic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.tipoantecedente')),
            ],
        ),
    ]
