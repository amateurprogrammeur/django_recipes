# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-28 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import positions.fields


class Migration(migrations.Migration):

    replaces = [('recipes', '0001_initial'), ('recipes', '0002_auto_20140904_2053'), ('recipes', '0003_auto_20170308_0717')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Maximum 120 characters', max_length=120, unique=True)),
                ('order_index', models.PositiveIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(help_text='Automatically generated from the title', unique=True)),
            ],
            options={
                'ordering': ['order_index'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('order', positions.fields.PositionField(blank=True, default=-1, null=True)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('name_sorted', models.CharField(default='', max_length=150)),
                ('conversion_factor', models.FloatField(blank=True, null=True)),
                ('name_plural', models.CharField(blank=True, max_length=150, null=True)),
                ('detail', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name_sorted'],
            },
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='FoodGroup|name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'FoodGroups',
                'verbose_name': 'FoodGroup',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('amountMax', models.FloatField(blank=True, null=True)),
                ('order_index', positions.fields.PositionField(blank=True, default=-1, null=True)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.Direction')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Food')),
            ],
            options={
                'ordering': ['direction', 'order_index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('keep', models.BooleanField(default=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='PrepMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='PrepMethod|name')),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Preparation Methods',
                'verbose_name': 'Preparation Method',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('prep_time', models.CharField(blank=True, max_length=100)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('serving_value', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ServingString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, verbose_name='ServingString|text')),
            ],
            options={
                'verbose_name_plural': 'Serving Strings',
                'verbose_name': 'Serving String',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Source|name')),
                ('url', models.URLField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Sources',
                'verbose_name': 'Source',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Unit|name')),
                ('name_abbrev', models.CharField(blank=True, max_length=60, verbose_name='Unit|name_abbrev')),
                ('plural_abbrev', models.CharField(blank=True, max_length=60, verbose_name='Unit|plural_abbrev')),
                ('type', models.IntegerField(choices=[(0, 'Other'), (1, 'Mass'), (2, 'Volume')])),
                ('system', models.IntegerField(choices=[(0, 'SI'), (1, 'Imperial')], null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Units',
                'verbose_name': 'Unit',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='serving_string',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.ServingString'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='sources',
            field=models.ManyToManyField(blank=True, to='recipes.Source'),
        ),
        migrations.AddField(
            model_name='photo',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='prep_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.PrepMethod'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Unit'),
        ),
        migrations.AddField(
            model_name='food',
            name='conversion_src_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='recipes.Unit'),
        ),
        migrations.AddField(
            model_name='food',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.FoodGroup'),
        ),
        migrations.AddField(
            model_name='direction',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.Direction'),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order_index'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='direction',
            options={'ordering': ['order', 'id'], 'verbose_name': 'Direction', 'verbose_name_plural': 'Directions'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['name_sorted'], 'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['direction', 'order_index', 'id'], 'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['title'], 'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipies'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Maximum 120 characters', max_length=120, unique=True, verbose_name='Category|name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Automatically generated from the title', unique=True),
        ),
        migrations.AlterField(
            model_name='direction',
            name='text',
            field=models.TextField(blank=True, verbose_name='Direction|text'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Food|name'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name_sorted',
            field=models.CharField(default='', max_length=150, verbose_name='Food|name_sorted'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Ingredient|amount'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(max_length=200, verbose_name='Photo|caption'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, verbose_name='Recipe|description'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='summary',
            field=models.CharField(blank=True, max_length=500, verbose_name='Recipe|summary'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Recipe|title'),
        ),
    ]
