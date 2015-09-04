# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_round_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='previous_round',
            field=models.ForeignKey(related_name='next_round', blank=True, to='tournament.Round', null=True),
            preserve_default=True,
        ),
    ]
