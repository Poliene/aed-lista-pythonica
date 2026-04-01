# src/exercicio_11.py

def modify_guest_list(guests, old_guest, new_guest):
    new_list = guests.copy()
    
    if old_guest in new_list:
        index = new_list.index(old_guest)
        new_list[index] = new_guest
    
    return new_list