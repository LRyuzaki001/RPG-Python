# Light magics , used for healing or suport.

light_magic = {
    'cure' : 5, # Basic Cure
    'cure+' : 10, # Cure Advanced
    'revive' : 'off', # Revive a member of party
    'remove-status' : 0, # Remove debuff
    'motivation' : 2, # Incrase AGI
    'motivation+' : 5, # Incrase uses of magic in turn or times to attack
    'resistance' : 8, # Incrase RES on a member
    'resistance+' : 15, # Incrase a Great RES on a member
}

# Dark magic, used for causes damage on a enemy

dark_magic = {
    'fireball' : {
      'dmg' : 7,
      'chance_apply_effect' : 'Burning',
    },
    
    'fire-beam' : {
        'dmg' : 5,
        'dmg_perTurn' : 3,
        'turns' : 2,
        'chance_apply_effect' : 'Burning',
        },
    
    'ice-stake' : {
        'dmg' : 1,
        'chanc_crit-mult' : 2
        },
    
    'ice-rain' : {
        'chanc_dmg_group' : 1,
        'chanc_dmg_perTurn' : 3,
        'chanc_effect' : 'Freeze',
        },
    
    'ice-sphere' : {
        'dmg' : 1,
        'chanc_effect' : 'Freeze',
        'chanc_explosion_percent' : 10,
        },
    
    'poison-mist' : {
        'dmg_perTurn' : 6,
        },
    
}

# enchantment, used in a weapon for a take a temporally boost.

enchantment = {
    'light-enchantment' : {
        'effect' : {
            'light_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'dark-enchantment' : {
        'effect' : {
            'dark_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'holy-enchantment' : {
        'effect' : {
            'holy_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'venom-enchant' : {
        'effect' : {
            'venom_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'fire-enchant' : {
        'effect' : {
            'fire_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'ice-enchant' : {
        'effect' : {
            'ice_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'lightning-enchantment' : {
        'effect' : {
            'lightning_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'blood-enchantment' : {
        'effect' : {
            'blood_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'wind-enchantment' : {
        'effect' : {
            'wind_percent_dmg' : 35,
            'turns_left' : 5,
            'stack_effect' : 10,
        },
    },
    
    'seal' : {
        'effect' : {
            'silence' : True,
        }
    },
    
}

# Cursed, used for cause a temporally negative substatus in a opponent.

curse = {
    'seal-dark-magic' : {
        'effect' : {
            'dmg_magic' : False,
        },
    },
    
    'Drain-HP' : {
        'effect' : {
            'HP' : -0.05, # 5% reduce HP per turn
            'turns_left' : 3,
            
        },
    },
    
    'drain-mana' : {
        'effect' : {
            'mana' : -0.15, # -15% of mana
            'turns_left' : 1,
        },
    },
    
    'blindness' : {
        'effect' : {
            
            'turns_left' : 3,
        },
    },
    
    'paralysis' : {
        'effect' : {
            'skip_turn' : True,
            'turns_left' : 3,
        },
    },
    
    'craziness' : {
        'effect' : {
            'all_targets' : True,
            'turns_left' : 4,
        },
    },
}
