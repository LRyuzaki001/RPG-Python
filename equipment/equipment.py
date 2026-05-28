# Equipments
# def = defense
# agi = agility
# res = resistance
# sort = Luck / critical chance
# weight = weight of equipment 
# The logical system is present in description.md file
# def: leather = 1x , _= 1.5x , steel 2x.
# Debuff: leather = less def , _= def is based on res , STELL = less durability


head_equip = {
    'leather_elm' : {
        'def' : 4,
        'agi' : 7,
        'res' : 2,
        'sort' : 0.05, # 5% Bonus sort
        'weight' : 5,
        'durability' : 150 , 
        'type' : 'leather',
    },
    'iron_elm' : {
        'def' : 7,
        'agi' : 1,
        'res' : 5,
        'weight' : 15,
        'durability' : 500 ,
        'type' : 'iron',
    },
    'steel_elm' :{
        'def' : 8,
        'agi' : -0.02, # 2% reduce agi
        'res' : 3,
        'sort' : -0.01, # - 1% sort
        'weight' : 10,
        'durability' : 300 ,
        'type' : 'steel'
    },
    'Hood' :{
        'def' : 5,
        'agi' : 1,
        'res' : 1,
        'sort' : 0,
        'weight' : 1,
    },
    'Mask' :{
        'def' : 1,
        'agi' : 15,
        'weight' : 1,
    },
    'Hat' :{
        'def' : 5,
        'agi' : 1,
        'res' : 1,
        'sort' : 0,
        'weight' : 1,
    },
    
}

chest_equip = {
    'leather_chest' :{
        'def' : 5,
        'agi' : 7,
        'res' : 1,
        'sort' : 0.05, # 5% Bonus sort  
        'weight' : 10,
        'durability' : 150 ,
        'type' : 'leather',
    },
    'iron_chest' :{
        'def' : 5,
        'agi' : 2,
        'res' : 15,
        'weight' : 30,
        'durability' : 500 ,
        'type' : 'iron',
    },
    'steel_chest' :{
        'def' : 5,
        'agi' : -0.02, # 2% reduce agi
        'res' : 1,
        'sort' : -0.01, # - 1% sort
        'weight' : 20,
        'durability' : 300 ,
        'type' : 'steel'
    },
    'Shirt' :{
        'def' : 1,
        'agi' : 5,
        'res' : 3,
        'weight' : 1,
        'durability' : 50,
    },
    
    'leather Jacket' :{
        'def' : 2,
        'agi' : 3,
        'res' : 2,
        'weight' : 3,
        'durability' : 100 ,
        'type' : 'leather',
    },
    
    'Mesh_armor' : {
    'def' : 5,
    'agi' : 1,
    'res' : 1,
    'sort' : 0,
    'weight' : 8,
    }
     
}

arm_equipment = {
    'leather_arm' :{
        'def' : 5,
        'agi' : 7,
        'res' : 1,
        'sort' : 0.05, # 5% Bonus sort  
        'weight' : 5,
        'durability' : 150 ,
        'type' : 'leather',
    },
    'iron_arm' :{
        'def' : 5,
        'agi' : 1,
        'res' : 1,
        'weight' : 15,
        'durability' : 500 ,
        'type' : 'iron',
    },
    'steel_arm' :{
        'def' : 5,
        'agi' : -0.02, # 2% reduce agi
        'res' : 1,
        'sort' : -0.01, # - 1% sort
        'weight' : 10,
        'durability' : 300 ,
        'type' : 'steel'
    },
    'Bracelet' :{
        'def' : 5,
        'agi' : 1,
        'res' : 1,
        'Mana' : 0.15, # Bonus 15% mana 
        'weight' : 1,
    },
}

hand_equipment = {
    'leather_glooves' :{
        'def' : 5,
        'agi' : 7,
        'res' : 1,
        'sort' : 0.05, # 5% Bonus sort  
        'weight' : 3,
        'durability' : 150 ,
        'type' : 'leather',
    },
    'iron_glooves' :{
        'def' : 5,
        'agi' : 1,
        'res' : 1,
        'sort' : 0,
        'weight' : 9,
        'durability' : 500 ,
        'type' : 'iron',
    },
    'steel_glooves' :{
        'def' : 5,
        'agi' : 1,
        'res' : 1,
        'sort' : -0.01, # - 1% sort
        'weight' : 6,
        'durability' : 300 ,
        'type' : 'steel'
    },
}

waist_equipment = {
    'leather_waist' :{
        'def' : 5,
        'agi' : 7,
        'res' : 1,
        'sort' : 0.05, # 5% Bonus sort  
        'weight' : 5,
        'durability' : 150 ,
        'type' : 'leather',
    },
    'iron_waist' :{
        'def' : 5,
        'agi' : 1,
        'res' : 5,
        'weight' : 8,
        'durability' : 500 ,
        'type' : 'iron',
    },
    'steel_waist' :{
        'def' : 5,
        'agi' : -0.02, # 2% reduce agi
        'res' : 1,
        'sort' : -0.01, # - 1% sort
        'weight' : 7,
        'durability' : 300 ,
        'type' : 'steel'
    },
}

leg_equipment = {
    'leather_leg' :{
        'def' : 5,
        'agi' : 7,
        'res' : 1,
        'sort' : 0.05, # 5% Bonus sort  
        'weight' : 5,
        'durability' : 150 ,
        'type' : 'leather',
    },
    'iron_leg' :{
        'def' : 5,
        'agi' : 1,
        'res' : 10,
        'weight' : 15,
        'durability' : 500 ,
        'type' : 'iron',
    },
    'steel_leg' :{
        'def' : 5,
        'agi' : -0.02, # 2% reduce agi
        'res' : 1,
        'sort_Reduce' : -0.01, # - 1% sort
        'weight' : 10,
        'durability' : 300 ,
        'type' : 'steel'
    },
}

foot_equipment = {
    'leather_foot' :{
        'def' : 5,
        'agi' : 7,
        'res' : 1,
        'sort' : 0.05, # 5% Bonus sort  
        'weight' : 5,
        'durability' : 150 ,
        'type' : 'leather',
    },
    'iron_foot' :{
        'def' : 5,
        'agi' : 1,
        'res' : 8,
        'weight' : 10,
        'durability' : 500 ,
        'type' : 'iron',
    },
    'steel_foot' :{
        'def' : 5,
        'agi_Reduce' : -0.02, # 2% reduce agi
        'agi' : 1,
        'res' : 3,
        'sort' : -0.01, # - 1% sort
        'weight' : 8,
        'durability' : 300 ,
        'type' : 'steel'
    },
}

bonus_equipment = {
    
    'leather' : {'7 parts': 0.3, # 30% on total more sort and 15% more agi status (7 parts)
                 '5 parts': 0.2, # 20% Bonus - 5 parts
                 '3 parts': 0.07, # 7% Bonus - 3 parts
                 },
    
    'iron' : {'7 parts': 0.5, # 40% on total more res status (7 parts)
                 '5 parts': 0.3, # 20% Bonus - 5 parts
                 '3 parts': 0.12, # 7% Bonus - 3 parts
        },
    
    'steel' : {'7 parts': 0.5, # 200% more base defense equipment (7 parts)
                 '5 parts': 0.3, # 65% Bonus - 5 parts
                 '3 parts': 0.12, # 30% Bonus - 4 parts
        },
    
}
