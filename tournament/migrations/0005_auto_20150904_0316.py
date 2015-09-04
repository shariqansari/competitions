# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_round_previous_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='competition',
            field=models.ForeignKey(related_name='blocks', to='tournament.Competition'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gauntletround',
            name='block',
            field=models.ForeignKey(related_name='rounds', to='tournament.Block'),
            preserve_default=True,
        ),
    ]
