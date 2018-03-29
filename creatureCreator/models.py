# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import validators
from django.db import models


class Array(models.Model):
    ARRAYS = (('C', 'Combatant'),
              ('E', 'Expert'),
              ('S', 'Spellcaster'))
    CR = (('third', '1/3'),
          ('half', '1/2'),
          ('1', '1'),
          ('2', '2'),
          ('3', '3'),
          ('4', '4'),
          ('5', '5'),
          ('6', '6'),
          ('7', '7'),
          ('8', '8'),
          ('9', '9'),
          ('10', '10'),
          ('11', '11'),
          ('12', '12'),
          ('13', '13'),
          ('14', '14'),
          ('15', '15'),
          ('16', '16'),
          ('17', '17'),
          ('18', '18'),
          ('19', '19'),
          ('20', '20'),
          ('21', '21'),
          ('22', '22'),
          ('23', '23'),
          ('24', '24'),
          ('25', '25'))

    title = models.CharField(
        max_length=1,
        choices=ARRAYS)
    cr = models.CharField(
        max_length=3,
        choices=CR)
    eac = models.IntegerField()
    kac = models.IntegerField()
    fort = models.IntegerField()
    ref = models.IntegerField()
    will = models.IntegerField()
    hp = models.IntegerField()
    ability_dc = models.IntegerField()
    spell_dc_base = models.IntegerField()
    ability_score_modifiers = models.CharField(
        max_length=20,
        validators=[validators.int_list_validator(allow_negative=True)])
    special_abilities_count = models.IntegerField()
    master_skills_modifier = models.IntegerField()
    good_skills_modifier = models.IntegerField()


class CreatureTypeGraft(models.Model):
    creature_type = models.CharField(max_length=20)
    creature_description = models.TextField()
    traits = models.TextField()
    adjustments = models.TextField()

    def __str__(self):
        return self.creature_type

    class meta:
        ordering = ('creature_type',)


class CreatureSubtypeGraft(models.Model):
    creature_type = models.CharField(max_length=20)
    creature_description = models.TextField()
    traits = models.TextField()
    adjustments = models.TextField()

    def __str__(self):
        return self.creature_type

    class meta:
        ordering = ('creature_type',)


class AbilitiesByCR(models.Model):
    SOURCES = (
        ('URC', 'Universal Creature Rules'),
        ('FTS', 'Feats'),
        ('FRE', 'Free'),
        ('ADJ', 'Adjustment'))
    CR = (('third', '1/3'),
          ('half', '1/2'),
          ('1', '1'),
          ('2', '2'),
          ('3', '3'),
          ('4', '4'),
          ('5', '5'),
          ('6', '6'),
          ('7', '7'),
          ('8', '8'),
          ('9', '9'),
          ('10', '10'),
          ('11', '11'),
          ('12', '12'),
          ('13', '13'),
          ('14', '14'),
          ('15', '15'),
          ('16', '16'),
          ('17', '17'),
          ('18', '18'),
          ('19', '19'),
          ('20', '20'),
          ('21', '21'),
          ('22', '22'),
          ('23', '23'),
          ('24', '24'),
          ('25', '25'))

    cr = models.CharField(
        max_length=3,
        choices=CR)
    ability_source = models.CharField(
        max_length=3,
        choices=SOURCES)
    ability_count = models.TextField()


class Skills(models.Model):
    skill_title = models.CharField(max_length=20)
    skill_description = models.TextField()


class ClassGraft(models.Model):
    class_title = models.CharField(max_length=12)
    class_description = models.TextField()
    special_rules = models.TextField()
    required_array = models.ManyToManyField(Array)
    adjustments = models.TextField()
    skills = models.ManyToManyField(Skills)
    ability_score_modifiers = models.TextField()
    gear = models.TextField()
    abilities_by_cr = models.ManyToManyField(AbilitiesByCR)


class Template(models.Model):
    ALIGNMENTS = (
        ('CE', 'Chaotic Evil'),
        ('CN', 'Chaotic Neutral'),
        ('CG', 'Chaotic Good'),
        ('NE', 'Neutral Evil'),
        ('TN', 'True Neutral'),
        ('NG', 'Neutral Good'),
        ('LE', 'Lawful Evil'),
        ('LN', 'Lawful Neutral'),
        ('LG', 'Lawful Good'))
    CR = (('third', 'CR 1/3'),
          ('half', 'CR 1/2'),
          ('1', 'CR 1'),
          ('2', 'CR 2'),
          ('3', 'CR 3'),
          ('4', 'CR 4'),
          ('5', 'CR 5'),
          ('6', 'CR 6'),
          ('7', 'CR 7'),
          ('8', 'CR 8'),
          ('9', 'CR 9'),
          ('10', 'CR 10'),
          ('11', 'CR 11'),
          ('12', 'CR 12'),
          ('13', 'CR 13'),
          ('14', 'CR 14'),
          ('15', 'CR 15'),
          ('16', 'CR 16'),
          ('17', 'CR 17'),
          ('18', 'CR 18'),
          ('19', 'CR 19'),
          ('20', 'CR 20'),
          ('21', 'CR 21'),
          ('22', 'CR 22'),
          ('23', 'CR 23'),
          ('24', 'CR 24'),
          ('25', 'CR 25'))

    min_cr = models.CharField(
        max_length=3,
        choices=CR)
    grafts = models.ManyToManyField(CreatureSubtypeGraft)
    alignment = models.CharField(
        max_length=2,
        choices=ALIGNMENTS)
    traits = models.TextField()


class SpecialAbilities(models.Model):
    SOURCES = (
        ('URC', 'Universal Creature Rules'),
        ('FTS', 'Feats'),
        ('FRE', 'Free'),
        ('ADJ', 'Adjustment'))

    # Will probably require many more columns
    title = models.CharField(max_length=50)
    description = models.TextField()
    source = models.CharField(
        max_length=3,
        choices=SOURCES)


class Spells(models.Model):
    SAVES = (
        ('FORT', 'Fortitude'),
        ('REF', 'Reflex'),
        ('WILL', 'Will'))
    title = models.CharField(max_length=50)
    description = models.TextField()
    school = models.CharField(max_length=50)
    casting_time = models.CharField(max_length=20)
    spell_range = models.CharField(max_length=50)
    effect = models.TextField()
    duration = models.TextField()
    saving_throw = models.CharField(
        max_length=4,
        choices=SAVES)
    spell_resistance = models.BooleanField()


class Senses(models.Model):
    title = models.CharField(max_length=50)
    subtype = models.CharField(max_length=50)
    description = models.TextField()
    sense_range = models.IntegerField()


class Aura(models.Model):
    title = models.CharField(max_length=50)
    effect = models.TextField()
    aura_range = models.IntegerField()
    DC = models.IntegerField()


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
    CR = (('third', 'CR 1/3'),
          ('half', 'CR 1/2'),
          ('1', 'CR 1'),
          ('2', 'CR 2'),
          ('3', 'CR 3'),
          ('4', 'CR 4'),
          ('5', 'CR 5'),
          ('6', 'CR 6'),
          ('7', 'CR 7'),
          ('8', 'CR 8'),
          ('9', 'CR 9'),
          ('10', 'CR 10'),
          ('11', 'CR 11'),
          ('12', 'CR 12'),
          ('13', 'CR 13'),
          ('14', 'CR 14'),
          ('15', 'CR 15'),
          ('16', 'CR 16'),
          ('17', 'CR 17'),
          ('18', 'CR 18'),
          ('19', 'CR 19'),
          ('20', 'CR 20'),
          ('21', 'CR 21'),
          ('22', 'CR 22'),
          ('23', 'CR 23'),
          ('24', 'CR 24'),
          ('25', 'CR 25'))
    SIZES = (('F', 'Fine'),
             ('D', 'Diminutive'),
             ('T', 'Tiny'),
             ('S', 'Small'),
             ('M', 'Medium'),
             ('L', 'Large'),
             ('H', 'Huge'),
             ('G', 'Gargantuan'),
             ('C', 'Colossal'))
    cr = models.CharField(max_length=5,
                          choices=CR,
                          default='1')
    xp = models.IntegerField(default=0)
    race = models.CharField(max_length=50,
                            null=True)
    alignment = models.CharField(max_length=2,
                                 choices=ALIGNMENTS,
                                 default='TN')
    size = models.CharField(max_length=1,
                            choices=SIZES,
                            default='M')
    creature_type = models.ForeignKey(CreatureTypeGraft,
                                      null=True)
    creature_subtype = models.ForeignKey(CreatureSubtypeGraft,
                                         null=True)
    initiative = models.IntegerField(default=0)
    senses = models.ManyToManyField(Senses)
    aura = models.ManyToManyField(Aura)
    hp = models.IntegerField(default=0)
    rp = models.IntegerField(default=0)
    eac = models.IntegerField(default=0)
    kac = models.IntegerField(default=0)
    fortitude = models.IntegerField(default=0)
    reflex = models.IntegerField(default=0)
    will = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    array = models.ForeignKey(Array,
                              null=True)
    creature_class = models.ForeignKey(ClassGraft,
                                       null=True)
    creature_template = models.ForeignKey(Template,
                                          null=True)
    special_abilities = models.ManyToManyField(SpecialAbilities)
    skills = models.ManyToManyField(Skills)
    spells = models.ManyToManyField(Spells)
