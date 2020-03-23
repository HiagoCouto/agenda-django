# Generated by Django 2.2.11 on 2020-03-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_event', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]