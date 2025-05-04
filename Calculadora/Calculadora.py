from tkinter import *


g = 0
pos = []

def atualizar_display(numero):
    global g
    
    #the conditional is for verification if have numbers on the screen 0 = False and 1 = True
    if g == 0:
        display_var.set(display_var.get() + str(numero))
    if g == 1:
        limpar_display()
        display_var.set(display_var.get() + str(numero))
        g = 0
    if str(numero) == 'x':
        a = str(numero).replace('x','*')
        lista.append(a)
    else:
        lista.append(str(numero))

    

    
def limpar_display():
    display_var.set('')
    lista.clear()


def calculo():
    global g
    global pos


    #verify if the first number is a 0 
    if lista[0] == '0':
        lista.remove('0')
    #else is going add the index of the signals in the list
    else:
        pos = [(i,palavra) for i, palavra in enumerate(lista) if palavra == '+' or palavra == '-' or palavra == '*' or palavra == '/']

    
    #lista de indexs de zeros após o sinal
    index_zero = []
    for a in pos:
       #numero após o sinal
        h = a[0] + 1
        #se o ultimo da lista for um zero
        if lista[-1] == '0':
            pass
        #se o ultimo da lista for um operador
        elif lista[-1] == a[1]:
            lista.append('0')
        #se após o sinal o número é zero
        elif lista[h] == '0':
            print('AQUI TEM UM ZERO')
            index_zero.append(h)
    
    #lista final após os tratamentos
    lista_final = [item for i,item in enumerate(lista) if i not in index_zero]
    print(lista_final)


    
    a = ''.join(lista_final)
    resultado = eval(a)
    print(resultado)
    limpar_display()
    if resultado == int(resultado):
        atualizar_display(int(resultado))
    else:
        atualizar_display(resultado)
    g = 1
    lista.clear()


root = Tk()

lista = []

larg_janela = 350
altura_janela = 500

larg_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = (larg_tela // 2) - (larg_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

root.configure(bg='white')
root.title("Calculadora")
root.geometry(f'{larg_janela}x{altura_janela}+{pos_x}+{pos_y}')
root.resizable(True,True)
root.minsize(width=350,height=500)
root.maxsize(width=350,height=500)

display_var = StringVar()

frame_display = Frame(root)
frame_display.pack(pady=5)

display = Label(frame_display,textvariable=display_var,font=('Arial',24),bg='white', anchor='e',relief='solid',width=15,height=2)
display.pack()

frame_botoes = Frame(root)
frame_botoes.config(bg='white')
frame_botoes.pack()

botoes = [
    (1,0,0), (2,0,1), (3,0,2), ('+',0,3),
    (4,1,0), (5,1,1), (6,1,2), ('-',1,3),
    (7,2,0), (8,2,1), (9,2,2), ('x',2,3),
    (0,3,1), ('/',3,3)
]

for n,l,c in botoes:
    botao = Button(frame_botoes,text=str(n),font=('Arial',18),command=lambda n=n:atualizar_display(n), width=5,height=2,bd=1)
    botao.grid(row=l,column=c,padx=5,pady=5)


botao_igual = Button(frame_botoes,text='=',font=('Arial',18),command=calculo,bd=1,width=5,height=2)
botao_igual.grid(row=3,column=2,padx=5,pady=5)

botao_limpar = Button(frame_botoes, text='C', font=('Arial',18),command=limpar_display,bd=1,width=5,height=2)
botao_limpar.grid(row=3,column=0,padx=5,pady=5)


root.mainloop()