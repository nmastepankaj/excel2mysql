# Generated by Django 2.2.14 on 2021-09-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file_name', models.CharField(max_length=256)),
                ('sql_file_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UploadCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
