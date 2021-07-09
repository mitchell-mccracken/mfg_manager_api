# Generated by Django 3.2.4 on 2021-07-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_alter_quote_part_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='part_cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6),
        ),
        migrations.AlterField(
            model_name='quote',
            name='part_qty',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
