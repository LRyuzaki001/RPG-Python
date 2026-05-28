potion = {
    
    # minor potions
    
    'minor_cure_potion' : {
        'hp': {
            'hp_percent' : 20
            },
        'wheight' : 0.2,
        
    },
    'minor_mana_potion' : {
        'mana': {
            'mana_percent': 40
            },
        'wheight' : 0.2,
        
    },
    'minor_poison_potion' : {
        'hp': 10,
        'wheight' : 0.2,
        
    },
    
    # medium Potion
    
    'medium_cure_potion' : {
        'hp': {
            'hp_percent' : 40
            },
        'wheight' : 0.4,
        
    },
    'medium_mana_potion' : {
        'mana': {
            'mana_percent': 40
            },
        'wheight' : 0.4,
        
    },
    
    'medium_poison_potion' : {
        'hp': 30,
        'wheight' : 0.4,
        
    },
    
    
    # large potion
    
    'large_cure_potion' : {
        'hp': {
            'hp_percent' : 70
            },
        'wheight' : 0.8,
        
    },
    'large_mana_potion' : {
        'mana': {
            'mana_percent': 70
            },
        'wheight' : 0.8,
        
    },
    'large_poison_potion' : {
        'dps': 40,
        'wheight' : 0.8,
        
    },
    
    
    
}

throw_potion = {
    
    'poison_bottle' : {
        'throwable' : True,
        'dmg_perturn' : 5,
        'effect' : 'poisoned',
        'wheight' : 0.5,
    },
    
    'ice_bottle' : {
        'throwable' : True,
        'dmg_perturn' : 3,
        'effect' : 'freeze',
        'wheight' : 0.5,
    },
    
        'fire_bottle' : {
        'throwable' : True,
        'dmg_perturn' : 3,
        'effect' : 'burning',
        'wheight' : 0.5,
    },
    
        'water_bottle' : {
        'throwable' : True,
        'effect' : {
            'status':'wet',
            'chanc_electrified' : 1.3,
            'chanc_freeze' : 1.3,        
                    },
        'wheight' : 0.5,
    },
        
        'oil_bottle' : {
        'throwable' : True,
        'incrase_chance_effect' : 'burning',
        'effect' : {
            'status':'oily',
            'chanc_burning' : 1.3        
                    },
        'wheight' : 0.5,
    },
}
