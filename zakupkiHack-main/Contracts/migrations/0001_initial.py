# Generated by Django 4.0 on 2022-09-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('product_vat_rate', models.TextField(blank=True, null=True)),
                ('product_msr', models.TextField(blank=True, null=True)),
                ('product_characteristics', models.TextField(blank=True, null=True)),
                ('okpd2_code', models.TextField(blank=True, null=True)),
                ('okpd2_name', models.TextField(blank=True, null=True)),
                ('inn', models.TextField(blank=True, null=True)),
                ('country_code', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Contracts',
                'managed': False,
            },
        ),
    ]