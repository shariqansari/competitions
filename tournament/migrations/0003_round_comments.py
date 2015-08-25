# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_auto_20150825_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='comments',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
