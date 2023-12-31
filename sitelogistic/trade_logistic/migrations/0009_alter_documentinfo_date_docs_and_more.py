# Generated by Django 4.2.5 on 2023-12-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_logistic', '0008_alter_documentinfo_date_docs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentinfo',
            name='date_docs',
            field=models.CharField(max_length=255, null=True, verbose_name='Дата доков'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='documents',
            field=models.CharField(max_length=255, null=True, verbose_name='Документы'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_doc',
            field=models.CharField(max_length=255, null=True, verbose_name='№ документов'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_nine',
            field=models.CharField(max_length=30, null=True, verbose_name='№ Длинной "9"'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='num_transport',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='№ авто'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='path_doc',
            field=models.CharField(max_length=255, null=True, verbose_name='Скачать PDF'),
        ),
        migrations.AlterField(
            model_name='documentinfo',
            name='status',
            field=models.CharField(max_length=255, null=True, verbose_name='Статус УВР'),
        ),
    ]
