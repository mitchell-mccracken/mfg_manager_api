# Generated by Django 3.2.4 on 2021-07-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0011_alter_quote_quote_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quote_notes',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]