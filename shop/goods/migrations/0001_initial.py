# Generated by Django 4.0.4 on 2022-05-30 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25, verbose_name='Наименование продукта')),
                ('price', models.PositiveIntegerField(verbose_name='Цена за единицу товара')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(verbose_name='Запас на складе')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.product', verbose_name='Продукт на складе')),
            ],
        ),
    ]
