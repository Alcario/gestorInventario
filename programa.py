import datetime
import os
import sqlite3
from prettytable import PrettyTable


class Persona:
    def __init__(self, id, nombre, apellidos):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos

class Herramienta:
    def __init__(self, id, nombre, cantidad):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad

class HerramientasPrestadas:
    def __init__(self, id, id_Prestamo, id_herramienta, id_cantidad):
        self.id = id
        self.id_Prestamo = id_Prestamo
        self.id_herramienta = id_herramienta
        self.cantidad = id_cantidad

class Prestamo:
    def __init__(self, id, id_persona, devuelto, fecha):
        self.id = id
        self.id_persona = id_persona
        self.devuelto = devuelto
        self.fecha = fecha

class HerramientasDevueltas:
    def __init__(self, id, id_herramienta, id_Prestamo, cantidad, fecha):
        self.id = id
        self.id_herramienta = id_herramienta
        self.id_Prestamo = id_Prestamo
        self.cantidad = cantidad
        self.fecha = fecha

class Connection:
    conn = None
    cursor = None

    def __init__(self):
        self.conn = sqlite3.connect('inventario.db')
        self.cursor = self.conn.cursor()

    def get_personas(self):
        self.cursor.execute('SELECT * FROM Personas')
        rows = self.cursor.fetchall()

        personas = []
        for row in rows:
            persona = Persona(row[0], row[1], row[2])
            personas.append(persona)
        return personas

    def get_persona(self, id):
        self.cursor.execute(
            'SELECT * FROM Personas WHERE idPersona = ?', (id,))
        row = self.cursor.fetchone()
        persona = Persona(row[0], row[1], row[2])
        return persona

    def insert_persona(self, persona):
        self.cursor.execute(
            'INSERT INTO Personas (nombre, apellido) VALUES (?, ?)', (persona.nombre, persona.apellidos))
        self.conn.commit()

    def get_herramientas(self):
        self.cursor.execute('SELECT * FROM Herramientas')
        rows = self.cursor.fetchall()

        herramientas = []
        for row in rows:
            herramienta = Herramienta(row[0], row[1], row[2])
            herramientas.append(herramienta)
        return herramientas

    def get_herramienta(self, id):
        self.cursor.execute(
            'SELECT * FROM Herramientas WHERE idHerramienta = ?', (id,))
        row = self.cursor.fetchone()
        herramienta = Herramienta(row[0], row[1], row[2])
        return herramienta

    def get_herramienta_by_name(self, nombre):
        self.cursor.execute(
            'SELECT * FROM Herramientas WHERE nombre = ?', (nombre))
        row = self.cursor.fetchone()
        herramienta = Herramienta(row[0], row[1], row[2])
        return herramienta

    def insert_herramienta(self, herramienta):
        self.cursor.execute(
            'INSERT INTO Herramientas (nombre, cantidad) VALUES (?, ?)', (herramienta.nombre, herramienta.cantidad))
        self.conn.commit()

    def update_herramienta(self, id_herramienta, cantidad):
        self.cursor.execute(
            'UPDATE Herramientas SET cantidad = ? WHERE idHerramienta = ?', (cantidad, id_herramienta))
        self.conn.commit()

    def get_herramientasPrestadas(self):
        self.cursor.execute(
            'SELECT * FROM HerramientasPrestadas')
        rows = self.cursor.fetchall()
        herramientasPrestadas = []
        for row in rows:
            herramientaPrestada = HerramientasPrestadas(
                row[0], row[1], row[2], row[3])
            herramientasPrestadas.append(herramientaPrestada)
        return herramientasPrestadas

    def get_herramientaPrestada(self, id):
        self.cursor.execute(
            'SELECT * FROM herramientasPrestadas WHERE idHerramientaPrestada = ?', (id,))
        row = self.cursor.fetchone()
        herramientaPrestada = HerramientasPrestadas(
            row[0], row[1], row[2], row[3])
        return herramientaPrestada

    def get_ultimaHerramientaPrestada(self):
        self.cursor.execute(
            'SELECT * FROM herramientasPrestadas ORDER BY idHerramientaPrestada DESC LIMIT 1')
        row = self.cursor.fetchone()
        herramientaPrestada = HerramientasPrestadas(
            row[0], row[1], row[2], row[3])
        return herramientaPrestada

    def insert_herramientaPrestada(self, id_herramienta, id_prestamo, cantidad):
        self.cursor.execute(
            'INSERT INTO herramientasPrestadas (idHerramienta, idPrestamo, cantidad) VALUES (?, ?, ?)', (id_herramienta, id_prestamo, cantidad))
        self.conn.commit()

    def get_herramientasPrestadas_by_idPrestamo(self, id):
        self.cursor.execute(
            'SELECT * FROM herramientasPrestadas WHERE idPrestamo = ?', (id,))
        rows = self.cursor.fetchall()
        herramientasPrestadas = []
        for row in rows:
            herramientaPrestada = HerramientasPrestadas(
                row[0], row[1], row[2], row[3])
            herramientasPrestadas.append(herramientaPrestada)
        return herramientasPrestadas

    def get_prestamos(self):
        self.cursor.execute('SELECT * FROM Prestamos WHERE devuelto = 0')
        rows = self.cursor.fetchall()
        prestamos = []
        for row in rows:
            prestamo = Prestamo(row[0], row[1], row[2], row[3])
            prestamos.append(prestamo)
        return prestamos

    def get_prestamos_devueltos(self):
        self.cursor.execute('SELECT * FROM Prestamos WHERE devuelto = 1')
        rows = self.cursor.fetchall()
        prestamos = []
        for row in rows:
            prestamo = Prestamo(row[0], row[1], row[2], row[3])
            prestamos.append(prestamo)
        return prestamos

    def get_prestamo(self, id):
        self.cursor.execute(
            'SELECT * FROM Prestamos WHERE idPrestamo = ?', (id,))
        row = self.cursor.fetchone()
        prestamo = Prestamo(row[0], row[1], row[2], row[3])
        return prestamo

    def insert_prestamo(self, prestamo):
        self.cursor.execute(
            'INSERT INTO Prestamos (idPersona, devuelto, fecha) VALUES (?, ?, ?)', (prestamo.id_persona, 0, datetime.datetime.now()))
        self.conn.commit()

    def insert_prestamoCompleto(self, id_persona):
        self.cursor.execute(
            'INSERT INTO Prestamos (idPersona, devuelto, fecha) VALUES (?, ?, ?)', (id_persona, 0, datetime.datetime.now()))
        self.conn.commit()

    def update_prestamo(self, id_prestamo):
        self.cursor.execute(
            'UPDATE Prestamos SET devuelto = 1 WHERE idPrestamo = ?', (id_prestamo,))
        self.conn.commit()

    def get_ultimoPrestamo(self):
        self.cursor.execute(
            'SELECT * FROM Prestamos ORDER BY idPrestamo DESC LIMIT 1')
        row = self.cursor.fetchone()
        prestamo = Prestamo(row[0], row[1], row[2], row[3])
        return prestamo

    def update_herramienta(self, id_herramienta, cantidad):
        self.cursor.execute(
            'UPDATE Herramientas SET cantidad = ? WHERE idHerramienta = ?', (cantidad, id_herramienta))
        self.conn.commit()

    def get_herramientasDevueltas(self):
        self.cursor.execute('SELECT * FROM HerramientasDevueltas')
        rows = self.cursor.fetchall()
        herramientasDevueltas = []
        for row in rows:
            herramientaDevuelta = HerramientasDevueltas(
                row[0], row[1], row[2], row[3], row[4])
            herramientasDevueltas.append(herramientaDevuelta)
        return herramientasDevueltas

    def get_herramientaDevuelta(self, id):
        self.cursor.execute(
            'SELECT * FROM HerramientasDevueltas WHERE idHerramientaDevuelta = ?', (id,))
        row = self.cursor.fetchone()
        herramientaDevuelta = HerramientasDevueltas(
            row[0], row[1], row[2], row[3], row[4])
        return herramientaDevuelta

    def get_herramientasDevueltas_by_idPrestamo(self, id):
        self.cursor.execute(
            'SELECT * FROM HerramientasDevueltas WHERE idPrestamo = ?', (id))
        rows = self.cursor.fetchall()

        herramientasDevueltas = []
        for row in rows:
            herramientaDevuelta = HerramientasDevueltas(
                row[0], row[1], row[2], row[3], row[4])
            herramientasDevueltas.append(herramientaDevuelta)

        return herramientasDevueltas

    def get_herramientasDevueltas_by_idPrestamo_idHerramienta(self, idPrestamo, idHerramienta):
        self.cursor.execute(
            'SELECT * FROM HerramientasDevueltas WHERE idPrestamo = ? AND idHerramienta = ?', (idPrestamo, idHerramienta))
        row = self.cursor.fetchone()

        if row is None:
            return HerramientasDevueltas(None, None, None, None, 0)

        herramientaDevuelta = HerramientasDevueltas(
            row[0], row[1], row[2], row[3], row[4])

        return herramientaDevuelta

    def insert_herramientaDevuelta(self, id_herramienta, id_prestamo, cantidad):
        self.cursor.execute(
            'INSERT INTO HerramientasDevueltas (idHerramienta, idPrestamo, cantidad, fecha) VALUES (?, ?, ?, ?)', (id_herramienta, id_prestamo, cantidad, datetime.datetime.now()))
        self.conn.commit()


def mostrar_personas():
    try:
        os.system("cls")
        personas = conn.get_personas()

        table = PrettyTable()
        table.field_names = ["ID", "Nombre", "Apellidos"]

        for persona in personas:
            table.add_row([persona.id, persona.nombre, persona.apellidos])

        print(table)

    except Exception as e:
        print(e)


def mostrar_herramientas():
    try:
        os.system("cls")
        herramientas = conn.get_herramientas()
        table = PrettyTable()
        table.field_names = ["ID", "Nombre", "Cantidad"]

        for herramienta in herramientas:
            table.add_row(
                [herramienta.id, herramienta.nombre, herramienta.cantidad])
        print(table)
    except Exception as e:
        print(e)


def mostrar_prestamos():
    try:
        os.system("cls")
        table = PrettyTable()
        table.field_names = [
            "ID Préstamo", "Fecha", "Nombre", "Apellidos", "Herramienta", "Cantidad"]

        prestamos = conn.get_prestamos()
        sorted_prestamos = sorted(prestamos, key=lambda x: x.id)

        for prestamo in sorted_prestamos:
            persona = conn.get_persona(prestamo.id_persona)
            herramientasPrestadas = conn.get_herramientasPrestadas_by_idPrestamo(
                prestamo.id)
            for herramientaPrestada in herramientasPrestadas:
                herramienta = conn.get_herramienta(
                    herramientaPrestada.id_herramienta)
                fecha = datetime.datetime.strptime(
                    prestamo.fecha, "%Y-%m-%d %H:%M:%S.%f")
                fecha_formateada = fecha.strftime(
                    "%d/%m/%y %H:%M:%S")
                table.add_row(
                    [prestamo.id, fecha_formateada, persona.nombre, persona.apellidos, herramienta.nombre, herramientaPrestada.cantidad])
        print(table)
    except Exception as e:
        print(e)

def insertar_persona():
    try:
        os.system("cls")
        persona = Persona(0, input("Ingresa el nombre: "), input(
            "Ingresa el apellido: "))
        conn.insert_persona(persona)
        print("\n**********************************")
        print("**\tPersona agregada\t**")
        print("**\t------------------\t**")
        print("**********************************\n")
    except Exception as e:
        print(e)

def insertar_herramienta():
    try:
        os.system("cls")
        herramienta = Herramienta(
            0, input("Ingresa el nombre: "), input("Ingresa la cantidad: "))
        conn.insert_herramienta(herramienta)
        print("\n**********************************")
        print("**\tHerramienta agregada\t**")
        print("**\t------------------\t**")
        print("**********************************\n")
    except Exception as e:
        print(e)

def prestar_herramienta():
    try:
        os.system("cls")
        mostrar_personas()

        idPersona = input("\nSeleccione la persona: ")
        cantHerramientas = input(
            "¿Cuantas herramientas necesita?: ")

        conn.insert_prestamoCompleto(idPersona)

        for i in range(int(cantHerramientas)):
            mostrar_herramientas()

            id_herramienta = input("\nSeleccione la herramienta: ")
            cantidad = input("Ingresa la cantidad: ")
            while True:
                if int(cantidad) <= int(conn.get_herramienta(id_herramienta).cantidad):
                    break
                else:
                    print(
                        "La cantidad de herramientas que se prestan es mayor a la cantidad de herramientas que hay")
                    cantidad = input("Ingresa la cantidad: ")

            conn.insert_herramientaPrestada(
                id_herramienta, conn.get_ultimoPrestamo().id, cantidad)

            update_herramienta = conn.update_herramienta(
                id_herramienta,  int(conn.get_herramienta(id_herramienta).cantidad)-int(cantidad))

        if int(cantHerramientas) > 1:
            print("\n**********************************")
            print("**\tHerramientas prestadas\t**")
            print("**\t------------------\t**")
            print("**********************************\n")
        else:
            print("\n**********************************")
            print("**\tHerramienta prestada\t**")
            print("**\t------------------\t**")
            print("**********************************\n")
    except Exception as e:
        print(e)

def listar_devoluciones():
    try:
        os.system("cls")
        herramientasDevueltas = conn.get_herramientasDevueltas()
        table = PrettyTable()
        table.field_names = [
            "ID Préstamo", "Fecha", "Nombre", "Apellidos", "Herramienta", "Cantidad"]

        for herramientaDevuelta in herramientasDevueltas:
            prestamo = conn.get_prestamo(
                herramientaDevuelta.id_Prestamo)
            persona = conn.get_persona(prestamo.id_persona)
            herramienta = conn.get_herramienta(
                herramientaDevuelta.id_herramienta)
            fecha = datetime.datetime.strptime(
                herramientaDevuelta.fecha, "%Y-%m-%d %H:%M:%S.%f")
            fecha_formateada = fecha.strftime("%d/%m/%y %H:%M:%S")
            table.add_row(
                [herramientaDevuelta.id_Prestamo, fecha_formateada, persona.nombre, persona.apellidos, herramienta.nombre, herramientaDevuelta.cantidad])
        print(table)
    except Exception as e:
        print(e)


def mostrar_herramientas_ordenadas():
    try:
        os.system("cls")
        herramientas = conn.get_herramientas()
        table = PrettyTable()
        table.field_names = ["ID", "Nombre"]
        for herramienta in herramientas:
            table.add_row([herramienta.id, herramienta.nombre])
        print(table)
    except Exception as e:
        print(e)


def mostrar_prestamos_devueltos():
    try:
        os.system("cls")
        table = PrettyTable()
        table.field_names = [
            "ID Préstamo", "Fecha", "Nombre", "Apellidos", "Herramienta", "Cantidad"]

        prestamos = conn.get_prestamos_devueltos()
        sorted_prestamos = sorted(prestamos, key=lambda x: x.id)

        for prestamo in sorted_prestamos:
            persona = conn.get_persona(prestamo.id_persona)
            herramientasPrestadas = conn.get_herramientasPrestadas_by_idPrestamo(
                prestamo.id)
            for herramientaPrestada in herramientasPrestadas:
                herramienta = conn.get_herramienta(
                    herramientaPrestada.id_herramienta)

                fecha = datetime.datetime.strptime(
                    prestamo.fecha, "%Y-%m-%d %H:%M:%S.%f")
                fecha_formateada = fecha.strftime(
                    "%d/%m/%y %H:%M:%S")
                table.add_row(
                    [prestamo.id, fecha_formateada, persona.nombre, persona.apellidos, herramienta.nombre, herramientaPrestada.cantidad])
        print(table)
    except Exception as e:
        print(e)


def mostrar_prestamos_devolución():
    try:
        os.system("cls")
        table = PrettyTable()
        table.field_names = [
            "ID Préstamo", "Fecha", "Nombre", "Apellidos", "Herramienta", "Cantidad"]

        prestamos = conn.get_prestamos()
        sorted_prestamos = sorted(prestamos, key=lambda x: x.id)

        for prestamo in sorted_prestamos:
            persona = conn.get_persona(prestamo.id_persona)
            herramientasPrestadas = conn.get_herramientasPrestadas_by_idPrestamo(
                prestamo.id)
            for herramientaPrestada in herramientasPrestadas:
                herramienta = conn.get_herramienta(
                    herramientaPrestada.id_herramienta)

                cantidadHerramientasDevueltas = conn.get_herramientasDevueltas_by_idPrestamo_idHerramienta(
                    prestamo.id, herramienta.id).cantidad
                if cantidadHerramientasDevueltas == None:
                    cantidadHerramientasDevueltas = 0

                cantidad = herramientaPrestada.cantidad - \
                    int(cantidadHerramientasDevueltas)

                fecha = datetime.datetime.strptime(
                    prestamo.fecha, "%Y-%m-%d %H:%M:%S.%f")
                fecha_formateada = fecha.strftime(
                    "%d/%m/%y %H:%M:%S")
                table.add_row(
                    [prestamo.id, fecha_formateada, persona.nombre, persona.apellidos, herramienta.nombre, cantidad])
        print(table)
    except Exception as e:
        print(e)


def devolver_herramienta():
    try:
        os.system("cls")
        mostrar_prestamos_devolución()

        idPrestamo = input("\nSeleccione el prestamo: ")

        herramientas = conn.get_herramientasPrestadas_by_idPrestamo(idPrestamo)
        bandera = 1
        for herramienta in herramientas:
            cantidadHerramientasDevueltas = conn.get_herramientasDevueltas_by_idPrestamo_idHerramienta(
                idPrestamo, herramienta.id_herramienta).cantidad
            if cantidadHerramientasDevueltas == None:
                cantidadHerramientasDevueltas = 0
            if cantidadHerramientasDevueltas == herramienta.cantidad:
                continue
            else:
                cantidad = int(input(
                    "Ingresa la cantidad de herramientas a devolver de " + conn.get_herramienta(herramienta.id_herramienta).nombre + ": "))

                while True:
                    if cantidad > 0:
                        if (int(cantidad)+int(cantidadHerramientasDevueltas)) == int(herramienta.cantidad):
                            break
                        elif (int(cantidad)+int(cantidadHerramientasDevueltas)) < int(herramienta.cantidad):
                            bandera = 0
                            break
                        else:
                            print(
                                "La cantidad a devolver supera la cantidad de herramientas prestadas")
                    else:
                        print("La cantidad debe ser mayor a 0")

                    cantidad = int(input(
                        "Ingresa la cantidad de herramientas a devolver de " + conn.get_herramienta(herramienta.id_herramienta).nombre + ": "))

                conn.update_herramienta(herramienta.id_herramienta, int(
                    conn.get_herramienta(herramienta.id_herramienta).cantidad)+int(cantidad))
                conn.insert_herramientaDevuelta(
                    herramienta.id_herramienta, idPrestamo, int(cantidad))

        if int(len(herramientas)) > 1:
            print("\n**********************************")
            print("**\tHerramientas devueltas\t**")
            print("**\t----------------------\t**")
            print("**********************************\n")
        else:
            print("\n**********************************")
            print("**\tHerramienta devuelta\t**")
            print("**\t------------------\t**")
            print("**********************************\n")

        if bandera == 1:
            conn.update_prestamo(idPrestamo)
    except Exception as e:
        print(e)


def actualizar_cantidad_herramienta():
    try:
        os.system("cls")
        herramientas = conn.get_herramientas()
        print("\n******************************************")
        print("**\tHerramientas encontradas\t**")
        print("**\t------------------------\t**")

        for herramienta in herramientas:
            print("**\t", herramienta.id, " - ", herramienta.nombre,
                  " - ", herramienta.cantidad, "\t**")
        print("******************************************\n")

        id_herramienta = input("\nSeleccione la herramienta: ")
        cantidad = input("Ingresa la cantidad: ")

        # controlar que la cantidad de herramientas a ingresar sea mayor a 0
        while True:
            if int(cantidad) > 0:
                break
            else:
                print("La cantidad debe ser mayor a 0")
                cantidad = input("Ingresa la cantidad: ")

        conn.update_herramienta(id_herramienta, int(
            conn.get_herramienta(id_herramienta).cantidad)+int(cantidad))
    except Exception as e:
        print(e)

try:
    conn = Connection()

    while True:
        os.system("cls")
        print("-----------------------MENU-----------------------")
        print("--\t1. Listar personas\t\t\t--")
        print("--\t2. Listar herramientas\t\t\t--")
        print("--\t3. Listar prestamos\t\t\t--")
        print("--\t4. Listar prestamos devueltos\t\t--")
        print("--\t5. Listar herramientas devueltas\t--")
        print("--\t6. Insertar persona\t\t\t--")
        print("--\t7. Insertar herramienta\t\t\t--")
        print("--\t8. Prestar herramienta\t\t\t--")
        print("--\t9. Devolver herramienta\t\t\t--")
        print("--\t10. Actualizar cantidad de herramientas\t--")
        print("--\t11. Salir\t\t\t\t--")
        print("--------------------------------------------------")
        op = input("Opción: ")

        match op:
            case "1":
                mostrar_personas()
                input()
                continue

            case "2":
                mostrar_herramientas()
                input()
                continue
            case "3":
                mostrar_prestamos()
                input()
                continue

            case "4":
                mostrar_prestamos_devueltos()
                input()
                continue

            case "5":
                listar_devoluciones()
                input()
                continue

            case "6":
                insertar_persona()
                input()
                continue

            case "7":
                insertar_herramienta()
                input()
                continue
            case "8":
                prestar_herramienta()

                input()
                continue
            case "9":
                devolver_herramienta()
                input()
                continue
            case "10":
                actualizar_cantidad_herramienta()
                input()
                continue
            case "11":
                os.system("cls")
                print("Saliendo...")
                break

except Exception as e:
    print(e)
