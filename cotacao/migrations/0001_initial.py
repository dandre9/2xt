# Generated by Django 2.0.1 on 2018-01-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provedor', models.CharField(max_length=250)),
                ('produto', models.CharField(max_length=250)),
                ('preco', models.FloatField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=250)),
            ],
        ),
    ]
