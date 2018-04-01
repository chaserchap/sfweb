# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
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
    base_spell_dc = models.IntegerField()
    high_ability_mod = models.IntegerField()
    med_ability_mod = models.IntegerField()
    low_ability_mod = models.IntegerField()
    special_abilities_count = models.IntegerField()
    master_skills_modifier = models.IntegerField()
    good_skills_modifier = models.IntegerField()
    high_attack_bonus = models.IntegerField()
    low_attack_bonus = models.IntegerField()
    ranged_energy_attack = models.CharField(max_length=15)
    ranged_kinetic_attack = models.CharField(max_length=15)
    standard_melee_attack = models.CharField(max_length=15)
    three_melee_attack = models.CharField(max_length=15)
    four_melee_attack = models.CharField(max_length=15)


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
    skill_modifier = models.IntegerField(default=5)


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
    TYPES = (
        ('ARA', 'Aura'),
        ('OFF', 'Offensive Ability'),
        ('DEF', 'Defensive Ability'),
        ('SNS', 'Sense'),
        ('IMM', 'Immunities'),
        ('OTH', 'Other'))
    ORIGIN = (
        ('EX', 'Ex'),
        ('SU', 'Su'),
        ('SP', 'Sp'))

    # Need to track origin (Ex, Su, and the other one)

    # Will probably require MANY more columns
    title = models.CharField(max_length=50)
    subtype = models.CharField(max_length=20,
                               null=True)
    ability_range = models.CharField(max_length=20,
                                     null=True)
    ability_type = models.CharField(max_length=3,
                                    choices=TYPES)
    description = models.TextField(null=True)
    source = models.CharField(
        max_length=3,
        choices=SOURCES,
        null=True)
    origin = models.CharField(
        max_length=2,
        choices=ORIGIN)


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
    subtype = models.CharField(max_length=50, null=True)
    description = models.TextField()
    sense_range = models.IntegerField()


class Immunities(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()


class Aura(models.Model):
    title = models.CharField(max_length=50)
    effect = models.TextField()
    aura_range = models.IntegerField()
    DC = models.IntegerField()


class Speed(models.Model):
    title = models.CharField(max_length=20)
    distance = models.IntegerField(default=30)


class Attack(models.Model):
    ATTACKS = (('M', 'Melee'),
               ('R', 'Ranged'))
    title = models.CharField(max_length=20)
    # Need a validator for dice attacks
    damage = models.CharField(max_length=20)
    add_damage = models.IntegerField()
    damage_type = models.CharField(max_length=20)
    mod = models.IntegerField()
    critical = models.CharField(max_length=20)
    three_attack = models.BooleanField(default=False)
    four_attack = models.BooleanField(default=False)
    against_eac = models.BooleanField(default=False)
    attack_type = models.CharField(max_length=1,
                                   choices=ATTACKS)
    additional_info = models.TextField(null=True)


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
    ABILITIES = (('STR', 'Strength'),
                 ('DEX', 'Dexterity'),
                 ('CON', 'Constitution'),
                 ('INT', 'Intelligence'),
                 ('WIS', 'Wisdom'),
                 ('CHA', 'Charisma'))
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
    hp = models.IntegerField(default=0)
    rp = models.IntegerField(default=0)
    eac = models.IntegerField(default=0)
    kac = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    fortitude = models.IntegerField(default=0)
    reflex = models.IntegerField(default=0)
    will = models.IntegerField(default=0)
    ability_dc = models.IntegerField(default=0)
    base_spell_dc = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="Creature Name")
    high_ability = models.CharField(max_length=3,
                                    choices=ABILITIES,
                                    null=True,
                                    default=True)
    med_ability = models.CharField(max_length=3,
                                   choices=ABILITIES,
                                   null=True,
                                   default=True)
    low_ability = models.CharField(max_length=3,
                                   choices=ABILITIES,
                                   null=True,
                                   default=True)
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    space = models.CharField(max_length=5,
                             default=5)
    reach = models.CharField(max_length=5,
                             default=5)
    charisma = models.IntegerField(default=10)
    attack = models.ManyToManyField(Attack,
                                    null=True)
    speed = models.IntegerField(default=20)
    special_movement = models.ManyToManyField(Speed,
                                              null=True)
    array = models.ForeignKey(Array,
                              null=True)
    creature_class = models.ForeignKey(ClassGraft,
                                       null=True)
    creature_template = models.ForeignKey(Template,
                                          null=True)
    special_abilities = models.ManyToManyField(SpecialAbilities)
    skills = models.ManyToManyField(Skills)
    language = models.CharField(max_length=100,
                                default='Common')
    spells = models.ManyToManyField(Spells)
    environment = models.TextField(null=True)
    organization = models.TextField(null=True)
    # Need 'Resistance', 'Weaknesses', 'Spell Resistance (SR)', and a way to do Spell-like abilities.

    def calculate(self):
        if self.array():
            self.eac = self.array.eac
            self.kac = self.array.kac
            self.fortitude = self.array.fort
            self.reflex = self.array.ref
            self.will = self.array.will
            self.hp = self.array.hp
            self.ability_dc = self.array.ability_dc
            self.base_spell_dc = self.array.base_spell_dc
            self.strength = 0
            self.dexterity = 0
            self.constitution = 0
            self.intelligence = 0
            self.wisdom = 0
            self.charisma = 0
            if self.high_ability == 'STR':
                self.strength += self.array.high_ability_mod
            elif self.high_ability == 'DEX':
                self.dexterity += self.array.high_ability_mod
            elif self.high_ability == 'CON':
                self.constitution += self.array.high_ability_mod
            elif self.high_ability == 'INT':
                self.intelligence += self.array.high_ability_mod
            elif self.high_ability == 'WIS':
                self.wisdom += self.array.high_ability_mod
            elif self.high_ability == 'CHA':
                self.charisma += self.array.high_ability_mod
            if self.med_ability == 'STR':
                self.strength += self.array.med_ability_mod
            elif self.med_ability == 'DEX':
                self.dexterity += self.array.med_ability_mod
            elif self.med_ability == 'CON':
                self.constitution += self.array.med_ability_mod
            elif self.med_ability == 'INT':
                self.intelligence += self.array.med_ability_mod
            elif self.med_ability == 'WIS':
                self.wisdom += self.array.med_ability_mod
            elif self.med_ability == 'CHA':
                self.charisma += self.array.med_ability_mod
            if self.low_ability == 'STR':
                self.strength += self.array.low_ability_mod
            elif self.low_ability == 'DEX':
                self.dexterity += self.array.low_ability_mod
            elif self.low_ability == 'CON':
                self.constitution += self.array.low_ability_mod
            elif self.low_ability == 'INT':
                self.intelligence += self.array.low_ability_mod
            elif self.low_ability == 'WIS':
                self.wisdom += self.array.low_ability_mod
            elif self.low_ability == 'CHA':
                self.charisma += self.array.low_ability_mod
