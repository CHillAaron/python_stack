# Generated by Django 2.2.4 on 2020-12-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_app', '0006_auto_20201215_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojosai',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]