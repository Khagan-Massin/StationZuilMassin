#Massin Elotmani
import tkinter
from PIL import Image, ImageTk
from tkinter import *
import psycopg2
from req import temp_req
from req import weer_icon
root = Tk()
root['bg'] = 'yellow'

print(temp_req())
print(weer_icon())

weer_img = PhotoImage(file=f'weather_icons/{weer_icon()}@2x.png')
#weer_label = Label(master=root, image=weer_img, background='yellow')
#weer_label.grid(row=0, column=3, columnspan=1)

weather = Label(master = root,
                text=f"{temp_req()} C°",
                background='yellow',
                foreground='blue',
                font=('Arial', 16, 'bold'),
                width=200, height=125,
                image= weer_img,
                compound='right'
                )

weather.grid(row = 0, column=2, columnspan=1)


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
verbinding.commit()

for row in random_text:

    wijzer.execute(f"SELECT * FROM station_service "
                   f"WHERE station_city = '{row[1]}'")

    faciliteit = wijzer.fetchall()
    faciliteit = faciliteit[0]
    print(faciliteit)
    station_city, country, ov_bike, elevator, toilet, park_and_ride = faciliteit
    print(station_city)

    label = Label(master = root,
                    text=f"{row[0]} schreef: '{row[2]}' in {row[1]} op {row[6]}",
                    background='yellow',
                    foreground='blue',
                    font=('Arial', 20, 'bold'),
                    width=100,height=3,
                    )

    label.grid(column=2, columnspan=1)







root.mainloop()