# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:10:40 2018

@author: wteal
"""

from avian_edit_api import load_page, change_description, delete_genre, save, login

ids_to_update = []
 
def make_the_changes(ids_to_update):
    for id_ in ids_to_update:
        load_page('edit', id_)
        save_elem = delete_genre('')

        save(save_elem)