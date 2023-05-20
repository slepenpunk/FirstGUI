from tkinter import *


class Application(Frame):
    menu = {
        'Veggie Noodles with Tofu': 30000,
        'Local Beer': 5000,
        'Veggie Beard': 10000,
        'French Fried': 20000
    }
    order_number = 0

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.menu = Application.menu
        self.keys = []

        for k in self.menu.keys():
            self.keys.append(k)

        Label(self, text='MENU\n'
                         '---------------------------------------',
              font='Arial 35',
              fg='green',
              bg='black').grid()

        self.check_btn1 = BooleanVar()
        Checkbutton(self,
                    text=f'{self.keys[0]} {self.menu.get(self.keys[0])}',
                    variable=self.check_btn1,
                    command=self.update_text,
                    font='Arial 25',
                    pady=10,
                    fg='green',
                    bg='black',
                    activebackground='black',
                    activeforeground='purple',
                    selectcolor='black'
                    ).grid(row=1, column=0, sticky=W)

        self.check_btn2 = BooleanVar()
        Checkbutton(self,
                    text=f'{self.keys[1]} {self.menu.get(self.keys[1])}',
                    variable=self.check_btn2,
                    command=self.update_text,
                    font='Arial 25',
                    fg='green',
                    bg='black',
                    activebackground='black',
                    activeforeground='purple',
                    selectcolor='black'
                    ).grid(sticky=W)

        self.check_btn3 = BooleanVar()
        Checkbutton(self,
                    text=f'{self.keys[2]} {self.menu.get(self.keys[2])}',
                    variable=self.check_btn3,
                    command=self.update_text,
                    font='Arial 25',
                    fg='green',
                    bg='black',
                    activebackground='black',
                    activeforeground='purple',
                    selectcolor='black'
                    ).grid(sticky=W)

        self.check_btn4 = BooleanVar()
        Checkbutton(self,
                    text=f'{self.keys[3]} {self.menu.get(self.keys[3])}',
                    variable=self.check_btn4,
                    command=self.update_text,
                    font='Arial 25',
                    fg='green',
                    bg='black',
                    activebackground='black',
                    activeforeground='purple',
                    selectcolor='black'
                    ).grid(sticky=W)

        Label(self, text='---------------------------------------\n'
                         'YOUR ORDER\n'
                         '↓↓↓',
              font='Arial 35',
              fg='green',
              bg='black'
              ).grid()

        self.txt = Text(self,
                        width=35,
                        height=5,
                        wrap=WORD,
                        font='Arial 25',
                        fg='green',
                        bg='black',
                        state=DISABLED,
                        )
        self.txt.grid()

        self.scroll = Scrollbar(self,
                                orient=VERTICAL,
                                command=self.txt.yview,
                                width=13
                                )
        self.scroll.grid(row=6, sticky='sne')
        self.txt.configure(yscrollcommand=self.scroll.set)

        self.order_bttn = Button(self,
                                 text='ORDER',
                                 command=self.accept_order,
                                 fg='green',
                                 bg='black',
                                 font='Arial 30',
                                 activebackground='green'
                                 )
        self.order_bttn.grid()

    def center_text(self):
        self.txt.tag_add('center', 0.0, END)
        self.txt.tag_config('center', justify=CENTER)

    def accept_order(self):
        try:
            if self.total_price > 0:
                Application.order_number += 1
                self.txt.configure(state=NORMAL)
                self.txt.delete(0.0, END)
                self.txt.insert(0.0, f'Your order number - {Application.order_number} is accepted!\n'
                                     f'{self.vars}\n'
                                     f'TO PAY - {self.total_price}VND')
                self.center_text()
                self.txt.configure(state=DISABLED)

            else:
                self.txt.configure(state=NORMAL)
                self.txt.delete(0.0, END)
                self.txt.insert(0.0, f'Empty order!\n'
                                     f'Please choose something.')
                self.center_text()
                self.txt.configure(state=DISABLED)

        except AttributeError:
            self.txt.configure(state=NORMAL)
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, f'Your order has not been accepted!')
            self.center_text()
            self.txt.configure(state=DISABLED)

    def update_text(self):
        self.total_price = 0
        self.vars = ''
        if self.check_btn1.get():
            self.vars += self.keys[0] + '\n'
            self.total_price += self.menu.get(self.keys[0])

        if self.check_btn2.get():
            self.vars += self.keys[1] + '\n'
            self.total_price += self.menu.get(self.keys[1])

        if self.check_btn3.get():
            self.vars += self.keys[2] + '\n'
            self.total_price += self.menu.get(self.keys[2])

        if self.check_btn4.get():
            self.vars += self.keys[3] + '\n'
            self.total_price += self.menu.get(self.keys[3])
        self.txt.configure(state=NORMAL)
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, f'TOTAL PRICE - {str(self.total_price)}\n{self.vars}')
        self.center_text()
        self.txt.configure(state=DISABLED)

        return self.total_price, self.vars


def main():
    root = Tk()
    root.title('GO VEGAN!')
    app = Application(root)
    app['bg'] = 'black'
    root.resizable(False, False)
    root.geometry("-400-40")
    app.mainloop()


main()
