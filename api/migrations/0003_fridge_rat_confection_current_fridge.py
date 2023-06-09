# Generated by Django 4.1.7 on 2023-03-12 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_confection_delete_item_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fridge_name', models.CharField(max_length=64)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('fridge_manufacturer', models.CharField(max_length=64)),
                ('fridge_volume', models.IntegerField(default=0)),
                ('fridge_description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Rat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rat_name', models.CharField(max_length=64)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('rat_species', models.CharField(max_length=64)),
                ('rat_weight', models.IntegerField(default=0)),
                ('rat_size', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='confection',
            name='current_fridge',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.fridge'),
            preserve_default=False,
        ),
    ]
