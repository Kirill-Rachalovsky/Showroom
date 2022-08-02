# Generated by Django 4.0.6 on 2022-08-02 09:48

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import src.core.abstractmodels


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_creation', models.DateField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Organization Name')),
                ('description', models.TextField(blank=True, help_text='<i>More information about your company...</i>', verbose_name='Description')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('start_year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='Year')),
                ('balance', models.PositiveIntegerField(default=500000, help_text='<i>Put your balance in dollars</i>', verbose_name='Balance')),
                ('car_priority', models.JSONField(default=src.core.abstractmodels.default_showroom_priorities)),
                ('total_sales', models.PositiveIntegerField(default=0)),
                ('price_increase', models.PositiveSmallIntegerField(default=30, help_text='<b>Enter the markup on the cars you sell</b>', validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name': 'Showroom',
                'verbose_name_plural': 'Showrooms',
            },
        ),
        migrations.CreateModel(
            name='ShowroomDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.PositiveSmallIntegerField(help_text='How many cars do I need to buy for the discount?', validators=[django.core.validators.MinValueValidator(0)])),
                ('discount', models.PositiveIntegerField(default=0, help_text='Enter the size of the discount in percent', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('data_start', models.DateField()),
                ('data_end', models.DateField(default=datetime.date(2022, 9, 1))),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='showroom.showroom')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
    ]
