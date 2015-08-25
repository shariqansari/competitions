from django.db import models
from django.contrib.auth.models import User
from polymorphic import PolymorphicModel

# General Models
class Competition(PolymorphicModel):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Round(PolymorphicModel):
    number = models.IntegerField()
    compete_start = models.DateTimeField()
    compete_end = models.DateTimeField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField()
    comments = models.TextField(null=True, blank=True)

class Team(models.Model):
    name = models.CharField(max_length=50)

class Competitor(models.Model):
    user = models.ForeignKey(User)
    artist_name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, related_name="competitors")
    team = models.ForeignKey(Team, null=True, blank=True)

class Entry(models.Model):
    round = models.ForeignKey(Round, related_name="entries")
    competitor = models.ForeignKey(Competitor)
    media_file = models.FileField(upload_to="entries")
    comments = models.TextField()

class Collaborators(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    artist_name = models.CharField(max_length=50)
    entry = models.ForeignKey(Entry, related_name="collaborators")
    
# Tournament Models
class Bracket(models.Model):
    competition = models.ForeignKey(Competition)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s: %s" % (self.competition.name, self.name)

class TournamentRound(Round):
    bracket = models.ForeignKey(Bracket)

class Battle(models.Model):
    round = models.ForeignKey(TournamentRound, related_name="battles")
    challenger_a = models.ForeignKey(Competitor, related_name="+")
    challenger_b = models.ForeignKey(Competitor, related_name="+")
    winner = models.ForeignKey(Competitor, related_name="+", null=True, blank=True)
    
    def loser(self):
        return [
            c for c 
            in [self.challenger_a, self.challenger_b] 
            if c is not self.winner
            ][0]
    
    def entries(self):
        entries = Entry.objects.filter(
            round=self.round, 
            competitor_id__in=[self.challenger_a.id, self.challenger_b.id]
            )

#Gauntlet Models

class Block(models.Model):
    competition = models.ForeignKey(Competition)
    number = models.IntegerField()

    def __unicode__(self):
        return "%s: Block %s" % (self.competition.name, self.number)

class GauntletRound(Round):
    block = models.ForeignKey(Block)

    def __unicode__(self):
        return "%s - Round %s" % (self.block, self.number)
