# Generated by Django 3.2.4 on 2021-06-09 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=300, null=True)),
                ('text', models.CharField(max_length=1000, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]