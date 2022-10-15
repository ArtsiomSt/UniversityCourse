# Generated by Django 4.0.6 on 2022-10-14 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainroot', '0002_computer_title_memory_title_proccessor_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='title',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='title',
        ),
        migrations.RemoveField(
            model_name='proccessor',
            name='title',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainroot.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='Prod', max_length=30),
        ),
    ]