# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:14:27 2018

@author: wteal
"""

from avian_pseudo_api import load_page, save, login, #Insert the functions you need here

ids_to_update = []


def make_the_changes(ids_to_update):
    for i in ids_to_update:
        load_page('edit', i)
        # Insert fuctions to run. 
        
        # Set the DOM element returned by the last-run function as save_elem
        save_elem = 
        
        # Save the document.
        save(save_elem)