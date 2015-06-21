# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=150, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('Image', models.ImageField(upload_to=b'images', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe')),
                ('Description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0430\u043a\u0446\u0438\u0438',
                'verbose_name_plural': '\u0410\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='ActionWares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Action', models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f', to='goods.Actions')),
            ],
            options={
                'verbose_name': '\u0410\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0410\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0442\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Parent', models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='goods.Categories', null=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Producers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u043e',
                'verbose_name_plural': '\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430',
            },
        ),
        migrations.CreateModel(
            name='PropertiesByCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Category', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='goods.Categories')),
                ('Property', models.ForeignKey(verbose_name=b'\xd0\xa1\xd0\xb2\xd0\xbe\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', to='goods.Properties')),
            ],
            options={
                'verbose_name': '\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c \u0442\u043e\u0432\u0430\u0440\u0430',
                'verbose_name_plural': '\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c \u0442\u043e\u0432\u0430\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='PropertiesValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Value', models.TextField()),
                ('Property', models.ForeignKey(verbose_name=b'\xd0\xa1\xd0\xb2\xd0\xbe\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', to='goods.Properties')),
            ],
            options={
                'verbose_name': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430',
                'verbose_name_plural': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432',
            },
        ),
        migrations.CreateModel(
            name='Wares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.CharField(max_length=50, verbose_name=b'\xd0\x90\xd1\x80\xd1\x82\xd0\xb8\xd0\xba\xd1\x83\xd0\xbb')),
                ('Name', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Image', models.ImageField(upload_to=b'images', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('Description', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('Category', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='goods.Categories')),
                ('Producer', models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to='goods.Producers')),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='WaresImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=150, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('Image', models.ImageField(upload_to=b'images', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('Ware', models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80', to='goods.Wares')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='WaresProperties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('Property', models.ForeignKey(verbose_name=b'\xd0\xa1\xd0\xb2\xd0\xbe\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', to='goods.Properties')),
                ('Value', models.ForeignKey(verbose_name=b'\xd0\x97\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb2\xd0\xbe\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0', to='goods.PropertiesValues')),
                ('Ware', models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80', to='goods.Wares')),
            ],
            options={
                'verbose_name': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432 \u0442\u043e\u0432\u0430\u0440\u0430',
                'verbose_name_plural': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0441\u0432\u043e\u0439\u0441\u0442\u0432 \u0442\u043e\u0432\u0430\u0440\u0430',
            },
        ),
        migrations.AddField(
            model_name='actionwares',
            name='Ware',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80', to='goods.Wares'),
        ),
    ]
