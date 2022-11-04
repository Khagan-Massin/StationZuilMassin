#Massin Elotmani
from PIL import Image, ImageFilter
from tkinter import *
import psycopg2
from req import temp_req
from req import weer_icon
root = Tk()
root['bg'] = '#FFC917'
root.geometry("1280x720")


logo_img = PhotoImage(file=f'NS_logo2.png')
logo_label = Label(master=root, image=logo_img, background='#FFC917')
logo_label.grid(row=0, column=1)

weer_img = PhotoImage(file=f'weather_icons/{weer_icon()}@2x.png')

weather = Label(master=root,
                text=f" {temp_req()} C°",
                background='#89CFF0',
                foreground='white',
                font=('Arial', 20, 'bold'),
                width=200, height=125,
                image=weer_img,
                compound='bottom',
                )

weather.grid(row=0, column=3, columnspan=1)

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

lift_img = PhotoImage(file=f'ov_icons/img_lift.png')
ov_fiets_img = PhotoImage(file=f'ov_icons/img_ovfiets.png')
pr_img = PhotoImage(file=f'ov_icons/img_pr.png')
toilet_img = PhotoImage(file=f'ov_icons/img_toilet.png')

rij = 0
for row in random_text:
    rij += 1
    wijzer.execute(f"SELECT * FROM station_service "
                   f"WHERE station_city = '{row[1]}'")

    faciliteit = wijzer.fetchall()
    faciliteit = faciliteit[0]
    print(faciliteit)
    station_city, country, ov_bike, elevator, toilet, park_and_ride = faciliteit
    col = 0

    if ov_bike:
        ov_fiets_label = Label(master=root, image=ov_fiets_img, background='#FFC917', width=150, height=150, )
        ov_fiets_label.grid(column=col, columnspan=1, row=rij)
        col += 1
    if elevator:
        lift_label = Label(master=root, image=lift_img, background='#FFC917', width=150, height=150, )
        lift_label.grid(column=col, columnspan=1, row=rij)
        col += 1
    if toilet:
        toilet_label = Label(master=root, image=toilet_img, background='#FFC917', width=150, height=150, )
        toilet_label.grid(column=col, columnspan=1, row=rij)
        col += 1
    if park_and_ride:
        pr_label = Label(master=root, image=pr_img, background='#FFC917', width=150, height=150, )
        pr_label.grid(column=col, columnspan=1, row=rij)
        col += 1
    else:
        pass
    col = 0

    label = Label(master=root,
                  text=f"{row[0]} schreef: '{row[2]}' in {row[1]} op {row[6]}",
                  background='#FFC917',#NS geel
                  foreground='#003082',#NS blauw
                  font=('Arial', 20, 'bold'),
                  width=65,
                  height=2,
                  )

    label.grid(column=4, row=rij, columnspan=1, sticky=E)




root.mainloop()
