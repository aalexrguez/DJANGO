# Generated by Django 4.2.19 on 2025-03-14 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_rename_activate_contacts_contact_activate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='contact_email',
            field=models.EmailField(default='alex@gmail.com', max_length=150),
        ),
    ]
