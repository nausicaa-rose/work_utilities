# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:56:43 2018

@author: wteal
"""

from avian_edit_api import driver, load_page, add_creator, save, delete_contributor

def add_new_creator_delete_people_org():
    ids_to_update = []
    
    for id_ in ids_to_update:
        load_page('edit', id_)
        add_creator('')
        e = delete_contributor('')
        save(e)
        
