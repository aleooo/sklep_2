# Generated by Django 4.0 on 2022-01-24 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_address_country'),
        ('order', '0006_alter_order_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.address')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
            ],
            bases=('shop.address',),
        ),
    ]