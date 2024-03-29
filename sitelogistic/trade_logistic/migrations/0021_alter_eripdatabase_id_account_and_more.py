# Generated by Django 4.2.5 on 2024-03-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_logistic', '0020_alter_eripdatabase_id_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eripdatabase',
            name='id_account',
            field=models.CharField(max_length=20, null=True, verbose_name='Счёт договора'),
        ),
        migrations.AlterField(
            model_name='eripdatabase',
            name='payer_name',
            field=models.CharField(max_length=100, null=True, verbose_name='ФИО плательщика'),
        ),
    ]
