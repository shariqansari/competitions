# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Collaborators',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_tournament.competition_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=50)),
                ('competition', models.ForeignKey(related_name='competitors', to='tournament.Competition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_file', models.FileField(upload_to=b'entries')),
                ('comments', models.TextField()),
                ('competitor', models.ForeignKey(to='tournament.Competitor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('compete_start', models.DateTimeField()),
                ('compete_end', models.DateTimeField()),
                ('voting_start', models.DateTimeField()),
                ('voting_end', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GauntletRound',
            fields=[
                ('round_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tournament.Round')),
                ('block', models.ForeignKey(to='tournament.Block')),
            ],
            options={
                'abstract': False,
            },
            bases=('tournament.round',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TournamentRound',
            fields=[
                ('round_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tournament.Round')),
                ('bracket', models.ForeignKey(to='tournament.Bracket')),
            ],
            options={
                'abstract': False,
            },
            bases=('tournament.round',),
        ),
        migrations.AddField(
            model_name='round',
            name='competition',
            field=models.ForeignKey(to='tournament.Competition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='round',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_tournament.round_set+', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='round',
            field=models.ForeignKey(related_name='entries', to='tournament.Round'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competitor',
            name='team',
            field=models.ForeignKey(blank=True, to='tournament.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competitor',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collaborators',
            name='entry',
            field=models.ForeignKey(related_name='collaborators', to='tournament.Entry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collaborators',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='battle',
            name='challenger_a',
            field=models.ForeignKey(related_name='+', to='tournament.Competitor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='battle',
            name='challenger_b',
            field=models.ForeignKey(related_name='+', to='tournament.Competitor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='battle',
            name='round',
            field=models.ForeignKey(related_name='battles', to='tournament.TournamentRound'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='battle',
            name='winner',
            field=models.ForeignKey(related_name='+', blank=True, to='tournament.Competitor', null=True),
            preserve_default=True,
        ),
    ]
