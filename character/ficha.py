#base status
base_value = 10

#Character base atribute

character = {
    'name':'',
    'class': '',
    'level' : '',
    'xp' : {
        'total' : 100
        },
    'status' : {
        'normal' : True,
        'mana' : True,
        'stamina' : True,
        'weight' : 0,
        'bledding' : 0,
        'poison' : 0,
        'freeze' : 0,
        'burning' : 0,
        'blindness' : 0,
        'paralysis' : 0,
        'craziness' : 0,
        'silence' : False,
        'death' : False,
        'over_weight' : True,
        },
    
    'atribute_base': {
        'hp' : base_value,
        'mana' : base_value,
        'stamina' : base_value,
        'for' : base_value,
        'res' : base_value,
        'agi' : base_value,
        'sort' : base_value,
        'weight' : base_value,
        'dmg_base' : base_value,
        'slot_magic' : 3,
    },
    
    'inventory' : {
        'itens':[],
        'bag_coin' : 0,
    },
    
    'equipment' : {
        'head' : [],
        'chest' : [],
        'arm' : [],
        'hand' : [],
        'waist' : [],
        'leg' : [],
        'foot' : [],
    },
    
    'Weapon' : {
        'L_hand':None,
        'R_hand':None,
    },
    
    'final_status':{
        'total_hp' : 0,
        'total_mana' : 0,
        'total_stamina' : 0,
        'total_for' : 0,
        'total_res' : 0,
        'total_agi' : 0,
        'total_sort' : 0,
        'total_weight' : 0,
        'total_dmg' : 0,
        'total_slot_magic' : 0,
        'type_dmg' : []
    },
    
     'current_status':{
        'total_hp' : 0,
        'total_mana' : 0,
        'total_stamina' : 0,
        'total_for' : 0,
        'total_res' : 0,
        'total_agi' : 0,
        'total_sort' : 0,
        'total_weight' : 0,
        'total_dmg' : 0,
        'total_slot_magic' : 0,
        'type_dmg' : []
    },
    
}

# Race of Character

race = {
    'elf' : {
        'mana_mult' : 1.3,
        'buff' : 1,
        'slot_magic' : 1,
        'magic_resist' : 2,
        },
    
    'dark-elf' : {
        'mana_mult' : 1.3,
        'debuff' : 1,
        'slot_magic' : 1,
        'magic_resist' : 2,
        },
    
    'orc' : {
        'for' : 3,
        'hp' : 1.5,
        'res' : 3,
        'bledding_resistance' : 3,
        },
    
    'human' : {
        'exp_bonus_mult' : 1.15, 
        'sort' : 3, 
        },
    
    'dragonborn' : {
        'def_mult' : 1.15, 
        'for_mult' : 1.15, 
        'fire_resistance' : 4,
        },
    
    'undead' : {
        
        # Unical effects
        'poison_effect' : 'convert in hp',
        'poison_Negate' : True,
        'hp_Regen' : 2, # Per turn
        
        # Debuffs
        'cure' : 'dmg',
        'fire_dmg_mult' : 2, 
        'agi' : -2,
        'for' : -1,
        },
    
    # Enemy only
    
    'dragon' : {
        #Elemental type
        'type' : ['fire', 'ice', 'blood', 'thunder', 'poison', 'curse'],
        # Unical effects
        'fire_immunity' : False,
        'ice_immunity' : False,
        'bledding_immunity' : False,
        'thunder_immunity' : False,
        'poison_immunity' : False,
        'curse_immunity' : False,
        
        },
    
    
    
    'thiefling' :{
        
        # Buff
        'fire_resistance' : 2,
        'charisma_mult' : 2,
        'stealth_bonus' : 2,
        
        # Debuff
        'holy_dmg_mult' : 1.5 
        },
    
    'dwarf' : {
        'res' : 4,                 
        'hp_mult' : 1.2,
        'poison_resistance' : 5,   
        'stun_resist' : 1,         
        },
    
}

# Class of Character

class_char = {
    
    'paladin' : {
        'unique_skills' : {
            'holy_smite': 'convert damage physical in Holy',
            'divine_shield': 'temporary immunity'
        },

         'class_bonus' : {
            'resist_holy': 0.50,  
            'armor_bonus': 1.2,   
            'heal_efficiency': 1.15 
         }
    }, #Affinity with sword, hammer and holy damage
    
    'druid' : {
        'unique_skills' : {
            'wolf_transformation': {'atk_speed': 1.5, 'dodge': 0.2},
            'bear_transformation': {'hp_multi': 2.0, 'resist_phys': 0.3},
            'pangolim_transformation': {'resist_all': 0.4, 'thorns': 5},
        },

        'class_bonus' : {
            'mana_Regen': 0.1,
            'nature_affinity': 1.1 

        }
    },  # Hability to transform in animals
    
    'mage' : {
        'unique_skills' : {
            'mana_Burn': 'damage based in mana of oponnent',
            'teleport': 'dodge garanted per 1 turn'
        },

        'class_bonus' : {
            'slot_magic': 5,
            'mana_multi': 1.3,
            'magical_penetration': 0.15

        }
    }, # High Damage Magic and low hp 
    
    'barbarian' : {
        'unique_skills' : {
           'enrage': 'incrase physical damage but decrease defense',
            'leap_slam': 'area physical damage'
        },

        'class_bonus' : {
            'hp_flat': 50,       # Bônus fixo de vida
            'physical_multi': 1.25,
            'resistance_stun': 0.3

        }
    }, # High Damage Physical and Medium resistance
    
    'necromancer' : {
        'unique_skills' : {
            'raise_undead': 'summon skeleton based on int',
            'soul_siphon': 'curses damage cure the conjurator'
        },

        'class_bonus' : {
           'curse_duration': 2, # Efeitos duram mais turnos
            'resist_cursed': 0.4,
            'minion_damage': 1.2

        }
    },
     # Hability to summoner a pawn (undead), based in char atribute
    
    'monk' : {
        'unique_skills' : {
           'seven_sided_strike': 'multiple Fast Attacks',
            'meditate': 'rechafully hp and stamina'
        },

        'class_bonus' : {
            'unarmed_multi': 1.5, # Bônus alto para luta sem armas
            'evasion': 0.25,      # Chance de desviar de ataques
            'attack_speed': 1.3

        }
    },
     # High base Damage(Disarm or glooves equip) and medium resistance
    
    'archer' : {
        'unique_skills' : {
            'rain_of_arrows': 'area physical damage',
            '   eagle_eye': 'incrase precision and crit'
        },

        'class_bonus' : {
            'crit_Chance': 0.2,
            'crit_Damage': 1.5,
            'range_Bonus': 10

        }
    },
     # High Chanc of critical Damage and agi , possibility to aplly effects in arrows, but low hp and res
     
}
