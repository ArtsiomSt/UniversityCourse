# Generated by Django 4.0.6 on 2022-11-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainroot', '0005_alter_proccessor_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='connection_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='memory',
            name='mem_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]