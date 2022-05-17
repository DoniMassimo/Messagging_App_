import os


def get_list_index(list, index):
    if index < len(list) and index >= 0:
        return list[index]
    else: return False
##
##### CUSTOM PRINT
def clear():  
    os.system('clear')
    
# ? funzione che permette la creazione di print personalizzati
def coustom_print(text: str, type: str, stdchar='#'):
    print()
    if type[0] == 'e':    # if equal error
        print(f'{stdchar * 2}\n{stdchar * 3} ERROR: {text}\n{stdchar * 2}')
    elif type[0] == 'w':  # warning
        print(f'{stdchar * 2} WARNING: {text}')
    elif type[0] == 'i':  # info
        stdchar = f'\n{stdchar} '
        s = stdchar.join(text.split('\n'))
        print(s)
    print()
    input()
# margin: 0 = sx, 1 = up, 2 = dx, 3 = down
# larghezza del box = lunghezza della stringa più lunga + margine sx e dx + 2
# funzione che stampa il testo in un box
def box_print(text: str, stdchar='#', **margins: int):    
    margins = list(margins['margins'])                 # trasformo margin da tuple a lista    
    for i in range(4, len(margins), -1):    # aggiungo i margini che l'utente non ha inserito
        margins.append(1)
    for i in margins:
        i = int(i)
    text = text.split('\n')
    longest_line = max(text, key=len)
    box_lenght = len(f'{stdchar}{stdchar * margins[0]}{stdchar * len(longest_line)}{stdchar * margins[2]}{stdchar}') # calcolo la larghezza del box
    print(f'{stdchar}{stdchar * margins[0]}{stdchar * len(longest_line)}{stdchar * margins[2]}{stdchar}') # stampo il margine superiorre
    for i in range(0, margins[1]): # stampo gli spazi vuoti del margine
        print(f'{stdchar}{" " * (box_lenght- 2)}{stdchar}')
    for line in text:
        print(f'{stdchar}{" " * margins[0]}{line}{" " * margins[2]}{" " * (box_lenght-len(line)-margins[0]-margins[2] - 2)}{stdchar}')
    for i in range(0, margins[1]):
        print(f'{stdchar}{" " * (box_lenght- 2)}{stdchar}')
    print(f'{stdchar}{stdchar * margins[0]}{stdchar * len(longest_line)}{stdchar * margins[2]}{stdchar}')


if __name__ == '__main__':
    pass
