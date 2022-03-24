#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'schellenberg'

import tkinter as tk
import time
import threading

from record import record


def start_recording(**kwargs):
    t = threading.Thread(target=record, kwargs=kwargs)
    t.start()


if __name__ == '__main__':
    window = tk.Tk()

    # header section
    frm_header = tk.Frame(master=window, width=500, height=15)
    header = tk.Label(master=frm_header, text='Internet radio recorder')
    header.pack()

    # input section
    frm_input = tk.Frame(master=window, width=500, height=20)

    lbl_url = tk.Label(master=frm_input, text='URL')
    ent_url = tk.Entry(master=frm_input)
    lbl_filename = tk.Label(master=frm_input, text='filename')
    ent_filename = tk.Entry(master=frm_input)
    lbl_duration = tk.Label(master=frm_input, text='duration')
    ent_duration = tk.Entry(master=frm_input, width=6)
    ent_duration.insert(0, '10')
    lbl_blocksize = tk.Label(master=frm_input, text='blocksize')
    ent_blocksize = tk.Entry(master=frm_input, width=6)
    ent_blocksize.insert(0, '1024')
    lbl_url.pack(side=tk.LEFT, pady=2)
    ent_url.pack(side=tk.LEFT, pady=2)
    lbl_filename.pack(side=tk.LEFT, pady=2)
    ent_filename.pack(side=tk.LEFT, pady=2)
    lbl_duration.pack(side=tk.LEFT, pady=2)
    ent_duration.pack(side=tk.LEFT, pady=2)
    lbl_blocksize.pack(side=tk.LEFT, pady=2)
    ent_blocksize.pack(side=tk.LEFT, pady=2)

    # button section
    frm_buttons = tk.Frame(master=window, width=500, height=20)
    url = ent_url.get()

    record_kwargs = {
        'url': ent_url.get(),
        'filename': ent_filename.get(),
        'duration': ent_duration.get(),
        'blocksize': ent_blocksize.get()
    }
    btn_record = tk.Button(master=frm_buttons, text='Record', command=lambda: start_recording(**record_kwargs))
    btn_list = tk.Button(master=frm_buttons, text='List recordings')

    btn_record.pack(side=tk.LEFT, pady=15)

    # packing frames
    frm_header.pack()
    frm_input.pack()
    frm_buttons.pack()
    window.mainloop()
