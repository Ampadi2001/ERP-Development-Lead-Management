# Generated by Django 4.2.7 on 2023-11-20 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_branches_adress_alter_branches_email_and_more'),
        ('STUDENTS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='qualification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.qualification'),
        ),
    ]