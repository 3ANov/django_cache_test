# Generated by Django 3.2.4 on 2021-06-05 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=200)),
                ('address', models.TextField(blank=True)),
                ('telephone_number', models.CharField(blank=True, max_length=100)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('logo_image', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name_plural': 'Основные настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('icon', models.CharField(max_length=60)),
                ('settings', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='site_settings.sitesettings')),
            ],
            options={
                'verbose_name_plural': 'Ссылки на социальные сети',
            },
        ),
    ]
