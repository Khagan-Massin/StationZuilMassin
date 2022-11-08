#Massin Elotmani
from PIL import Image, ImageFilter
from tkinter import *
from tkinter import ttk
import psycopg2
from req import temp_req
from req import weer_icon
root = Tk()
root['bg'] = '#FFC917'
root.title('Nederlandse Spoorwegen')


# Voegt NS logo
logo_img = PhotoImage(file=f'NS_logo2.png')
logo_label = Label(master=root, image=logo_img, background='#FFC917', relief = 'sunken')
logo_label.grid(row=0, column=0, sticky = N)
def weer_func(stad):
    weer_img = PhotoImage(file=f'weather_icons/{weer_icon(stad)}@2x.png')

    weather = Label(master=root,
                    text=f"{temp_req(stad)} C° in\n{stad}",
                    background='#89CFF0',
                    foreground='white',
                    font=('Arial', 25, 'bold'),
                    width=230, height=175,
                    image=weer_img,
                    compound='top',
                    )
    weather.img = weer_img

    weather.grid(row=0, column=4, columnspan=1, sticky=E)
# Maak Knoppen voor weer in verschillende steden
weer_button_ams = ttk.Button(root, text="Amsterdam", command=lambda: weer_func("Amsterdam"))
weer_button_ams.grid(row=0, column=1, sticky=E)

weer_button_utr = ttk.Button(root, text="Utrecht", command=lambda: weer_func("Utrecht"))
weer_button_utr.grid(row=0, column=2, sticky=W)

weer_button_rot = ttk.Button(root, text="Rotterdam", command=lambda: weer_func("Rotterdam"))
weer_button_rot.grid(row=0, column=3, sticky=W)

weer_button_hil = ttk.Button(root, text="Hilversum", command=lambda: weer_func("Hilversum"))
weer_button_hil.grid(row=0, column=4, sticky=W)

# Voor dat een van de knoppen is ingedrukt laat het weer in utrecht zien
weer_func('Utrecht')

verbinding = psycopg2.connect(
    host="localhost",
    database="StationZuilMassin",
    user="postgres",
    password="HalloSQL1q2"
)

wijzer = verbinding.cursor()
#Pakt de vijf meest recente goedgekeurde opmerkingen
wijzer.execute(
    f"SELECT * "
    f"FROM opmerkingen "
    f"WHERE goedgekeurd = TRUE "
    f"ORDER BY id DESC LIMIT 5;"
)

last_5 = wijzer.fetchall()
verbinding.commit()
#Laad in all de faciliteit iconen
lift_img = PhotoImage(file=f'ov_icons/img_lift.png')
ov_fiets_img = PhotoImage(file=f'ov_icons/img_ovfiets.png')
pr_img = PhotoImage(file=f'ov_icons/img_pr.png')
toilet_img = PhotoImage(file=f'ov_icons/img_toilet.png')

'''
Rij variable woord elke iteratie van de for loop +1 groter 
zodat elk label en faciliteit plaatje onder de vorige word geplaatst
'''
rij = 0
for row_last5 in last_5:
    rij += 1
    wijzer.execute(f"SELECT * FROM station_service "
                   f"WHERE station_city = '{row_last5[1]}'")

    faciliteit = (wijzer.fetchall())[0]
    #Maak elke kolom in database eigen variable
    station_city, country, ov_bike, elevator, toilet, park_and_ride = faciliteit

    col = 0
    #Zet welke labels er worden geplaatst labels is altijd 1 naast de vorige
    #col variable word elke keer dat een label word geplaatst een groter.
    if ov_bike:
        ov_fiets_label = Label(master=root, image=ov_fiets_img, background='#003082', width=128, height=128, )
        ov_fiets_label.grid(column=col, columnspan=1, row=rij ,sticky=E)
        col += 1
    if elevator:
        lift_label = Label(master=root, image=lift_img, background='#003082', width=128, height=128, )
        lift_label.grid(column=col, columnspan=1, row=rij,sticky=E)
        col += 1
    if toilet:
        toilet_label = Label(master=root, image=toilet_img, background='#003082', width=128, height=128, )
        toilet_label.grid(column=col, columnspan=1, row=rij,sticky=E)
        col += 1
    if park_and_ride:
        pr_label = Label(master=root, image=pr_img, background='#003082', width=128, height=128, )
        pr_label.grid(column=col, columnspan=1, row=rij,sticky=E)
        col += 1
    #reset col variable
    col = 0
    '''
    Plaats eem opmerking op het scherm
    row_last5[0] = naam
    row_last5[2] = opmerkingen
    row_last5[1] = station
    row_last5[5] = tijddatum
    '''
    comment_label = Label(master=root,
                          text=f"{row_last5[0]} schreef: '{row_last5[2]}' in {row_last5[1]} op {row_last5[5]}",
                          background='#FFC917',  #NS geel
                          foreground='#003082',  #NS blauw
                          font=('Arial', 20, 'bold'),
                          width=65,
                          height=2,
                          )

    comment_label.grid(column=4, row=rij, columnspan=1,)
    #Lijntje voor decoratie
    sep = ttk.Separator(
        master = root,
        orient = 'horizontal'
    )
    sep.grid(row=rij, column=4, columnspan=1 ,ipadx=500, pady=10, sticky=S)

#Sluit verbinding en start tkinter
verbinding.close()
wijzer.close()
root.mainloop()
