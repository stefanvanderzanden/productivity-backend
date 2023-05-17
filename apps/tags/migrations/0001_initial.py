# Generated by Django 4.2 on 2023-04-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, verbose_name='Tag naam')),
                ('slug', models.SlugField(unique=True, verbose_name='Tag slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]