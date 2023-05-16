# Generated by Django 4.1.7 on 2023-05-16 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0068_balance_sheet_payments1_profit_loss_payments1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('types', models.CharField(choices=[('S', 'Sales'), ('P', 'Purchase')], default='S', max_length=10)),
                ('item_rate', models.CharField(choices=[('percentage', 'Markup or Markdown the item rates by a percentage'), ('individual_rate', 'Enter the rate individually for each item')], default='percentage', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('currency', models.CharField(default='Indian Rupee', max_length=255)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
