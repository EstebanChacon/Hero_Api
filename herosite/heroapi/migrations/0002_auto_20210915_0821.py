# Generated by Django 3.2.7 on 2021-09-15 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Superpower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='hero',
            name='publishers',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='heroapi.publisher'),
        ),
        migrations.AddField(
            model_name='hero',
            name='superpowers',
            field=models.ManyToManyField(to='heroapi.Superpower'),
        ),
    ]
