# Generated by Django 4.0.4 on 2022-12-05 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0051_rename_pymnt_balance_sheet_bill_pymnt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance_sheet',
            name='acctype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profit_loss',
            name='acctype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='balance_sheet',
            name='account',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='balance_sheet',
            name='details',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
