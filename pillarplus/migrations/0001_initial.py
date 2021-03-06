# Generated by Django 3.0.7 on 2021-12-28 16:46

from django.db import migrations, models
import pillarplus.dirs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileLoader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to=pillarplus.dirs.upload_csv_files)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(blank=True, default='', max_length=25)),
                ('options', models.CharField(blank=True, default='', max_length=100)),
                ('mandatory', models.BooleanField(max_length=10)),
            ],
        ),
    ]
