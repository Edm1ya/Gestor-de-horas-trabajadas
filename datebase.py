import sqlite3

class Datebase:
    def __init__(self) -> None:
        try:
            conexion = sqlite3.connect("db1.db")
            conexion.execute("""CREATE TABLE registros (
                                            id integer primary key autoincrement,
                                            fecha text,
                                            hora1 text,
                                            hora2 text,
                                            hora3 real,
                                            lugar text
                                            )""")
        except sqlite3.OperationalError:
            print("la tabla ya existe")
    
    def agregar(self, fecha, hora1,hora2,hora3,lugar):
        cone = sqlite3.connect("db1.db")
        cone.execute("INSERT INTO registros (fecha, hora1, hora2, hora3, lugar) values (?,?,?,?,?)", (fecha, hora1, hora2, hora3, lugar))
        cone.commit()
        # cursor = cone.cursor()
        cone.close

    def mostrar(self):
        cone = sqlite3.connect("db1.db")
        cursor = cone.cursor()
        reg = cursor.execute("select fecha, hora1, hora2, hora3, lugar from registros")
        # for fila in reg:
        #     for fil in fila: 
        #         print(type(fil), fil)

        return reg
    
    def borrar(self, id):
        cone = sqlite3.connect("db1.db")
        cursor = cone.cursor()
        cursor.execute("delete from registros where id=?",(id))
        cone.commit()
        cone.close()

    def identificar(self, fecha, hora1, hora2, hora3,lugar):
        cone = sqlite3.connect("db1.db")
        cursor = cone.cursor()
        cursor.execute("select id from registros where fecha=? and hora1=? and hora2=? and hora3=? and lugar=?", (fecha,hora1, hora2, hora3,lugar))
        fila = cursor.fetchone()
        cone.close()
        
        return fila
    
    def edit(self, old_fecha, old_hora1 ,old_hora2 ,old_hora3 ,old_lugar, fecha_edit, hora1_edit, hora2_edit, hora3_edit, lugar_edit ):

        cone = sqlite3.connect("db1.db")
        cursor = cone.cursor()
        # cursor.execute("update registros set fecha=?, hora1=?, hora2=?, hora3=?, lugar=? where id=?", (fecha, hora1, hora2, hora3, lugar, id))
        cursor.execute("UPDATE registros SET fecha=?, hora1=?, hora2=?, lugar=? WHERE fecha=? and hora1=? and hora2=? and lugar=?", (old_fecha, old_hora1 ,old_hora2,old_lugar, fecha_edit, hora1_edit, hora2_edit, lugar_edit))
        cone.commit()
        cone.close


a = Datebase()
a.mostrar()

 