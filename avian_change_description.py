# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:10:40 2018

@author: wteal
"""

from avian_edit_api import load_page, change_description, save, login

ids_to_update = []

def change_text(string_, old_text, new_text):
    return string_.replace(old_text, new_text, 1)
    

def make_the_changes(ids_to_update):
    old_text = ''
    new_text = ''
    for id_ in ids_to_update:
        load_page('edit', id_)
        save_elem = change_description(change_text, old_text, new_text)

        save(save_elem)