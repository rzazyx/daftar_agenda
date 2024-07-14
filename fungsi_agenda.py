def membuka_agenda(filepath= 'agenda.txt'):
    with open(filepath, mode='r') as file:
        agendaku = file.readlines()
    return agendaku

def membuat_agenda(filepath = 'agenda.txt'):
    with open(filepath, mode='w') as file:
        file.writelines([])

def menyimpan_agenda(filepath = 'agenda.txt', agendaku= []):
    with open('agenda.txt', mode='w') as file:
        file.writelines(agendaku)
