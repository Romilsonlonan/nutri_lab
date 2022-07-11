# Generated by Django 4.0.6 on 2022-07-07 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('percentual_gordura', models.IntegerField()),
                ('percentual_musculo', models.IntegerField()),
                ('colesterol_hdl', models.IntegerField()),
                ('colesterol_ldl', models.IntegerField()),
                ('colesterol_total', models.IntegerField()),
                ('trigliceridios', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.pacientes')),
            ],
        ),
    ]
