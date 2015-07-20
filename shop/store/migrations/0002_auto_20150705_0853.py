# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=b'Verana', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='Verana', upload_to='itempics'),
            preserve_default=False,
        ),
    ]
