# Generated by Django 3.0.7 on 2021-12-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pillarplus', '0002_auto_20211229_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileloader',
            name='form_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
