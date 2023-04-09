from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65, 2.02, 4.9]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58, 3.19, 1.67]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74, 2.34, 5.05]



def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revizar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1


    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0,END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantida in texto_comida:
        sub_total_comida += (float(cantida.get()) *precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantida in texto_bebida:
        sub_total_bebida += (float(cantida.get()) *precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantida in texto_postre:
        sub_total_postre += (float(cantida.get()) *precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.19
    total = sub_total + impuestos

    var_costo_comida.set(f'${round(sub_total_comida,2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida,2)}')
    var_costo_postre.set(f'${round(sub_total_postre,2)}')
    var_subtotal.set(f'${round(sub_total,2)}')
    var_impuesto.set(f'${round(impuestos,2)}')
    var_total.set(f'${round(total,2)}')


def recibo():
    text_recibo.delete(1.0,END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    text_recibo.insert(END, f'Datos: \t{num_recibo}\t\n\t{fecha_recibo}''\n')
    text_recibo.insert(END, f'*'*42 + '\n')
    text_recibo.insert(END, 'Items.\t\tCant.\tCosto.\n')
    text_recibo.insert(END, f'-'*48 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            text_recibo.insert(END, f'{lista_comidas[x]}\t\t'
                                f'{comida.get()}\t${int(comida.get())*precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            text_recibo.insert(END, f'{lista_bebidas[x]}\t\t'
                                f'{bebida.get()}\t${int(bebida.get())*precios_bebida[x]}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            text_recibo.insert(END, f'{lista_postres[x]}\t\t'
                                f'{postre.get()}\t${int(postre.get())*precios_postres[x]}\n')
        x += 1

    text_recibo.insert(END, f'-'*48 + '\n')
    text_recibo.insert(END, f'Costo Comida\t\t{var_costo_comida.get()}\n')
    text_recibo.insert(END, f'Costo Bebida\t\t{var_costo_bebida.get()}\n')
    text_recibo.insert(END, f'Costo Postre\t\t{var_costo_postre.get()}\n')

    text_recibo.insert(END, f'-'*48 + '\n')
    text_recibo.insert(END, f'Sub-total\t\t{var_subtotal.get()}\n')
    text_recibo.insert(END, f'Impuesto\t\t{var_impuesto.get()}\n')
    text_recibo.insert(END, f'Total\t\t{var_total.get()}\n')

    text_recibo.insert(END, f'*'*42 + '\n')
    text_recibo.insert(END, f'*'*9+ f'Gracias por Comprar'+ f'*'*10)


def guardar():
    infor_recibo = text_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt') #pide guardar como un archivo
    archivo.write(infor_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo se Guardo')


def limpiar():
    text_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')




#iniciar tkinter
app = Tk()

#tamaño de la ventana
app.geometry('1090x580')

#evitar maximizar
app.resizable(0,0)

#title
app.title('Super Restaurante - Modulo Facturacions')
#fondo
app.config(bg='#313628')

#panel superior
panel_superior = Frame(app, bd=0, relief=FLAT) #el grosor del borde y el tipo de visualizacion
panel_superior.pack(side=TOP) #arroja a la ventana y donde se ubicara
#etiueta titulo
etiqueta_titulo = Label(panel_superior
                        , text='Modulo de Facturacion'
                        , fg='#cadf9e', font=('Dosis',38)
                        , bg='#000', width=32)
etiqueta_titulo.grid(row=0, column=0)#ubicacion de mi panel



#panel izquierdo
panel_izquiedo = Frame(app, bd=1, relief=FLAT)
panel_izquiedo.pack(side=LEFT)

#panel costos
panel_costo = Frame(panel_izquiedo, bd=1, relief=FLAT, bg="#000", padx=2)
panel_costo.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquiedo, text='comidas'
                            , font=('Dosis', 20, 'bold')
                            , bd=10, relief=FLAT
                            , fg='#a4ac96', bg='#313628') #panel de etiquete incorporada
panel_comidas.pack(side=LEFT)

#panel de bebidas
panel_bebidas = LabelFrame(panel_izquiedo, text='Bebidas'
                            , font=('Dosis', 20, 'bold')
                            , bd=10, relief=FLAT
                            , fg='#a4ac96', bg='#313628') #panel de etiquete incorporada
panel_bebidas.pack(side=LEFT)


#panel de postres
panel_postres = LabelFrame(panel_izquiedo, text='Postres'
                            , font=('Dosis', 20, 'bold')
                            , bd=10, relief=FLAT
                            , fg='#a4ac96', bg='#313628', ) #panel de etiquete incorporada
panel_postres.pack(side=LEFT)



#panel derecha
panel_derecha = Frame(app, bd=1, relief=FLAT, bg='#313628')
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='#cadf9e')
panel_calculadora.pack()
#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='#cadf9e')
panel_recibo.pack()
#panel Botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='#cadf9e')
panel_botones.pack()


#lista de productos
lista_comidas = ['pollo', 'salmon', 'res', 'atun', 'camarones', 'hambuguesa'
                , 'perros', 'pizza', 'empanadas', 'arepas']
lista_bebidas = ['gaseosas', 'cerveza', 'jugos', 'agua', 'vino', 'de la casa'
                , 'energizante', 'tea', 'aromatica', 'cafe']
lista_postres = ['helado', 'Brownies', 'fruta', 'flan', 'pastel', 'chocolatina'
                , 'arequipe', 'pai', 'galletas', 'gomitas']


#generar variables comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:


    #check button
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas
                        , text=comida.title()
                        , font=('Dosis', 13, 'bold')
                        , onvalue=1, offvalue=0
                        , variable=variables_comida[contador]
                        , bg='#fff', fg='#000', bd=1
                        , width=11
                        , command=revizar_check)
    comida.grid(row=contador, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas
                                    , font=('Dosis', 18, 'bold')
                                    , bd=1
                                    , width=3
                                    , state=DISABLED
                                    , textvariable= texto_comida[contador])
    cuadros_comida[contador].grid(row=contador
                                , column=1)

    contador += 1
#onvalue y offvalue se le da una valor si esta o no activado esto permite la toma de deciciones


#generar variables bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas
                        , text=bebida.title()
                        , font=('Dosis', 13, 'bold')
                        , onvalue=1, offvalue=0
                        , variable=variables_bebida[contador]
                        , bg='#fff', fg='#000', bd=1
                        , width=11
                        , command=revizar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas
                                    , font=('Dosis', 18, 'bold')
                                    , bd=1
                                    , width=3
                                    , state=DISABLED
                                    , textvariable= texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador
                                , column=1)
    contador += 1



#generar variables postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres
                        , text=postre.title()
                        , font=('Dosis', 13, 'bold')
                        , onvalue=1, offvalue=0
                        , variable=variables_postre[contador]
                        , bg='#fff', fg='#000', bd=1
                        , width=11
                        , command=revizar_check)
    postre.grid(row=contador, column=0, sticky=W)

    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres
                                    , font=('Dosis', 18, 'bold')
                                    , bd=1
                                    , width=3
                                    , state=DISABLED
                                    , textvariable= texto_postre[contador])
    cuadros_postre[contador].grid(row=contador
                                , column=1)
    contador += 1


#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#etiquetas de costo comida y campos de entrada
etiqueta_costo_comida = Label(panel_costo
                        ,text='Costo Comida'
                        ,font=('Sosis', 13, 'bold')
                        ,bg="#000", fg='#cadf9e')
etiqueta_costo_comida.grid(row=0, column=0, padx=5)
text_costo_comida = Entry(panel_costo
                        , font=('dosis', 10, 'bold')
                        , bd=1, width=7
                        , state='readonly' #solo permite leer
                        , textvariable=var_costo_comida)
text_costo_comida.grid(row=0, column=1, padx=15) #ubicacion de los paneles



#etiquetas de costo bebida y campos de entrada
etiqueta_costo_bebida = Label(panel_costo
                        ,text='Costo Bebida'
                        ,font=('Sosis', 13, 'bold')
                        ,bg="#000", fg='#cadf9e')
etiqueta_costo_bebida.grid(row=0, column=2, padx=5)
text_costo_bebida = Entry(panel_costo
                        , font=('dosis', 10, 'bold')
                        , bd=1, width=7
                        , state='readonly' #solo permite leer
                        , textvariable=var_costo_bebida)
text_costo_bebida.grid(row=0, column=3, padx=5) #ubicacion de los paneles



#etiquetas de costo postre y campos de entrada
etiqueta_costo_postre = Label(panel_costo
                        ,text='Costo Postre'
                        ,font=('Sosis', 13, 'bold')
                        ,bg="#000", fg='#cadf9e')
etiqueta_costo_postre.grid(row=0, column=4, padx=14)
text_costo_postre = Entry(panel_costo
                        , font=('dosis', 10, 'bold')
                        , bd=1, width=7
                        , state='readonly' #solo permite leer
                        , textvariable=var_costo_postre)
text_costo_postre.grid(row=0, column=5, padx=6) #ubicacion de los paneles

#etiquetas de costo subtotal y campos de entrada
etiqueta_subtotal = Label(panel_costo
                        ,text='Costo subtotal'
                        ,font=('Sosis', 13, 'bold')
                        ,bg="#000", fg='#cadf9e')
etiqueta_subtotal.grid(row=1, column=0, padx=5)
text_subtotal = Entry(panel_costo
                        , font=('dosis', 10, 'bold')
                        , bd=1, width=7
                        , state='readonly' #solo permite leer
                        , textvariable=var_subtotal)
text_subtotal.grid(row=1, column=1, padx=5) #ubicacion de los paneles


#etiquetas de costo impuesto y campos de entrada
etiqueta_impuesto = Label(panel_costo
                        ,text='Costo Impuesto'
                        ,font=('Sosis', 13, 'bold')
                        ,bg="#000", fg='#cadf9e')
etiqueta_impuesto.grid(row=1, column=2, padx=5)
text_impuesto = Entry(panel_costo
                        , font=('dosis', 10, 'bold')
                        , bd=1, width=7
                        , state='readonly' #solo permite leer
                        , textvariable=var_impuesto)
text_impuesto.grid(row=1, column=3, padx=5) #ubicacion de los paneles


#etiquetas de costo total y campos de entrada
etiqueta_total = Label(panel_costo
                        ,text='Costo Total'
                        ,font=('Sosis', 13, 'bold')
                        ,bg="#000", fg='#cadf9e')
etiqueta_total.grid(row=1, column=4, padx=5)
text_total = Entry(panel_costo
                        , font=('dosis', 10, 'bold')
                        , bd=1, width=7
                        , state='readonly' #solo permite leer
                        , textvariable=var_total)
text_total.grid(row=1, column=5, padx=5) #ubicacion de los paneles


#botones
botones = ['Total', 'Recibo', 'Guardar', 'Limpiar']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones
                , text=boton.title()
                , font=('Dosis', 8, 'bold')
                , fg='#cadf9e', bg='#000', bd=1, width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=limpiar)


#recibo
text_recibo = Text(panel_recibo
                , font=('Dosis', 12, 'bold')
                , bd=1, width=31, height=12)
text_recibo.grid(row=0 ,column=0)


#calculadora
visor_calculadora = Entry(panel_calculadora
                        , font=('Dosis', 16, 'bold')
                        , bd=1, width=23)
visor_calculadora.grid(row=0, column=0,
                        columnspan=4)

botones_calculadora = ['7','8','9','+'
                    ,'4','5','6','-'
                    ,'1','2','3','x'
                    ,'Borrar', '0', '=', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora
                , text=boton.title()
                , font=('Dosis', 16, 'bold')
                , fg='#cadf9e', bg='#000',bd=1, width=4)
    botones_guardados.append(boton)
    boton.grid(row=fila
                , column=columna)
    if columna == 3:
        fila +=1

    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=borrar)
botones_guardados[13].config(command=lambda : click_boton('0'))
botones_guardados[14].config(command=obtener_resultado)
botones_guardados[15].config(command=lambda : click_boton('/'))





#evitar cerrar la pantalla
app.mainloop() #hace que la ventana este siempre a la vista