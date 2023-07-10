# Generated by Django 4.2.1 on 2023-06-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comandas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Comandas',
            },
        ),
    ]