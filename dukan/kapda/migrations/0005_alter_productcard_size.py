# Generated by Django 5.1.4 on 2024-12-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapda', '0004_alter_productcard_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcard',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=6),
        ),
    ]
