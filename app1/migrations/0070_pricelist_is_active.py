# Generated by Django 4.1.7 on 2023-05-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0069_pricelist_pricelist2_individual_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelist',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]