# Generated by Django 3.0.3 on 2020-02-07 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_base', '0010_auto_20200206_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
    ]
