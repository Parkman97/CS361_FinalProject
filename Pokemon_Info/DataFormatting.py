import os

def dataFormatting(type, data, pokemonName=None):

    if type == 'name':

        print(f"Pokemon Name        | {pokemonName}")
        print('--------------------------------------------------------------------')
        for key, value in data.items():
            if key not in  ['sprite', 'height', 'base_happiness']:
                if isinstance(value, dict):
                    print(f"{key.capitalize():<19} |")
                    for sub_key, sub_value in value.items():
                        print(f"{'':<19} | {sub_key}: {sub_value}")
                elif isinstance(value, list):
                    print(f"{key.capitalize():<19} | {', '.join(value)}")
                else:
                    print(f"{key.capitalize():<19} | {value}")
                print('--------------------------------------------------------------------')

    else:
        print('\n')
        print('\n')
        print("|Type      |ID  |Pokemon                  |Moves                    |Half Damage From         |Half Damage To           |Double Damage To         |Double Damage From       ")
        print("|----------|----|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------")

        num_fields = 0
        for key in data:
            if isinstance(data[key], (dict, list)):
                if len(data[key]) > num_fields:
                    num_fields = len(data[key])

        i = 0
        while i < num_fields:
            if i == 0:
                id = str(data['id'])
                len_id = len(id)
                id_diff = (2 - len_id) * " "
                id = id + id_diff

                name = data['name']
                len_name = len(name)
                name_diff = (8 - len_name) * " "
                name = name + name_diff
            else:
                 id = "  "
                 name = "        "

            if i < len(data['damage_relations']['double_damage_from']):
                double_damage_from = data['damage_relations']['double_damage_from'][i]  
            else: 
                double_damage_from = ''
            
            if i < len(data['damage_relations']['double_damage_to']):
                 double_damage_to = data['damage_relations']['double_damage_to'][i]  
            else: 
                 double_damage_to = ''
            
            if i < len(data['damage_relations']['half_damage_from']):
                 half_damage_from = data['damage_relations']['half_damage_from'][i]  
            else: 
                 half_damage_from = ''

            if i < len(data['damage_relations']['half_damage_to']):
                half_damage_to = data['damage_relations']['half_damage_to'][i]  
            else: 
                half_damage_to = ''

            if i < len(data['moves']):
                moves = data['moves'][i]  
            else: 
                moves = ''
            
            if i < len(data['pokemon']):
                pokemon = data['pokemon'][i]  
            else: 
                pokemon = ''

            print(f"| {name} | {id} | {pokemon:<23} | {moves:<23} | {half_damage_from:<23} | {half_damage_to:<23} | {double_damage_to:<23} | {double_damage_from} ")

            i += 1