# Generated by Django 4.1.5 on 2023-06-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dozecafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee_section_2',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
