from datetime import datetime, timedelta

class Registro:
    #creo que ya no sirve toca chequear 

    # def agregar(self, fecha,hora_e,hora_s, lugar):
    #     registro = [fecha,hora_e,hora_s,lugar]
    #     hora_t = self.calculo_horas(hora_e,hora_s)
    #     registro.insert(3,hora_t)

    #     return registro


    def calculo_horas(self, hora_e, hora_s):
        if hora_e and hora_s:
            hora_e = datetime.strptime(hora_e, "%H:%M") 
            hora_s = datetime.strptime(hora_s, "%H:%M") 
            tdelta = hora_s - hora_e
            horas_t = tdelta.total_seconds()/3600
            # horas_t = str(horas_t)
            return horas_t    
        else:
            return 0;


# f="24-05-2020"
# h1="08:46"
# h2="14:27"
# l="odontoleon"

# hora = Registro()
# tiempo3 = hora.calculo_horas(h1,h2)

# print(tiempo3)