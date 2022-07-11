# Generated by Django 4.0.6 on 2022-07-11 13:31

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code_class', models.CharField(max_length=100)),
                ('billing_code', models.CharField(max_length=20)),
                ('hourly_rate', models.IntegerField(default='$16/Hr')),
                ('active', models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1)),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='date added')),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_active', models.DateField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Equipment Codes',
                'db_table': 'Equipment Code Maintenance',
            },
            managers=[
                ('dj_equipment_code', django.db.models.manager.Manager()),
            ],
        ),
    ]
