import psycopg2

verbinding = psycopg2.connect(
    host = "localhost",
    database = "ModOpdracht",
    user = "postgres",
    password = "HalloSQL1q2"
)

wijzer = verbinding.cursor()

wijzer.execute("")

verbinding.commit()

wijzer.close()
verbinding.close()

