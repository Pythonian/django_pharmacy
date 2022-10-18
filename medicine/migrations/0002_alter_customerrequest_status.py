# Generated by Django 4.0.6 on 2022-10-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('D', 'Done')], default='P', max_length=1, verbose_name='Request status'),
        ),
    ]
