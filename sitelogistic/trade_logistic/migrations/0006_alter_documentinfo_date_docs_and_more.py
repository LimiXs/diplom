# Generated by Django 4.2.5 on 2023-11-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_logistic', '0005_documentinfo_alter_note_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentinfo',
            name='date_docs',
            field=models.DateField(blank=True, verbose_name='Дата доков'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='date_placement',
            field=models.DateField(blank=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='documents',
            field=models.CharField(blank=True, max_length=150, verbose_name='Документы'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_doc',
            field=models.CharField(blank=True, max_length=150, verbose_name='№ документов'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_nine',
            field=models.CharField(blank=True, max_length=10, verbose_name='№ Длинной "9"'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_td',
            field=models.CharField(blank=True, max_length=50, verbose_name='Таможенное разрешение'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_transport',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='№ авто'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='path_doc',
            field=models.CharField(blank=True, max_length=150, verbose_name='Скачать PDF'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='status',
            field=models.CharField(blank=True, max_length=150, verbose_name='Статус УВР'),
        ),
    ]