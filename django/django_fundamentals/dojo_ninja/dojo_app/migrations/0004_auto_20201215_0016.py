# Generated by Django 2.2.4 on 2020-12-15 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_app', '0003_auto_20201214_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojosai',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='ninja',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
