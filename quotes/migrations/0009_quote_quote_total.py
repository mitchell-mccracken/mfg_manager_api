# Generated by Django 3.2.4 on 2021-07-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0008_delete_appuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quote_total',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
