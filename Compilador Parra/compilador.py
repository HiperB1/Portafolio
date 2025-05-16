import random

class Tokens:
    def __init__(self, ruta):
        #DECLARACION DE VARIABLES
        self.ruta = ruta 
        self.clase = "" #AQUI SE GUARDARA LA CLASE INGRESADA POR EL USUARIO
        self.nombre = "" #AQUI SE GUARDARA EL NOMBRE INGRESADO POR EL USUARIO
        self.tipo_error = ""
        self.clases_validas = ["GUERRERO","MAGO","ARQUERO"] #AQUI SE GUARDAN LAS CLASES VALIDAS PARA SU PROXIMA VERIFICACION
        self.claves_validas = ["CLASE","NOMBRE","PERSONAJE"] #AQUI SE GUARDAN LAS PALABRAS CLAVES PARA SU PROXIMA VERIFICACION
        self.error = False #BOLEEANOS PARA VERIFICACION DE ERRORES
        self.clase_valida = False
        self.claves_validas_c = False
        self.contador_clase = 0
        self.contador_nombre = 0
        self.contador_personaje = 0
     


    def Clasificacion(self):#METODO PARA CLASIFICACION LEXICA Y SINTACTICA
        archivo = open(self.ruta, 'r')#ABRIR EL ARCHIVO EN MODO LECTURA
        contenido = archivo.read()#LEER EL CONTENIDO DEL ARCHIVO
        contenido_separado = contenido.strip().split("\n")#sEPARAR EL CONTENIDO DEL ARCHIVO EN LINEAS 

        for i in range(len(contenido_separado)):#CICLO PARA RECORRER CADA LINEA
            



            linea_actual = contenido_separado[i].strip().split(":")#SEPARACION DE LA LINEA ACTUAL EN CARACTERES INDIVIDUALES

            for b in range(len(linea_actual)): #VERIFICACION DE SINTAXIS 

                if linea_actual[0] == "CLASE":#VERIFICACION DE QUE NO SE REPITAN CLAVES
                    self.contador_clase = self.contador_clase + 1
                if linea_actual[0] == "NOMBRE":
                    self.contador_nombre = self.contador_nombre + 1
                if linea_actual[0] == "PERSONAJE":
                    self.contador_personaje = self.contador_personaje + 1
                if linea_actual[0] == "CLASE" or linea_actual[0] == "NOMBRE" or linea_actual[0] == "PERSONAJE":
                    self.claves_validas_c = True
                else:
                    print(f"ERROR EN LA LINEA {i+1}")
                    exit()

                
                
                



            for j in range(len(linea_actual)):#CICLO PARA RECORRER CADA ELEMENTO DE CADA LINEA
                
                if linea_actual[j] == 'NOMBRE':#VERIFICAR SI EN LA LINEA ACTUAL ESTA EL COMANDO CLAVE NOMBRE
                    self.nombre = linea_actual[j+1]
                if linea_actual[j] == "CLASE":#VERIFICAR SI EN LA LINEA ACTUAL ESTA EL COMANDO CLAVE CLASE
                    self.clase = linea_actual[j+1].strip().upper()

                    for h in range(len(self.clases_validas)):
                        if self.clase == self.clases_validas[h]:
                            self.clase_valida = True
                            
                    if self.clase_valida == False:
                        self.error = True
                        self.tipo_error = "CLASE NO VALIDA"

        if self.error == True:#SI DIO UN ERROR DECIR EL TIPO Y TERMINAR LA EJECUCION
            print(f"ERROR: {self.tipo_error}")
            exit()
        if self.contador_clase > 2:
            print(f"ERROR EN LA LINEA {i+1} CLAVE REPETIDA CLASE")
            exit()
        if self.contador_nombre > 2:
            print(f"ERROR EN LA LINEA {i+1} CLAVE REPETIDA NOMBRE")      
            exit()         
        if self.contador_personaje > 2:
            print(f"ERROR EN LA LINEA {i+1} CLAVE REPETIDA PERSONAJE")
            exit()

                    
        
        print(f"NOMBRE: {self.nombre} Y CLASE: {self.clase}")#IMPRIMIR EL NOMBRE Y CLASE DEL PERSONAJE

    def Show_Info(self):#METODO PARA MOSTRAR INFORMACION SEGUN LA CLASE INGRESADA POR EL USUARIO
        if self.clase == "GUERRERO":#LLAMADA A CADA CLASE SEGUN LA CLASE INGRESADA POR EL USUARIO APLICACIONDO COMPOSICION DEL TEMA POO
            guerrero = Guerrero()
            guerrero.Mostrar_info()
        if self.clase == "MAGO":
            mago = Mago()
            mago.Mostrar_info()
        if self.clase == "ARQUERO":
            arquero = Arquero()
            arquero.Mostrar_info()
        
    def Output(self):
        archivo_output = open("output.txt", 'w')
        archivo_output.write("PERSONAJE")
        archivo_output.write(f"\nNOMBRE={self.nombre}")
        archivo_output.write(f"\nCLASE={self.clase}")
        if self.clase == "GUERRERO":
            guerrero = Guerrero()
            archivo_output.write(f"\nVIDA={guerrero.vida}")
            archivo_output.write(f"\nINTELIGENCIA={guerrero.inteligencia}")
            archivo_output.write(f"\nRABIA={guerrero.rabia}")
            archivo_output.write(f"\nVIDA={guerrero.vida}")
            archivo_output.write(f"\nINVENTARIO={guerrero.inventario[0]}-{guerrero.inventario[1]}-{guerrero.inventario[2]}")
        if self.clase == "MAGO":
            mago = Mago()
            archivo_output.write(f"\nVIDA={mago.vida}")
            archivo_output.write(f"\nINTELIGENCIA={mago.inteligencia}")
            archivo_output.write(f"\nMANA={mago.mana}")
            archivo_output.write(f"\nVIDA={mago.vida}")
            archivo_output.write(f"\nINVENTARIO={mago.inventario[0]}-{mago.inventario[1]}-{mago.inventario[2]}")
        if self.clase == "ARQUERO":
            arquero = Arquero()
            archivo_output.write(f"\nVIDA={arquero.vida}")
            archivo_output.write(f"\nINTELIGENCIA={arquero.inteligencia}")
            archivo_output.write(f"\nPRESICION={arquero.presicion}")
            archivo_output.write(f"\nVELOCIDAD={arquero.velocidad}")
            archivo_output.write(f"\nVIDA={arquero.vida}")
            archivo_output.write(f"\nINVENTARIO={arquero.inventario[0]}-{arquero.inventario[1]}-{arquero.inventario[2]}")
            
        
   


        


class Guerrero:#CLASE GUERRERO 
    def __init__(self):#INICIALIZACION DE LA CLASE CON SUS PROPIEDADES UNICAS
        self.vida = 100
        self.inteligencia = random.randint(1,100)
        self.rabia = random.randint(1,10)
        self.inventario = ["Espada", "Escudo", "Pocion De Vida"]#INVENTARIO CON ITEMS UNICOS DE CADA CLASE
    
    def Mostrar_info(self):#METODO MOSTRAR INFO PARA CADA CLASE CON SUS RESPECTIVOS CAMBIOS ADAPATADOS A DICHAS CLASES
        print(f"TU GUERRERO TIENE:\nVIDA:{self.vida}\nINTELIGENCIA:{self.inteligencia}\nRABIA:{self.rabia}\nSALUD:{self.vida}\nINVENTARIO:")
        for i in range(len(self.inventario)):
            print(f"-{self.inventario[i]}")



class Mago:#CLASE MAGO
    def __init__(self):#INICIALIZACION DE LA CLASE CON SUS PROPIEDADES UNICAS
        self.vida = 100
        self.inteligencia = random.randint(1,100)
        self.mana = 100
        self.inventario = ["Baston Magico", "Libro Hechizos", "Pocion De Mana"]#INVENTARIO CON ITEMS UNICOS DE CADA CLASE

    def Mostrar_info(self):
        print(f"TU MAGO TIENE:\nVIDA:{self.vida}\nINTELIGENCIA:{self.inteligencia}\nMANA:{self.mana}\nSALUD:{self.vida}\nINVENTARIO:")
        for i in range(len(self.inventario)):
            print(f"-{self.inventario[i]}")

    
class Arquero:#CLASE ARQUERO
    def __init__(self):#INICIALIZACION DE LA CLASE CON SUS PROPIEDADES UNICAS
        self.vida = 100
        self.inteligencia = random.randint(1,100)
        self.presicion = random.randint(1,10)
        self.velocidad = random.randint(1,100)
        self.inventario = ["Arco", "Daga", "Pocion De Resistencia"]#INVENTARIO CON ITEMS UNICOS DE CADA CLASE

    def Mostrar_info(self):
        print(f"TU ARQUERO TIENE:\nVIDA:{self.vida}\nINTELIGENCIA:{self.inteligencia}\nPRESICION:{self.presicion}\nVELOCIDAD:{self.velocidad}\nSALUD:{self.vida}\nINVENTARIO:")
        for i in range(len(self.inventario)):
            print(f"-{self.inventario[i]}")



        






                        





    





        

token = Tokens(r"input.txt")

token.Clasificacion()
token.Show_Info()
token.Output()








