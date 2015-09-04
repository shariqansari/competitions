# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_auto_20150904_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='previous_round',
            field=models.OneToOneField(related_name='next_round', null=True, blank=True, to='tournament.Round'),
            preserve_default=True,
        ),
    ]
