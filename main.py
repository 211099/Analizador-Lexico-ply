import ply.lex as lex
import re


# Definir las palabras reservadas
reserved = {
    'int': 'Reservada',
    'function': 'Reservada',
    'read': 'Reservada',
    'printf': 'Reservada',
    'program': 'Reservada'
}

# Lista de tokens
tokens = [
    'ID',
    'NUMERO',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'COLON',
    'LBRACE',
    'RBRACE',
    'Punto_coma',
    'STRING',
    'SUMA',
    'IGUAL',
] + list(reserved.values())

# Expresiones regulares para los tokens simples
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_COLON = r':'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_Punto_coma = r';'
t_SUMA = r'\+'
t_IGUAL = r'='

# Expresiones regulares con acciones para los tokens más complejos
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]*(?:\\.[^"\\]*)*)"'
    t.value = t.value[1:-1]  # Eliminar las comillas alrededor de la cadena
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \n'

# Manejo de errores
def t_error(t):
    print(f'Error: Carácter inesperado "{t.value[0]}"')
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Ejemplo de uso
def tokenize(data):
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING':
            print(f'String encontrado: {token.value}')
        else:
            print(token)

# Código de ejemplo
data = '''
function name() {
    int a, b, c;
    read a;
    printf("hola mundo");
}
'''

# Encontrar la función utilizando una expresión regular completa
def find_function(data):
    function_regex = r'program\s+\w+\s*\(\s*\)\s*{[\s\S]*?}'
    matches = re.findall(function_regex, data)
    if matches:
        for match in matches:
            print(f'Función encontrada: {match}')
    else:
        print('No se encontró ninguna función.')

# Encontrar declaraciones de variables int en el código fuente
def find_int_declarations(data):
    int_declaration_regex = r'int\s+(\w+(?:,\s*\w+)*)(?:\s*:\s*\w+)?\s*;'
    matches = re.findall(int_declaration_regex, data)
    if matches:
        for match in matches:
            print(f'Declaración de variables int encontrada: {match}')
    else:
        print('No se encontró ninguna declaración de variables int.')

# Tokenizar el código fuente e imprimir los tokens
tokenize(data)

# Encontrar la función y declaraciones de variables int en el código fuente
find_function(data)
find_int_declarations(data)


import tkinter as tk
from tkinter import ttk

# Crear ventana principal
window = tk.Tk()
window.title("Clasificación de Tokens")

# Crear tabla
table = ttk.Treeview(window, columns=("Token", "Clasificación"), show="headings")
table.heading("Token", text="Token")
table.heading("Clasificación", text="Clasificación")
table.pack(padx=10, pady=10)

# Función para clasificar los tokens
def classify_tokens():
    # Obtener el texto ingresado por el usuario
    data = text_input.get("1.0", "end").strip()

    # Limpiar la tabla
    table.delete(*table.get_children())

    # Clasificar los tokens y mostrarlos en la tabla
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        table.insert("", "end", values=(token.value, token.type))

# Etiqueta y cuadro de texto para ingresar el código fuente
label = tk.Label(window, text="Ingrese el código fuente:")
label.pack(padx=10, pady=5)

text_input = tk.Text(window, height=10, width=40)
text_input.pack(padx=10, pady=5)

# Botón para clasificar los tokens
classify_button = tk.Button(window, text="Clasificar Tokens", command=classify_tokens)
classify_button.pack(padx=10, pady=5)

# Construir el lexer
lexer = lex.lex()

# Ejecutar la interfaz gráfica
window.mainloop()