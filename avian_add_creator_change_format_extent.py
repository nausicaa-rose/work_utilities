# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:45:02 2018

@author: wteal
"""
from avian_edit_api import load_page, add_creator, change_format_extent_number, save 

def add_new_creator_update_format_extent():
    ids_to_update = []

    for id_ in ids_to_update:
        load_page('edit', id_)
        add_creator('')
        save_elem = change_format_extent_number()
        save(save_elem)
    