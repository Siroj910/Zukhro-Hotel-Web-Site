# Generated by Django 2.2.14 on 2022-03-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingrooms',
            name='li1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pricingrooms',
            name='li2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pricingrooms',
            name='li3',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
