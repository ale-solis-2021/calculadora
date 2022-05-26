from tkinter import *

ventana=Tk() #va a contener la interfaz grafica

#para hacer funcionar los botones de +,/,-,**,etc
def btnClik(num):
	global operador #significa que la variable es accesible desde cualquier lugar del programa.
	operador=operador+str(num)
	input_text.set(operador)

def resultado():
	global operador
	try:
	    oper=str(eval(operador))#sirve para realizar algunas op
	    input_text.set(oper)
	except:
		input_text.set("Error")
	operador="" #sirve para seguir operando


    
input_text=StringVar()
operador=""

#Agregar formato a la ventana
ventana.title("CALCULADORA OP BÀSICA")
ventana.configure(background="SlateBlue1")


#Esta variable va a contener el formato de los botones
anchoBoton=8 #unidad de pantalla pixeles
altoBoton=3
colorBoton=("#33FFF1")
color2=("#20B2AA")

#para agregar elemento en la ventana                                                #para que escriba de derecha izquiera 
displey=Entry(ventana, font=("arial", 20, "bold"), bd=15, insertwidth=4, bg="LightPink", justify="right", textvariable=input_text)
displey.grid(row=0, column=0, columnspan=5)

#crear los botones con numeros
                                                                           #para que funciones el al apretar los num.                    
Button(ventana, text=9, bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(9)).grid(row=1, column=0)
Button(ventana, text=8 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(8)).grid(row=1, column=1)
Button(ventana, text=7 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(7)).grid(row=1, column=2)

Button(ventana, text=4 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(4)).grid(row=2, column=0)
Button(ventana, text=5 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(5)).grid(row=2, column=1)
Button(ventana, text=6 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(6)).grid(row=2, column=2)


Button(ventana, text=3 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(3)).grid(row=3, column=0)
Button(ventana, text=2 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(2)).grid(row=3, column=1)
Button(ventana, text=1 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(1)).grid(row=3, column=2)

Button(ventana, text="." , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(".")).grid(row=4, column=0)
Button(ventana, text=0 , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:btnClik(0)).grid(row=4, column=1)
Button(ventana, text="=" , bg=colorBoton, width=anchoBoton, height=altoBoton, command=lambda:resultado()).grid(row=4, column=2)



#agregamos los botones con operadores:
Button(ventana, text="^" , bg=color2, width=anchoBoton, height=altoBoton, command=lambda:btnClik("**")).grid(row=1, column=3)
Button(ventana, text="AC" , bg=color2, width=anchoBoton, height=altoBoton).grid(row=1, column=4)

Button(ventana, text="+" ,bg=color2 , width=anchoBoton, height=altoBoton, command=lambda:btnClik("+")).grid(row=2, column=3)
Button(ventana, text="-" , bg=color2, width=anchoBoton, height=altoBoton, command=lambda:btnClik("-")).grid(row=2, column=4)

Button(ventana, text="*" , bg=color2, width=anchoBoton, height=altoBoton, command=lambda:btnClik("*")).grid(row=3, column=3)
Button(ventana, text="/" , bg=color2, width=anchoBoton, height=altoBoton, command=lambda:btnClik("/")).grid(row=3, column=4)


ventana.mainloop() #bucle que me va a controlar mis acciones


