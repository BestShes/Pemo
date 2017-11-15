# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0005_remove_category_user'),
        ('user', '0008_member_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memo.Category')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='categories',
            field=models.ManyToManyField(through='user.MemberCategory', to='memo.Category'),
        ),
    ]