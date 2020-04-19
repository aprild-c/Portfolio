# Generated by Django 2.1.5 on 2020-04-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('school', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('company', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
