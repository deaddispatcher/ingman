# Generated by Django 4.2.4 on 2023-08-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
