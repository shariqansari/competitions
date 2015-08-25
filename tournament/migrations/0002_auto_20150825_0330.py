# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='competition',
        ),
        migrations.AddField(
            model_name='block',
            name='competition',
            field=models.ForeignKey(default=1, to='tournament.Competition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bracket',
            name='competition',
            field=models.ForeignKey(default=1, to='tournament.Competition'),
            preserve_default=False,
        ),
    ]
