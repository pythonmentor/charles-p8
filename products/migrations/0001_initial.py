# Generated by Django 3.0.2 on 2020-01-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('url', models.CharField(max_length=255)),
                ('categories', models.ManyToManyField(related_name='products', to='products.Category')),
            ],
        ),
    ]