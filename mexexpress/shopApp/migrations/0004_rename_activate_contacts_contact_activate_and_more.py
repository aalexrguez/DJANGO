# Generated by Django 4.2.19 on 2025-03-12 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_rename_adddress_contacts_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='activate',
            new_name='contact_activate',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='address',
            new_name='contact_address',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='full_name',
            new_name='contact_full_name',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='phone',
            new_name='contact_phone',
        ),
    ]
