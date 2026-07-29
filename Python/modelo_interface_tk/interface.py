#This model is example my habilities to create ui for using tkinter

from tkinter import *


class InterfaceTk:
    def __init__(self):
        self.tela = Tk()
        self.tela.title('Example Program')
        self.tela.wm_iconbitmap('icone.ico')
        self.tela.geometry('600x500')
        self.labels = {}
        self.entrys = {}
        self.buttons = {}
        self.widgets = {'labels': self.labels,
                        'entrys': self.entrys,
                        'buttons': self.buttons}
        self.frames = {}
        self.config()

    def start(self):
        self.tela.mainloop()

    def config(self):
        ##frames

        #main frame = all screen
        self.frames['main_frame'] = Frame(master=self.tela)
        self.frames['main_frame'].pack(fill='both', expand=True)
        #

        #header frame
        self.frames['header_frame'] = Frame(master=self.frames['main_frame'], pady=20)
        self.frames['header_frame'].pack(fill='x')
        #

        #body frame
        self.frames['body_frame'] = Frame(master=self.frames['main_frame'])
        self.frames['body_frame'].pack(fill='x', anchor='w', padx=40)
        #

        #lines body frame
        self.frames['body_frame_l1'] = Frame(master=self.frames['body_frame'])
        self.frames['body_frame_l1'].pack(anchor='w')

        self.frames['body_frame_l2'] = Frame(master=self.frames['body_frame'])
        self.frames['body_frame_l2'].pack(anchor='w')

        self.frames['body_frame_l3'] = Frame(master=self.frames['body_frame'], pady=20)
        self.frames['body_frame_l3'].pack(anchor='w')

        self.frames['body_frame_l4'] = Frame(master=self.frames['body_frame'])
        self.frames['body_frame_l4'].pack(anchor='w')

        self.frames['body_frame_l5'] = Frame(master=self.frames['body_frame'], pady=20)
        self.frames['body_frame_l5'].pack(anchor='center')  # <-- botão centralizado
        #

        #baseboard frame
        self.frames['baseboard_frame'] = Frame(master=self.frames['main_frame'])
        self.frames['baseboard_frame'].pack(side=BOTTOM, fill='x')
        ##

        ###Other Widgets

        #label header
        self.labels['header'] = Label(
            master=self.frames['header_frame'],
            text='Example Program',
            font=('Times New Roman', 32, 'bold'),
            fg='blue'
        )
        self.labels['header'].pack(anchor='center')
        #

        ##Widgets body lines

        #title forms (label)
        self.labels['title_forms'] = Label(
            master=self.frames['body_frame_l1'],
            text='Registration',
            font=('Calibri', 16, 'italic', 'underline', 'bold'),
            fg='red'
        )
        self.labels['title_forms'].pack(anchor='w')
        #

        #name (label)
        self.labels['name'] = Label(
            master=self.frames['body_frame_l2'],
            text='Name:',
            font=('Calibri', 14, 'bold'),
            padx=5
        )
        self.labels['name'].pack(side=LEFT)
        #
        #name (entry)
        self.entrys['name'] = Entry(master=self.frames['body_frame_l2'], font=('Calibri', 14), width=40)
        self.entrys['name'].pack(side=LEFT)
        #

        #lastname (label)
        self.labels['lastname'] = Label(
            master=self.frames['body_frame_l3'],
            text='Lastname:',
            font=('Calibri', 14, 'bold'),
            padx=5
        )
        self.labels['lastname'].pack(side=LEFT)
        #
        #lastname (entry)
        self.entrys['lastname'] = Entry(master=self.frames['body_frame_l3'], font=('Calibri', 14), width=37)
        self.entrys['lastname'].pack(side=LEFT)
        #

        #email (label)
        self.labels['email'] = Label(
            master=self.frames['body_frame_l4'],
            text='E-mail:',
            font=('Calibri', 14, 'bold'),
            padx=5
        )
        self.labels['email'].pack(side=LEFT)
        #
        # email (entry)
        self.entrys['email'] = Entry(master=self.frames['body_frame_l4'], font=('Calibri', 14), width=40)
        self.entrys['email'].pack(side=LEFT)
        #

        #submit (button)
        self.buttons['submit'] = Button(
            master=self.frames['body_frame_l5'],
            text='Submit',
            font=('Arial', 16, 'bold'),
            bg='orange'
        )
        self.buttons['submit'].pack(anchor='center')
        #
        ##

        #baseboard (label)
        self.labels['baseboard'] = Label(master=self.frames['baseboard_frame'], text='Baseboard default, planning for programmer...',
                                         font=('Verdana', '10', 'italic'), pady=10)
        self.labels['baseboard'].pack()
        #
        ###
