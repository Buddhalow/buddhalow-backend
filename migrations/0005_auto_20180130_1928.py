# Generated by Django 2.0.1 on 2018-01-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddhalow', '0004_aqtivity_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sport',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
