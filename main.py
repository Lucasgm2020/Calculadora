import tkinter as tk

class Interfaz:
    def __init__(self,ventana):

        self.pantalla = tk.Text(ventana,state="disabled",width=40,height=3)
        self.pantalla.grid(column=0,row=0,columnspan=4,pady=5,padx=5)
        self.operaciones = ""
        self.error_generated = False
        
        boton1 = self.crear_boton(ventana,7)
        boton2 = self.crear_boton(ventana,8)
        boton3 = self.crear_boton(ventana,9)
        boton4 = self.crear_boton(ventana,u"\u232B") #simbolo de borrar
        boton5 = self.crear_boton(ventana,4)
        boton6 = self.crear_boton(ventana,5)
        boton7 = self.crear_boton(ventana,6)
        boton8 = self.crear_boton(ventana,"/")
        boton9 = self.crear_boton(ventana,1)
        boton10 = self.crear_boton(ventana,2)
        boton11 = self.crear_boton(ventana,3)
        boton12 = self.crear_boton(ventana,"*")
        boton13 = self.crear_boton(ventana,".")
        boton14 = self.crear_boton(ventana,0)
        boton15 = self.crear_boton(ventana,"+")
        boton16 = self.crear_boton(ventana,"-")
        boton17 = self.crear_boton(ventana,"=",ancho=21)
        
        botones_numericos = [boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16]
        contador = 0
        
        for i in range(1,5):
            for j in range(4):
                botones_numericos[contador].grid(row=i,column=j)
                contador+=1
        boton17.grid(row=5,column=1,columnspan=2)
        
    def crear_boton(self,ventana,valor,ancho=9,alto=1):
        return tk.Button(ventana,text=valor,command=lambda: self.click(valor),width=ancho,height=alto,padx=1,pady=1)
   
    def click(self,valor):
        errores = ["Syntax Error","Zero Division not Allowed","Error"]
        
        try:
            
            if self.error_generated:
                self.operaciones = ""
                self.limpiar_pantalla()
                self.error_generated = False
                
            if valor == "=":
                resultado = eval(self.operaciones)
                self.limpiar_pantalla()
                self.mostrar_en_pantalla(resultado)
                
            elif valor == u"\u232B": #simbolo de borrar
                operaciones = ""
                self.limpiar_pantalla()
                
            else:
                self.operaciones+=str(valor)
                self.mostrar_en_pantalla(valor)
        
        except SyntaxError:
            self.limpiar_pantalla()
            self.mostrar_en_pantalla(errores[0])
            self.error_generated = True
            
            
        except ZeroDivisionError:            
            self.limpiar_pantalla()
            self.mostrar_en_pantalla(errores[1])    
            self.error_generated = True
            
        except:
            self.limpiar_pantalla()
            self.mostrar_en_pantalla(errores[2])
            self.error_generated = True
                    
            
    def mostrar_en_pantalla(self,texto):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(tk.END,texto)
        self.pantalla.configure(state="disabled")
     
    def limpiar_pantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0",tk.END)
        self.pantalla.configure(state="disabled")       
     
ventana = tk.Tk()
ventana.geometry("350x200")
ventana.title("Calculadora")        
app = Interfaz(ventana)
ventana.mainloop()