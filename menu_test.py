from tkinter import *
import psycopg2
import requests
import json
root = Tk()


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
                    font=('Arial', 16, 'bold'),
                    width=100,height=3,
                    )

    label.pack()









root.mainloop()