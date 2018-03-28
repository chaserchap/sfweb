# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Creature(models.Model):
	ALIGNMENTS = (('CE', 'Chaotic Evil'),
				  ('CN', 'Chaotic Neutral'),
				  ('CG', 'Chaotic Good'),
				  ('NE', 'Neutral Evil'),
				  ('TN', 'True Neutral'),
				  ('NG', 'Neutral Good'),
				  ('LE', 'Lawful Evil'),
				  ('LN', 'Lawful Neutral'),
				  ('LG', 'Lawful Good'))

	SIZES = (('F', 'Fine'),
			 ('D', 'Diminutive'),
			 ('T', 'Tiny'),
			 ('S', 'Small'),
			 ('M', 'Medium'),
			 ('L', 'Large'),
			 ('H', 'Huge'),
			 ('G', 'Gargantuan'),
			 ('C', 'Colossal'))

	name = models.CharField(max_length=50)
	cr = models.DecimalField(max_digits=5,
							 decimal_places=2)
	xp = models.IntegerField()
	race = models.CharField(max_length=50)
	graft = models.ManyToManyField(Graft)
	alignment = models.CharField(max_length=2,
						         choices=ALIGNMENTS,
						         default='TN')
	size = models.CharField(max_length=1,
							choices=SIZES,
							default='M')
	creature_type = models.ManyToManyField(CreatureType)
	creature_subtype = models.ManyToManyField(CreatureSubtype)
	initiative = models.IntegerField()
	senses = models.ManyToManyField(Senses)
	aura = models.ManyToManyField(Aura)
	hp = models.IntegerField()
	rp = models.IntegerField()
	eac = models.IntegerField()
	kac = models.IntegerField()
	fortitude = models.IntegerField()
	reflex = models.IntegerField()
	will = models.IntegerField()
	defensive_abilities = models.ManyToManyField(DefensiveAbilities)


class Graft(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)


class Senses(models.Model):
	title = models.CharField(max_length=50)
	sense_range = models.IntegerField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class Aura(models.Model):
	title = models.CharField(max_length=50)
	aura_range = models.IntegerField()
	dc = models.IntegerField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title','-dc')


class DefensiveAbilities(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)


class CreatureType(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)


class CreatureSubtype(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)
