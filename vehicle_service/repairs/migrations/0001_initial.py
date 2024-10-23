# Generated by Django 5.1.2 on 2024-10-23 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('repair_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_type', models.CharField(choices=[('repair', 'Repair'), ('purchase', 'New Purchase')], max_length=10)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairs.component')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairs.vehicle')),
            ],
        ),
    ]