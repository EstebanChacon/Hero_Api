# models.py

from django.db import models


class Superpower(models.Model):
    name = ['electrokinesis','energy_constructs','mind_control_resistance','matter_manipulation','telepathy_resistance',
    'mind_control','enhanced_hearing','dimensional_travel','element_control','size_changing','fire_resistance',
    'fire_control','dexterity','reality_warping','illusions','energy_beams','peak_human_condition','shapeshifting',
    'heat_resistance','jump','self-sustenance','energy_absorption','cold_resistance','magic','telekinesis',
    'toxin_and_disease_resistance','telepathy','regeneration','immortality','teleportation','force_fields',
    'energy_manipulation','endurance','longevity','weapon-based_powers','energy_blasts','enhanced_senses',
    'invulnerability','stealth','marksmanship','flight','accelerated_healing','weapons_master','intelligence',
    'reflexes','super_speed','durability','stamina','agility','super_strength']
    def __str__(self):
        return str(self.name)

class Publisher(models.Model):

    name = models.CharField(max_length=80)
    def __str__(self):
        return str(self.name)

class Hero(models.Model):
    name = models.CharField(max_length=80)
    alias = models.CharField(max_length=80)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default = None)
    superpowers = models.ManyToManyField(Superpower)
    def __str__(self):
        return str(self.name)
