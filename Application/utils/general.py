import os

def verify_or_create_folder(folder):
    if not os.path.exists(f'output/{folder}'):
        os.makedirs(f'output/{folder}')

def complete_dictionary(dictionary, default):
    for key in default:
        if dictionary[key] == None:
            dictionary[key] = default[key]
    
    return dictionary