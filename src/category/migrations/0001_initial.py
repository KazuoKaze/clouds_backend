# Generated by Django 5.0.9 on 2024-10-18 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='category.category')),
            ],
            options={
                'verbose_name_plural': 'SubCategory',
                'ordering': ['-timestamp'],
            },
        ),
    ]
