# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-01 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatureCreator', '0007_auto_20180331_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('damage', models.CharField(max_length=20)),
                ('add_damage', models.IntegerField()),
                ('damage_type', models.CharField(max_length=20)),
                ('mod', models.IntegerField()),
                ('critical', models.CharField(max_length=20)),
                ('three_attack', models.BooleanField(default=False)),
                ('four_attack', models.BooleanField(default=False)),
                ('against_eac', models.BooleanField(default=False)),
                ('attack_type', models.CharField(choices=[('M', 'Melee'), ('R', 'Ranged')], max_length=1)),
                ('additional_info', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Immunities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Speed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('distance', models.IntegerField(default=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='array',
            name='ability_score_modifiers',
        ),
        migrations.RemoveField(
            model_name='creature',
            name='aura',
        ),
        migrations.RemoveField(
            model_name='creature',
            name='melee_attack',
        ),
        migrations.RemoveField(
            model_name='creature',
            name='ranged_attack',
        ),
        migrations.RemoveField(
            model_name='creature',
            name='senses',
        ),
        migrations.AddField(
            model_name='array',
            name='high_ability_mod',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='array',
            name='low_ability_mod',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='array',
            name='med_ability_mod',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creature',
            name='environment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='creature',
            name='high_ability',
            field=models.CharField(choices=[('STR', 'Strength'), ('DEX', 'Dexterity'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Wisdom'), ('CHA', 'Charisma')], default=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='creature',
            name='language',
            field=models.CharField(default='Common', max_length=100),
        ),
        migrations.AddField(
            model_name='creature',
            name='low_ability',
            field=models.CharField(choices=[('STR', 'Strength'), ('DEX', 'Dexterity'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Wisdom'), ('CHA', 'Charisma')], default=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='creature',
            name='med_ability',
            field=models.CharField(choices=[('STR', 'Strength'), ('DEX', 'Dexterity'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Wisdom'), ('CHA', 'Charisma')], default=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='creature',
            name='organization',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='creature',
            name='reach',
            field=models.CharField(default=5, max_length=5),
        ),
        migrations.AddField(
            model_name='creature',
            name='space',
            field=models.CharField(default=5, max_length=5),
        ),
        migrations.AddField(
            model_name='creature',
            name='speed',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_modifier',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='specialabilities',
            name='ability_range',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='specialabilities',
            name='ability_type',
            field=models.CharField(choices=[('ARA', 'Aura'), ('OFF', 'Offensive Ability'), ('DEF', 'Defensive Ability'), ('SNS', 'Sense'), ('IMM', 'Immunities'), ('OTH', 'Other')], default=None, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialabilities',
            name='origin',
            field=models.CharField(choices=[('EX', 'Ex'), ('SU', 'Su'), ('SP', 'Sp')], default=None, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialabilities',
            name='subtype',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='creature',
            name='constitution',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='creature',
            name='dexterity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='creature',
            name='intelligence',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='creature',
            name='strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='creature',
            name='wisdom',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='specialabilities',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='creature',
            name='attack',
            field=models.ManyToManyField(null=True, to='creatureCreator.Attack'),
        ),
        migrations.AddField(
            model_name='creature',
            name='special_movement',
            field=models.ManyToManyField(null=True, to='creatureCreator.Speed'),
        ),
    ]
