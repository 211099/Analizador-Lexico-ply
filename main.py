import tkinter as tk
import ply.lex as lex

reserved = {
   'for' : 'FOR',
   'do' : 'DO',
   'while' : 'WHILE',
   'if' : 'IF',
   'else' : 'ELSE',
}

tokens = ['ParentecisA','ParentecisC',] + list(reserved.values())

# Regular expression rules for simple tokens

t_FOR   = r'\bfor\b'
t_DO   = r'\bdo\b'
t_WHILE   = r'\bwhile\b'
t_IF   = r'\bif\b'
t_ELSE   = r'\belse\b'
t_ParentecisA  = r'\('
t_ParentecisC  = r'\)'
t_ignore  = ' \t'

# se define una regla para detectar las lineas 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# detecta elementos que no son los tokens
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    text_output.insert(tk.END, "Illegal character '%s'" % t.value[0]  + "\n")
    t.lexer.skip(1)


# Crear la ventana principal
root = tk.Tk()
root.geometry("800x600")
root.configure(bg="#303030") 

# Crear los widgets
label_input = tk.Label(root, text="Ingresa los datos:", fg="white", bg="#303030",font=("Arial", 16))
label_input.grid(row=0, column=0, pady=50, padx=50)

text_output_into = tk.Text(root, width=20, height=10, bg="white", fg="black")
text_output_into.grid(row=1, column=0, pady=10, padx=20)

text_output = tk.Text(root, width=50, height=10, bg="white", fg="black")
text_output.grid(row=1, column=1, pady=10, padx=50)

button = tk.Button(root, text="Obtener datos", bg="#00FF00", fg="black",font=("Arial", 10))
button.grid(row=2, column=0, pady=50)

clear_button = tk.Button(root, text="Limpiar cuadro de texto", bg="#FF0000", fg="black",font=("Arial", 10))
clear_button.grid(row=2, column=1, pady=50, padx=10)

def limpiar_texto():
    text_output.delete("1.0", tk.END)


def obtener_datos():
    lexer = lex.lex()
    resultados = text_output_into.get("1.0", "end-1c") 

    data = resultados

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break      
        text_output.insert(tk.END, str(tok) + "\n")
  
    

button.config(command=obtener_datos)
clear_button.config(command=limpiar_texto)

root.mainloop()