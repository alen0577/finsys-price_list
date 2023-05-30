# Generated by Django 4.1.7 on 2023-05-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0070_pricelist_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelist2_individual',
            name='itemdetails',
        ),
        migrations.AddField(
            model_name='pricelist2_individual',
            name='itemname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pricelist2_individual',
            name='itemrate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]