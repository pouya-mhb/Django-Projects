# Generated by Django 4.1.5 on 2023-01-30 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish_date',)},
        ),
    ]
