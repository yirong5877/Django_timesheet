# Generated by Django 4.0.6 on 2022-07-18 13:38

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuppliesCodeMaintenance',
            fields=[
                ('SuppliesCodeID', models.AutoField(primary_key=True, serialize=False)),
                ('SCDescription', models.CharField(max_length=100, verbose_name='Supplies Code')),
                ('SCBillingCode', models.CharField(max_length=20, verbose_name='Billing Codes')),
                ('SCDefaultRates', models.IntegerField(blank=True, default=0, null=True, verbose_name='Default Hourly Rates')),
                ('SCActive', models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1, verbose_name='Active Status')),
                ('LastUpdatedBy', models.IntegerField(blank=True, null=True)),
                ('SCDateAdded', models.DateField(auto_now_add=True, verbose_name='Date Added')),
                ('SCDateUpdated', models.DateField(auto_now=True, verbose_name='Date Updated')),
                ('SCDateActivated', models.DateField(null=True, verbose_name='Date Activated')),
            ],
            managers=[
                ('dj_supplies_code', django.db.models.manager.Manager()),
            ],
        ),
    ]
