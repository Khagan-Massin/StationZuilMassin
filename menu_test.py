#Massin Elotmani
import tkinter
from tkinter import *
import psycopg2
from req import api_rek
from req import weer_icon
root = Tk()
root['bg'] = 'yellow'

print(api_rek())
print(weer_icon())

weather = Label(master = root,
                    text=f"{api_rek()} C°",
                    background='yellow',
                    foreground='blue',
                    font=('Arial', 16, 'bold'),
                    width=25,height=2,
                    )

weather.grid(row = 0, column=2, columnspan=1)

my_img = PhotoImage(file='img_lift.png')
my_label = Label(master=root,image=my_img)
my_label.grid(row = 1, column=1, columnspan=1)

# my_img = PhotoImage(file='img_ovfiets.png')
# my_label = Label(master=root,image=my_img)
# my_label.grid(row = 5, column=2, columnspan=1)
#
# my_img = PhotoImage(file='img_pr.png')
# my_label = Label(master=root,image=my_img)
# my_label.grid(row = 5, column=3, columnspan=1)
#
# my_img = PhotoImage(file='img_toilet.png')
# my_label = Label(master=root,image=my_img)
# my_label.grid(row = 5, column=4, columnspan=1)


verbinding = psycopg2.connect(
    host="localhost",
    database="StationZuilMassin",
    user="postgres",
    password="HalloSQL1q2"
)

wijzer = verbinding.cursor()

wijzer.execute(
    f"SELECT * "
    f"FROM opmerkingen "
    f"WHERE goedgekeurd = TRUE "
    f"ORDER BY id DESC LIMIT 5;"
)

random_text = wijzer.fetchall()
print(random_text)
verbinding.commit()
wijzer.close()

for row in random_text:
    label = Label(master = root,
                    text=f"{row[0]} schreef: '{row[2]}' in {row[1]} op {row[6]}",
                    background='yellow',
                    foreground='blue',
                    font=('Arial', 20, 'bold'),
                    width=100,height=3,
                    )

    label.grid(column=2, columnspan=1)





root.mainloop()