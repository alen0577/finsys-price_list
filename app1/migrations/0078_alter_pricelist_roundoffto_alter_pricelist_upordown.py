# Generated by Django 4.1.7 on 2023-07-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0077_rename_pricelist2_individual_pricelist_individual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='roundoffto',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='upordown',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
