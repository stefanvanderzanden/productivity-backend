# Generated by Django 4.2.1 on 2023-06-03 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubProject',
            fields=[
                ('code', models.CharField(help_text='Geef hier een code op', max_length=50, primary_key=True, serialize=False, verbose_name='Code')),
                ('name', models.CharField(help_text='Geef hier een naam op', max_length=50, verbose_name='Naam')),
                ('description', models.TextField(blank=True, help_text='Geef hier een omschrijving op', null=True, verbose_name='Omschrijving')),
                ('project', models.ForeignKey(help_text='Geef hier het project op waar dit project onder valt', on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='subproject',
            field=models.ForeignKey(blank=True, help_text='Geef hier het project op voor het ticket', null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.subproject', verbose_name='Project'),
        ),
    ]
