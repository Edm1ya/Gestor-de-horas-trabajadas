from tkinter import *
from tkinter import ttk 
from helpers import Registro
from datebase import Datebase
import sqlite3

class Mainwindow():
    def __init__(self):
        self.conex = Datebase()
        self.fondo = "#dff9f6"
        self.root = Tk()
        self.root.title("Gestor de Horas")
        self.root.geometry("1020x600")
        self.root.resizable(0,0)
        self.root.config(background=self.fondo)
        self.build()

        self.root.mainloop()

    def build(self):
        #buttons 
        self.framebuttons = Frame(self.root, bg=self.fondo)
        self.framebuttons.grid(column=0,row=0)
        self.buttonsave = Button(self.framebuttons, text="Guardar", command= self.guardar ,width= 20, bg="#23ff00", activebackground='#3bc100')
        self.buttonsave.grid(column=0,row=0, pady= 20)

        self.buttonedit = Button(self.framebuttons, text="Modificar", command= self.modificar ,width= 20, bg="#2765ff", activebackground='#0038c2')
        self.buttonedit.grid(column=0,row=1, pady= 20)

        self.buttondelete = Button(self.framebuttons, text="Borrar", command= self.borrar ,width= 20, bg="#ff0101", activebackground='#df0000')
        self.buttondelete.grid(column=0,row=2, pady= 20)


        #Entry of dates
        self.frame = Frame(self.root, bg=self.fondo)
        self.frame.grid(column=1,row=0)
        
        #Date
        self.labelfecha = Label(self.frame, text="Fecha", bg=self.fondo)
        self.labelfecha.grid(column=0 ,row=0 ,sticky="w")
        self.fecha = StringVar()
        self.entryfecha = Entry(self.frame, textvariable=self.fecha)
        self.entryfecha.grid(column=0, row=1,sticky="w")

        #Time input
        self.labelhora1 = Label(self.frame, text="Hora de Entrada", bg=self.fondo)
        self.labelhora1.grid(column=0,row=2 ,sticky="w")
        self.hora1 = StringVar()
        self.entryhora1 = Entry(self.frame, textvariable=self.hora1)
        self.entryhora1.grid(column=0, row=3, sticky="w")

        #Time Output
        self.labelhora2 = Label(self.frame, text="Hora de Salida", bg=self.fondo)
        self.labelhora2.grid(column=1,row=2, padx=50, sticky="w")
        self.hora2 = StringVar()
        self.entryhora2 = Entry(self.frame, textvariable=self.hora2)
        self.entryhora2.grid(column=1, row=3, padx=50, sticky="w")

        #el color del azaroso labelframe :v
        style = ttk.Style()
        style.configure("Custom.TLabelframe", background=self.fondo, foreground=self.fondo)

        #Time Total
        self.labelframe1 = ttk.Labelframe(self.frame, text="Horas Trabajadas", style="Custom.TLabelframe")
        self.labelframe1.grid(column=2,row=2)
        # self.hora3 = StringVar() 
        self.entryhora3 = Entry(self.labelframe1, textvariable= StringVar(self.labelframe1, value=""), state="readonly")
        self.entryhora3.grid(column=0,row=0)

        #Zone
        self.labellugar = Label(self.frame, text="Lugar", bg=self.fondo)
        self.labellugar.grid(column=1,row=0, padx=50, sticky="w")
        self.lugar = StringVar()
        self.entrylugar = Entry(self.frame, width=25, textvariable=self.lugar)
        self.entrylugar.grid(column=1, row=1, padx=50 , pady=10,sticky="w")

        #button update
        self.buttonupdate = Button(self.frame, text="Actualizar", command=self.update)
        self.buttonupdate.grid(column=2, row=0)


        #Treeview
        self.frameview = ttk.Frame(self.root)
        self.frameview.grid(column=0,row=1, columnspan=2)

        self.treev = ttk.Treeview(self.frameview, selectmode='browse')
        

         #Scrollbar 
        self.scrollbar = Scrollbar(self.frameview, orient="vertical", command=self.treev.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.treev.configure(yscrollcommand=self.scrollbar.set)

        self.treev['column'] = ('Fecha' ,'Hora1' ,'Hora2' ,'Hora3' ,'Lugar')

        self.treev.column("#0",width=0, stretch=NO)
        self.treev.column("Fecha", anchor=CENTER, stretch=NO)
        self.treev.column("Hora1", anchor=CENTER)
        self.treev.column("Hora2", anchor=CENTER)
        self.treev.column("Hora3", anchor=CENTER)
        self.treev.column("Lugar", anchor=CENTER)

        self.treev.heading("Fecha", text="Fecha", anchor=CENTER)
        self.treev.heading("Hora1", text="Hora Entrada", anchor=CENTER)
        self.treev.heading("Hora2", text="Hora Salida", anchor=CENTER)
        self.treev.heading("Hora3", text="Horas Trabajadas", anchor=CENTER)
        self.treev.heading("Lugar", text="Lugar", anchor=CENTER)
        
        self.treev.bind("<<TreeviewSelect>>", self.clic)

        self.treev.pack(side="left")


        table = self.conex.mostrar()
        for items in table:
         self.treev.insert(
                "","end",text="",values=(items[0],items[1],items[2],items[3],items[4])
                    )

    def update(self):
        time3 = Registro()
        self.hora3 = time3.calculo_horas(self.hora1.get(),self.hora2.get())
        self.entryhora3.config(textvariable= StringVar(self.labelframe1, value =self.hora3))
        self.entryhora3.insert(END,self.hora3)
        self.entryhora3.grid(column=0,row=0)
        
        # self.labelhora3 = Label(self.labelframe1, background=self.fondo, text=self.horas_t)
        # self.labelhora3.grid(column=0,row=0)

    def guardar(self):
        time3 = Registro()
        self.hora3 = time3.calculo_horas(self.hora1.get(),self.hora2.get())
        self.entryhora3.config(textvariable= StringVar(self.labelframe1, value =self.hora3))

        if self.fecha.get() and self.hora1.get() and self.hora2.get() and self.hora3 and self.lugar.get():

            self.conex.agregar(self.fecha.get(), self.hora1.get(), self.hora2.get(), self.hora3, self.lugar.get())
            print("Guardado")

            self.treev.insert("","end", text="", values=(self.fecha.get(), self.hora1.get(), self.hora2.get(), self.hora3, self.lugar.get()))

        else:
            print("Faltan datos")
    

    def modificar(self):
        self.ventana_modificar = Toplevel()
        self.ventana_modificar.title("Ventana de modificar")

        Label(self.ventana_modificar, text="Fecha").grid(row=0, column=0)
        fecha_edit = Entry(self.ventana_modificar)
        fecha_edit.grid(row=0, column=1, padx=5, pady=10)

        Label(self.ventana_modificar, text="Hora Entrada").grid(row=1, column=0)
        hora1_edit = Entry(self.ventana_modificar)
        hora1_edit.grid(row=1, column=1, padx=5, pady=10)

        Label(self.ventana_modificar, text="Hora Salida").grid(row=2, column=0)
        hora2_edit = Entry(self.ventana_modificar)
        hora2_edit.grid(row=2, column=1, padx=5, pady=10)

        Label(self.ventana_modificar, text="Horas Trabajadas").grid(row=3, column=0)
        hora3_edit = Entry(self.ventana_modificar, state="readonly")
        hora3_edit.grid(row=3, column=1, padx=5, pady=10)

        Label(self.ventana_modificar, text="Lugar").grid(row=4, column=0)
        lugar_edit = Entry(self.ventana_modificar)
        lugar_edit.grid(row=4, column=1, padx=5, pady=10)

        Button(self.ventana_modificar, text="Modificar", command=lambda: self.edit_reg(self.old_fecha, self.old_hora1, self.old_hora2, self.old_hora3, self.old_lugar, fecha_edit.get(), hora1_edit.get(), hora2_edit.get(), hora3_edit.get(), lugar_edit.get())).grid(row=5, column=0)

        button_edit = Button(self.ventana_modificar, text="Actualizar", command=lambda: self.update2(hora1_edit.get(), hora2_edit.get(), hora3_edit))
        button_edit.grid(row=5, column=1, padx=25)

        self.registro = self.treev.focus()
        self.campos = self.treev.item(self.registro, 'values')
        self.old_fecha = self.campos[0]
        self.old_hora1 = self.campos[1]
        self.old_hora2 = self.campos[2]
        self.old_hora3 = self.campos[3]
        self.old_lugar = self.campos[4]

    def edit_reg(self, old_fecha, old_hora1, old_hora2, old_hora3, old_lugar, fecha_edit, hora1_edit, hora2_edit, hora3_edit, lugar_edit):
        cone = sqlite3.connect("db1.db")
        cursor = cone.cursor()
        cursor.execute("UPDATE registros SET fecha=?, hora1=?, hora2=?, hora3=?, lugar=? WHERE fecha=? and hora1=? and hora2=? and hora3=? and lugar=?", (fecha_edit, hora1_edit, hora2_edit, hora3_edit, lugar_edit, old_fecha, old_hora1, old_hora2, old_hora3,old_lugar))
        cone.commit()
        cone.close()
        self.treev.delete(self.registro)
        self.treev.insert("","end", text="", values=(fecha_edit, hora1_edit, hora2_edit, hora3_edit, lugar_edit))
        self.ventana_modificar.destroy()

    def update2(self, hora1, hora2, hora3_edit):
        hora = Registro()
        horas_trabajadas = hora.calculo_horas(hora1, hora2)
        hora3_edit.config(state="normal")
        hora3_edit.delete(0, END)
        hora3_edit.insert(END, horas_trabajadas)
        hora3_edit.config(state="readonly")

        """self.ventana_modificar = Toplevel()
        self.ventana_modificar.title("Ventana de modificar")
        Label(self.ventana_modificar, text="Fecha").grid(row=0, column=0)
        
        fecha_edit = Entry(self.ventana_modificar)
        fecha_edit.grid(row=0, column=1, padx=5, pady=10)

        Label(self.ventana_modificar, text="Hora Entrada").grid(row=1, column=0)
        hora1_edit = Entry(self.ventana_modificar)
        hora1_edit.grid(row=1, column=1, padx=5, pady=10)

        Label(self.ventana_modificar, text="Hora Salida").grid(row=2, column=0)
        hora2_edit = Entry(self.ventana_modificar)
        hora2_edit.grid(row=2, column=1, padx=5, pady=10)


        Label(self.ventana_modificar, text="Horas Trabajadas").grid(row=3, column=0)
        hora3_edit = Entry(self.ventana_modificar, textvariable= StringVar(self.ventana_modificar, value=""), state="readonly")
        # hora3_edit = Entry(self.ventana_modificar)
        hora3_edit.grid(row=3, column=1, padx=5, pady=10)

        Label(self.ventana_modificar, text="Lugar").grid(row=4, column=0)
        lugar_edit = Entry(self.ventana_modificar)
        lugar_edit.grid(row=4, column=1, padx=5, pady=10)

        Button(self.ventana_modificar, text="Modificar", command= lambda: self.edit_reg(self.old_fecha , self.old_hora1, self.old_hora2, self.old_hora3,self.old_lugar,fecha_edit.get(), hora1_edit.get(), hora2_edit.get(), self.hora3_edit, lugar_edit.get())).grid( row= 5, column=0) 

        button_edit = Button(self.ventana_modificar, text="Actualizar", command=lambda: self.update2(hora1_edit.get(), hora2_edit.get()))
        button_edit.grid(row=5, column=1, padx= 25 )

        self.registro = self.treev.focus() #tengo que verificar si necesito esto :v 
        self.campos = self.treev.item(self.registro, 'values')
        self.old_fecha = self.campos[0]
        self.old_hora1 = self.campos[1]
        self.old_hora2 = self.campos[2]
        self.old_hora3 = self.campos[3]
        self.old_lugar = self.campos[4]    

        
    def update2 (self,hora1,hora2):
        time3 = Registro()
        hora3 = time3.calculo_horas(hora1,hora2)
        self.hora3_edit.config(textvariable= StringVar(self.labelframe1, value =hora3))
        self.hora3_edit.insert(END,self.hora3)
        self.hora3_edit.grid(row=3, column=1, padx=5, pady=10)

    def edit_reg(self, old_fecha, old_hora1 ,old_hora2 ,old_hora3 ,old_lugar, fecha_edit, hora1_edit, hora2_edit, hora3_edit, lugar_edit ):
        #     pass
        if self.clic != None:
            # id = self.conex.identificar(old_fecha, old_hora1, old_hora2 ,old_hora3 ,old_lugar)
            self.conex.edit(old_fecha, old_hora1 ,old_hora2 ,old_hora3 ,old_lugar, fecha_edit, hora1_edit, hora2_edit, hora3_edit, lugar_edit)
            self.treev.delete(self.registro)
            self.treev.insert("","end", text="", values=(fecha_edit, hora1_edit, hora2_edit, hora3_edit, lugar_edit))
        self.ventana_modificar.destroy()"""



    def borrar(self):
        self.registro = self.treev.focus()
        self.campos = self.treev.item(self.registro, 'values')

        if self.registro !=0:
            id =self.conex.identificar(self.campos[0], self.campos[1], self.campos[2], self.campos[3], self.campos[4])
            self.conex.borrar(id)
            self.treev.delete(self.registro)
            print("registro borrado")
        else:
            print("Ta vacio")

    def clic(self, event):
        self.registro = self.treev.focus()
        self.campos = self.treev.item(self.registro, 'values')

        self.entryfecha.delete(0,'end')
        self.entryhora1.delete(0,'end')
        self.entryhora2.delete(0,'end')
        self.entryhora3.delete(0,'end')
        self.entrylugar.delete(0,'end')

        self.entryfecha.insert(END,self.campos[0])
        self.entryhora1.insert(END,self.campos[1])
        self.entryhora2.insert(END,self.campos[2])
        self.entryhora3.insert(END,self.campos[3])
        self.entrylugar.insert(END,self.campos[4])


if __name__ =='__main__':
    app = Mainwindow()