# Generated by Django 4.0.6 on 2022-07-21 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('thumb', models.ImageField(upload_to='thumb_cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('aula', models.FileField(upload_to='aulas')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.cursos')),
            ],
        ),
    ]
