# Generated by Django 3.1.1 on 2023-11-06 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
