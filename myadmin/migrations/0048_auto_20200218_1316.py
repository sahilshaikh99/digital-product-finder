# Generated by Django 3.0.2 on 2020-02-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0047_auto_20200216_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='feature_has_value',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=1),
        ),
    ]