# Generated by Django 2.2 on 2021-07-02 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('powerOfBanking', '0004_cardbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardBoxWithImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='powerofbanking_cardboxwithimage', serialize=False, to='cms.CMSPlugin')),
                ('image', models.ImageField(upload_to='power_of_banking/images')),
                ('title', models.CharField(max_length=120)),
                ('subtitle', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
