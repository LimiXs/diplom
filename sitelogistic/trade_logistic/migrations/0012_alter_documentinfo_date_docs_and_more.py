# Generated by Django 4.2.5 on 2023-12-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_logistic', '0011_alter_documentinfo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentinfo',
            name='date_docs',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дата доков'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='documents',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Документы'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_doc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='№ документов'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_nine',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='№ Длинной "9"'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_td',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Таможенное разрешение'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='path_doc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Путь'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Статус УВР'),
        ),
    ]
