# buffs / debuffs and duration of effects

debuffs = {
        'over_weight' : {
            'stat_penalty' : 0.6, # Reduce 60% of AGI
            'icon' : '⚖️', 
            'type' : 'physical'
        },
        
        'stunned' : {
            'turns_left' : 2 ,
            'dmg_penalty' : 2, # Double Damage
            'icon' : '💫', 
            'type' : 'physical'
        },
        
        'fracture' : {
            'turns_left' : 3,
            'dmg_penalty' : 0.3, # +30% Damage Taken
            'icon' : '🦴', 
            'type' : 'physical'
        },
        
        'bleeding' : {
            'turns_left' : 3 ,
            'dmg' : 3 ,
            'agi_penalty' : 0.1, # Reduce 10% of AGI
            'icon' : '🩸', 
            'type' : 'physical'
        },
        
        'poison' : {
            'turns_left' : 4 ,
            'dmg' : 1 ,
            'icon' : '', 
            'type' : 'physical'
        },
        
        'blindness' : {
            'turns_left' : 2 ,
            'dmg' : 1 ,
            'stat_penalty' : 0,
            'icon' : '🕶️', 
            'type' : 'physical'
        },
        
        'freeze' : {
            'turns_left' : 2 ,
            'dmg' : 3 ,
            'agi_penalty' : 0.8, # Reduce 80% of AGI
            'icon' : '❄️', 
            'type' : 'magical'
        },
        
        'burning' : {
            'turns_left' : 2 ,
            'dmg' : 4 ,
            'agi_penalty' : 0.2, # Reduce 20% of AGI
            'icon' : '🔥', 
            'type' : 'magical'
        },
        
        'burning_Magic' : {
            'magic_reduction' : 0.3, # Reduces 30% magic of opponent
            'icon' : '🕯️', 
            'type' : 'magical'
        },
        
        'electrified' : {
            'turns_left' : 2 ,
            'dmg' : 5 ,
            'dmg_penalty' : 2, # Double damage if opponent water type
            'icon' : '⚡', 
            'type' : 'magical'
        },
        
        'paralysis' : {
            'turns_left' : 2 ,
            'paralyzed' : True,
            'icon' : '⛓️', 
            'type' : 'magical'
        },
        
        'craziness' : {
            'turns_left' : 2 ,
            'dmg' : 3 ,
            'random_target' : True, # Attack any opponent
            'icon' : '🌀', 
            'type' : 'magical'
        },
           
           }

buffs = {
    
    'fury' : {
            'turns_left' : 2 ,
            'stat_penalty' : 2, # Double damage
            'icon' : '💥', 
            'type' : 'physical'
        },
    
    'inspiration' : {
            'turns_left' : 2 ,
            'extra_attack' : 1 , # Double attack in a turn
            'icon' : '✨', 
            'type' : 'physical'
        },
    
    'resistance' : {
            'turns_left' : 2 ,
            'dmg_resistance' : 0.6, # 60% resistance in a target
            'icon' : '🛡︎', 
            'type' : 'physical'
        },
    
    'iron-skin' : {
            'turns_left' : 2 ,
            'def' : 0.9 , # 90% Bonus defense
            'agi_reduce' : 0.3, # 30% less agility 
            'icon' : '🛡️', 
            'type' : 'physical'
        },
    
    'regeneration' : {
            'turns_left' : 3 ,
            'hp' : 0.3 , # hp regeneration per Turn
            'icon' : '❤️', 
            'type' : 'physical'
        },
    
    'revenge' : {
            'turns_left' : 3 ,
            'dmg_bonus' : 0.4 , # 40% More damage effect
            'icon' : '⚔️ ', 
            'type' : 'physical'
        },
    
    'vampirism' : {
            'turns_left' : 2 ,
            'dmg_bonus' : 0.05 , # 5% Bonus Damage
            'hp' : 0.1 , # 10% taken hp converted of damage on a enemy
            'icon' : '🧛', 
            'type' : 'physical'
        },
    
    'chain' : {
            'turns_left' : 2 ,
            'agi_reduced' : 0.5, # Reduce 50% of AGI
            'icon' : '🔗', 
            'type' : 'physical'
        },
    
    'last-effort' : {
            'turns_left' : 2 , # Then effect comes at a 0 , the person dies.
            'dmg_bonus' : 2 , # Double damage
            'die' : False,
            'icon' : '❤️', 
            'type' : 'physical'
        },
    
    'letal-focus' : {
            'turns_left' : 2 ,
            'dmg_bonus' : 1.5 , # 150% damage bônus
            'sort' : 1, # Incrase 1 point in sort, incrase chance of critical
            'icon' : '🎯', 
            'type' : 'physical'
        },
    
    'frenesi' : {
            'turns_left' : 2 ,
            'dmg_bonus' : 1.8 , # 180 % damage bônus
            'stamina_bonus' : 3, # Bonus Stamina
            'icon' : '💥', 
            'type' : 'physical'
        },
    
    'involuntary-reflex' : {
            'turns_left' : 1,
            'dmg_bonus' : 1.5, # 150% counter attack dmg on a enemy
            'icon' : '⚡', 
            'type' : 'physical'
        },
       
    'second-chance' : {
            'turns_left' : 1,
            'hp' : 1 , # Chance surviving a deathly damage
            'icon' : '⚖️', 
            'type' : 'physical'
        },
    
    'intimidation' : {
            'turns_left' : 2 ,
            'dmg_reduction' : 0.2 , # Incrase 20% chance to dodge
            'fear' : 0.1, # 10% to apply fear a enemy
            'icon' : '😨', 
            'type' : 'mental'
        },
    
}
