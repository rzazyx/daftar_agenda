import PySimpleGUI as pg
import os
import fungsi_agenda

if os.path.exists('agenda.txt'):
    agendaku = fungsi_agenda.membuka_agenda()
else:
    fungsi_agenda.membuat_agenda()
    agendaku = fungsi_agenda.membuka_agenda()

agendaku = ["makan","tidur"]

#element
label_input = pg.Text("Masukkan agenda baru: ")
label_daftar = pg.Text("Daftar Agendaku: ")
box_input = pg.InputText(key="key_box_input", size=(40,1))
tombol_tambah = pg.Button("Tambah", key="key_tambah")
tombol_hapus = pg.Button("Hapus", key="key_hapus")
tombol_keluar = pg.Button("Keluar", key="key_keluar")
daftar_agenda = pg.Listbox(values=agendaku, key="key_daftar_agenda", size=(60,10))

#window
window= pg.Window("DAFTAR AGENDAKU",
                  layout=[[label_input],[box_input, tombol_tambah, tombol_hapus, tombol_keluar],[label_daftar],
                          [label_daftar],[daftar_agenda]],
                  size=(1000,600),
                  font=("Helvetica", 20))

while True:
    event, data = window.read()
    print(event)
    print(data)


    match event:
        case "key_tambah":
            #menambahkan data
            agenda_baru = data["key_box_input"]
            agendaku.append(agenda_baru + '\n')
            window['key_daftar_agenda'].update(values=agendaku)
        case "key_hapus":
            #menghapus data
            agenda_dihapus = data["key_daftar_agenda"][0]
            agendaku.remove(agenda_dihapus)

        case "key_keluar":
            #keluar
            fungsi_agenda.menyimpan_agenda(agendaku=agendaku)
            break
        case pg.WINDOW_CLOSED:
            fungsi_agenda.menyimpan_agenda(agendaku=agendaku)
            break


window.close()