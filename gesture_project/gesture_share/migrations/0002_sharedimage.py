# Generated by Django 5.1.4 on 2024-12-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gesture_share', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=255)),
                ('user_ip', models.GenericIPAddressField()),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
