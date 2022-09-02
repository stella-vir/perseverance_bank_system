# Generated by Django 4.1 on 2022-09-02 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Doing business with us since ')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_text', models.CharField(max_length=200)),
                ('defaults', models.IntegerField(default=-999999999)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perseverance.customer')),
            ],
            options={
                'verbose_name_plural': 'Balance',
            },
        ),
    ]
