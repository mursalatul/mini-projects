# Generated by Django 5.0.2 on 2024-03-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allappurl',
            name='url_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
