# Generated by Django 4.2.8 on 2024-02-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name of categoty')),
                ('image', models.ImageField(upload_to='category-images/')),
            ],
            options={
                'verbose_name': 'post category',
                'verbose_name_plural': 'post categories',
            },
        ),
    ]