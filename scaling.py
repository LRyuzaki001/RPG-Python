
from character.ficha import (base_value,
                             character,
                             race,
                             class_char)
from equipment.equipment import (hand_equipment,
                                 chest_equip,
                                 arm_equipment,
                                 hand_equipment,
                                 waist_equipment,
                                 leg_equipment,
                                 foot_equipment,
                                 bonus_equipment)
from magic.magic import (light_magic,
                         dark_magic,
                         enchantment,
                         curse)
from weapons.weapon import weapon
from effects.effects import debuffs,buffs
from potion.potion import potion,throw_potion

# Select the initial attributes'

print('Welcome to the character creation.')
character_name = str(input('Write your character name: '))
character_class = str(input('Write your character class: '))
character_race = str(input('Select your character race: '))

# Putting the character characteristics in a dictionary

character['name'] = character_name
character['class'] = character_class
character['race'] = character_race

# 1-st Scaling of character, race, and class selected.

base_character = {
    'character' : character}

# multiplier atribute base

multiplier_mana = character['attribute_base']['mana'] * race ['elf']['mana_mult']

print (multiplier_mana)

# 2-nd Scaling based in total of 1-st scaling and equipment, magic, weapons, buffs and debuffs.

