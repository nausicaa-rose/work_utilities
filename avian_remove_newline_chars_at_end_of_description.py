# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:52:29 2018

@author: wteal
"""

from avian_edit_api import load_page, change_description, save, login

ids_to_update = []

def remove_final_newline(text):
    return text.strip()

def make_the_changes(ids_to_update):
    for id_ in ids_to_update:
        load_page('edit', id_)
        save_elem = change_description(remove_final_newline)
        save(save_elem)