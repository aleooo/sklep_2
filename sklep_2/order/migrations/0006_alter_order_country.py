# Generated by Django 4.0 on 2022-01-11 19:56

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=60),
        ),
    ]