# Generated by Django 2.1.5 on 2019-01-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorrecords', '0006_auto_20190126_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incompatible',
            name='medication',
            field=models.TextField(max_length=2048),
        ),
    ]
