# Generated by Django 4.2.5 on 2024-01-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_logistic', '0012_alter_documentinfo_date_docs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_path', models.CharField(blank=True, max_length=255, verbose_name='Полный путь')),
                ('file_name', models.CharField(max_length=30, verbose_name='Имя файла')),
                ('doc_number', models.CharField(max_length=70, verbose_name='Номер уведомления')),
                ('in_use', models.BooleanField(default=False, verbose_name='Путь найден')),
            ],
        ),
    ]
