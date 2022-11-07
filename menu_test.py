#Massin Elotmani
from PIL import Image, ImageFilter
from tkinter import *
from tkinter import ttk
import psycopg2
from req import temp_req
from req import weer_icon
root = Tk()
root['bg'] = '#FFC917'
#root.geometry("1280x720")



logo_img = PhotoImage(file=f'NS_logo2.png')
logo_label = Label(master=root, image=logo_img, background='#FFC917')
logo_label.grid(row=0, column=0)
def weer_func(stad):
    weer_img = PhotoImage(file=f'weather_icons/{weer_icon(stad)}@2x.png')

    weather = Label(master=root,
                    text=f" {temp_req(stad)} C°",
                    background='#89CFF0',
                    foreground='white',
                    font=('Arial', 25, 'bold'),
                    width=200, height=125,
                    image=weer_img,
                    compound='bottom',
                    )
    weather.img = weer_img

    weather.grid(row=0, column=4, columnspan=1, sticky=E)

weer_button_ams = ttk.Button(root, text="Amsterdam", command=lambda: weer_func("amsterdam"))
weer_button_ams.grid(row=0, column=1, sticky=E)

weer_button_utr = ttk.Button(root, text="Utrecht", command=lambda: weer_func("utrecht"))
weer_button_utr.grid(row=0, column=2, sticky=W)

weer_button_rot = ttk.Button(root, text="Rotterdam", command=lambda: weer_func("rotterdam"))
weer_button_rot.grid(row=0, column=3, sticky=W)

weer_button_hil = ttk.Button(root, text="Hilversum", command=lambda: weer_func("hilversum"))
weer_button_hil.grid(row=0, column=4, sticky=W)

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

last_5 = wijzer.fetchall()
verbinding.commit()

lift_img = PhotoImage(file=f'ov_icons/img_lift.png')
ov_fiets_img = PhotoImage(file=f'ov_icons/img_ovfiets.png')
pr_img = PhotoImage(file=f'ov_icons/img_pr.png')
toilet_img = PhotoImage(file=f'ov_icons/img_toilet.png')

rij = 0
for row_last5 in last_5:
    rij += 1
    wijzer.execute(f"SELECT * FROM station_service "
                   f"WHERE station_city = '{row_last5[1]}'")

    faciliteit = (wijzer.fetchall())[0]
    station_city, country, ov_bike, elevator, toilet, park_and_ride = faciliteit

    col = 0

    if ov_bike:
        ov_fiets_label = Label(master=root, image=ov_fiets_img, background='#003082', width=128, height=128, )
        ov_fiets_label.grid(column=col, columnspan=1, row=rij)
        col += 1
    if elevator:
        lift_label = Label(master=root, image=lift_img, background='#003082', width=128, height=128, )
        lift_label.grid(column=col, columnspan=1, row=rij)
        col += 1
    if toilet:
        toilet_label = Label(master=root, image=toilet_img, background='#003082', width=128, height=128, )
        toilet_label.grid(column=col, columnspan=1, row=rij)
        col += 1
    if park_and_ride:
        pr_label = Label(master=root, image=pr_img, background='#003082', width=128, height=128, )
        pr_label.grid(column=col, columnspan=1, row=rij)
        col += 1

    col = 0

    comment_label = Label(master=root,
                          text=f"{row_last5[0]} schreef: '{row_last5[2]}' in {row_last5[1]} op {row_last5[6]}",
                          background='#FFC917',  #NS geel
                          foreground='#003082',  #NS blauw
                          font=('Arial', 20, 'bold'),
                          width=65,
                          height=2,
                          )

    comment_label.grid(column=4, row=rij, columnspan=1, sticky=N)

    sep = ttk.Separator(
        master = root,
        orient = 'horizontal'
    )
    sep.grid(row=rij, column=4, columnspan=1 ,ipadx=500, pady=10)

root.mainloop()
