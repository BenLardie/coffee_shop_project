# Generated by Django 2.2 on 2019-04-05 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redeye', '0002_auto_20190405_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='redeye.Menu'),
        ),
    ]