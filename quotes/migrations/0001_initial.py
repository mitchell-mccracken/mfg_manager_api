# Generated by Django 3.2.4 on 2021-07-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_title', models.CharField(max_length=200)),
                ('q_date_created', models.DateTimeField(verbose_name='date published')),
                ('customer_name', models.CharField(default='none', max_length=200)),
                ('contact_name', models.CharField(default='none', max_length=200)),
                ('customer_address', models.CharField(default='none', max_length=400)),
            ],
        ),
    ]
