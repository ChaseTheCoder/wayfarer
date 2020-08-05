# Generated by Django 3.1 on 2020-08-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200805_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='Post Date')),
                ('post_city', models.CharField(choices=[('L', 'London'), ('S', 'Sydney'), ('T', 'Tokyo'), ('P', 'Paris')], default='L', max_length=10, verbose_name='Post City')),
            ],
        ),
    ]