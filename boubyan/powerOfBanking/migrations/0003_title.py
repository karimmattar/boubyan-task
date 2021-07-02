# Generated by Django 2.2 on 2021-07-01 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('powerOfBanking', '0002_cardicon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='powerofbanking_title', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=180)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]