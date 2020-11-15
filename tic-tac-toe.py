from tkinter import *
from PIL import ImageTk, Image


field = [None, None, None, None, None, None, None, None, None] # O = 0, X = 1
centers = [(423, 200), (565, 200), (707, 200), (423, 342), (565, 342), (707, 342), (423, 484), (565, 484), (707, 484)]
current_move = 1
game_ended = False
labels = []

root = Tk()
c = Canvas(width=1440, height=900)
root.resizable(width=False, height=False)
c.pack(fill=BOTH)

image = ImageTk.PhotoImage(file='images/Dlya_Yarika_chisty_fon.jpg')
c.create_image(1, 1, image=image, anchor=NW)


def click(mv):
    if game_ended == False:
        mv=int(mv)
        move(mv)
        buttons[mv].place_forget()


def restart():
    global field
    global game_ended
    c.delete('object')
    field = [None, None, None, None, None, None, None, None, None]
    game_ended = False
    current_move = 1
    for i in range(9):
        buttons[i].place(x=centers[i][0], y=centers[i][1], height=141, width=141)
    for i in labels:
        i.place_forget()
    move_label = Label(image=move_x_img)
    move_label.place(x=396, y=50, width=481, height=120)


buttons = []
images = []
x_images = []
o_images = []

for i in range(9):
    img = Image.open(f'images/{i+1}.jpg').resize((141, 141))
    images.append(ImageTk.PhotoImage(img))
    img = Image.open(f'images/x{i+1}.jpg').resize((141, 141))
    x_images.append(ImageTk.PhotoImage(img))
    img = Image.open(f'images/o{i+1}.jpg').resize((141, 141))
    o_images.append(ImageTk.PhotoImage(img))

for i in range(9):
    buttons.append(Button(text='', bd=0, image=images[i]))
    buttons[i].place(x=centers[i][0], y=centers[i][1], height=141, width=141)

buttons[0].config(command=lambda: click(0))
buttons[1].config(command=lambda: click(1))
buttons[2].config(command=lambda: click(2))
buttons[3].config(command=lambda: click(3))
buttons[4].config(command=lambda: click(4))
buttons[5].config(command=lambda: click(5))
buttons[6].config(command=lambda: click(6))
buttons[7].config(command=lambda: click(7))
buttons[8].config(command=lambda: click(8))

close_img = Image.open(f'images/vykhod.jpg').resize((126, 126))
close_img = ImageTk.PhotoImage(close_img)
restart_img = Image.open(f'images/restart.jpg').resize((126, 126))
restart_img = ImageTk.PhotoImage(restart_img)

restart_btn = Button(text='', command=restart, image=restart_img, bd=0)
restart_btn.place(x=1000, y=342, height=126, width=126)
close = Button(text='', command=root.destroy, image=close_img, bd=0)
close.place(x=150, y=342, height=126, width=126)

move_o_img = Image.open(f'images/khod_o.jpg').resize((481, 120))
move_o_img = ImageTk.PhotoImage(move_o_img)
move_x_img = Image.open(f'images/khod_x.jpg').resize((481, 120))
move_x_img = ImageTk.PhotoImage(move_x_img)
win_o_img = Image.open(f'images/vyigral_o.jpg').resize((481, 120))
win_o_img = ImageTk.PhotoImage(win_o_img)
win_x_img = Image.open(f'images/vyigral_x.jpg').resize((481, 120))
win_x_img = ImageTk.PhotoImage(win_x_img)

move_label = Label(image=move_x_img)
move_label.place(x=396, y=50, width=481, height=120)


def move(cell):
    global current_move
    global game_ended
    if current_move == 1:
        field[cell] = 1
        draw_x(cell)
        current_move = 0
        move_label = Label(image=move_o_img)
        move_label.place(x=396, y=50, width=481, height=120)
    elif current_move == 0:
        field[cell] = 0
        draw_o(cell)
        current_move = 1
        move_label = Label(image=move_x_img)
        move_label.place(x=396, y=50, width=481, height=120)
    if win(field) == 0:
        move_label = Label(image=win_o_img)
        move_label.place(x=396, y=50, width=481, height=120)
        game_ended = True
    elif win(field) == 1:
        move_label = Label(image=win_x_img)
        move_label.place(x=396, y=50, width=481, height=120)
        game_ended = True
    elif win(field) == 2:
        move_label = Label(text='ничья')
        move_label.place(x=396, y=50, width=481, height=120)
        game_ended = True


def win(field):
    win_combinations = ((0, 1, 2), (2, 5, 8), (6, 7, 8), (0, 3, 6), (0, 4, 8), (2, 4, 6), (3, 4, 5), (1, 4, 7))
    for i in win_combinations:
        if field[i[0]] == field[i[1]] == field[i[2]] and field[i[0]] != None:
            return field[i[0]]
    none_count = 0
    for i in range(9):
        if field[i] == None:
            none_count +=1
    if none_count == 0:
        return 2
    return None


def draw_x(number):
    global centers
    global labels
    labels.append(Label(image=x_images[number]))
    labels[-1].place(x=centers[number][0], y=centers[number][1], width=141, height=141)


def draw_o(number):
    global centers
    global labels
    labels.append(Label(image=o_images[number]))
    labels[-1].place(x=centers[number][0], y=centers[number][1], width=141, height=141)


root.mainloop()
