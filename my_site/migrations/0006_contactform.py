# Generated by Django 4.1.7 on 2023-03-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_projectimages_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=1200)),
            ],
        ),
    ]
