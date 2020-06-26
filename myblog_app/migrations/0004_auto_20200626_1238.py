# Generated by Django 2.1.15 on 2020-06-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog_app', '0003_auto_20200626_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='myblogmodels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('discription', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='myblogmodel',
            name='discription',
            field=models.TextField(),
        ),
    ]