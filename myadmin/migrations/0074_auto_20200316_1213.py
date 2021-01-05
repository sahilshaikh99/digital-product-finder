# Generated by Django 3.0.2 on 2020-03-16 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0073_auto_20200314_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_item_id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_item_type',
        ),
        migrations.AddField(
            model_name='review',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='myadmin.Brand'),
        ),
    ]