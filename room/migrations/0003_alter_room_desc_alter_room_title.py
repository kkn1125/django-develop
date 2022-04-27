# Generated by Django 4.0.2 on 2022-04-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_alter_room_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='desc',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='방 설명'),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(max_length=100, verbose_name='방 제목'),
        ),
    ]