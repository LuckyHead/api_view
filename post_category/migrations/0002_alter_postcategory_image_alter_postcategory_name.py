# Generated by Django 4.2.8 on 2024-02-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='image',
            field=models.ImageField(editable=False, upload_to='category-images/'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='name',
            field=models.CharField(editable=False, max_length=256, verbose_name='Name of categoty'),
        ),
    ]
