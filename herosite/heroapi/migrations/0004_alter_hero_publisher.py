# Generated by Django 3.2.7 on 2021-09-23 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroapi', '0003_rename_publishers_hero_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='publisher',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='heroapi.publisher'),
        ),
    ]
