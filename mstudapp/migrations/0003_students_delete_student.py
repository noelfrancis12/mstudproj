# Generated by Django 4.2 on 2023-05-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mstudapp', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('courses', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
