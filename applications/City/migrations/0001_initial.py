# Generated by Django 4.2.6 on 2023-12-01 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryCode', models.CharField(max_length=30, verbose_name='CountryCode ')),
            ],
            options={
                'verbose_name': 'CountryCode ',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('ID', models.IntegerField(max_length=30, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=35, verbose_name='Name')),
                ('District', models.CharField(max_length=20, verbose_name='District')),
                ('Population', models.IntegerField(max_length=20, verbose_name='Population')),
                ('Mayor', models.CharField(max_length=30, verbose_name='Mayor')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='Citys')),
                ('CountryCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Country.country')),
            ],
            options={
                'verbose_name': 'Name City',
                'verbose_name_plural': 'Names Citys',
            },
        ),
    ]
