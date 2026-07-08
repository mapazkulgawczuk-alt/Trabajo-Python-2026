# -*- coding: utf-8 -*-
# ============================================================
# SISTEMA DE GESTIÓN DE VETERINARIA
# Trabajo Final Integrador - Algoritmos y Estructuras de Datos
# Escenario 14: Gestión de Veterinaria
# ============================================================
#
# TEORÍA DE REGISTROS Y ARCHIVOS:
#   - Un ARCHIVO es una colección de registros  → representado por una LISTA
#   - Un REGISTRO es un conjunto de campos      → representado por un DICCIONARIO
#   - Un CAMPO es cada dato dentro del registro → representado por una CLAVE del diccionario
#
# Este programa usa tres "archivos" simulados:
#   mascotas[]   → archivo de mascotas
#   turnos[]     → archivo de turnos
#   atenciones[] → archivo de atenciones médicas
#
# INSTRUCCIONES PARA EL EMULADOR:
#   - Compatible con Python 3.6 o superior
#   - Ejecutar directamente: el programa arranca en main()
#   - Usar emuladores con soporte de input() interactivo:
#     Repl.it | OnlineGDB | PythonAnywhere | Programiz
# ============================================================



# -----------------------------------------------
# ARCHIVOS SIMULADOS (listas de registros)
# -----------------------------------------------
mascotas    = []   # Cada elemento es un registro (diccionario) de mascota
turnos      = []   # Cada elemento es un registro (diccionario) de turno
atenciones  = []   # Cada elemento es un registro (diccionario) de atención médica

# -----------------------------------------------
# CONTADORES GLOBALES DE ID
# Se incrementan cada vez que se agrega un registro
# -----------------------------------------------
contador_id_mascota    = 1
contador_id_turno      = 1
contador_id_atencion   = 1


# ============================================================
#  FUNCIONES AUXILIARES DE INTERFAZ
# ============================================================

def separador():
    """Imprime una línea visual para separar secciones."""
    print("=" * 57)

def separador_simple():
    """Imprime una línea delgada para separar registros."""
    print("-" * 57)

def pausar():
    """Detiene la ejecución hasta que el usuario presione Enter."""
    input("\n  Presione Enter para continuar...")

def encabezado(titulo):
    """Imprime un encabezado formateado para cada sección."""
    print()
    separador()
    print(f"   {titulo}")
    separador()


# ============================================================
#  FUNCIONES DE VALIDACIÓN
#  Cada función valida un tipo de dato y repite el pedido
#  hasta recibir un valor correcto (estructura repetitiva).
# ============================================================

def pedir_texto(mensaje):
    """
    Solicita un texto no vacío.
    Valida que el usuario no deje el campo en blanco.
    Retorna el texto ingresado sin espacios extra.
    """
    while True:                                  # Estructura repetitiva
        valor = input(mensaje).strip()
        if valor == "":
            print("  [!] Este campo no puede estar vacío. Intente nuevamente.")
        else:
            return valor                         # Retorna solo si es válido


def pedir_entero_positivo(mensaje):
    """
    Solicita un número entero mayor a cero.
    Valida que sea numérico y positivo.
    Retorna el entero validado.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("  [!] Este campo no puede estar vacío.")
            continue
        try:
            numero = int(entrada)               # Puede lanzar ValueError
            if numero <= 0:
                print("  [!] Debe ingresar un número entero mayor a cero.")
            else:
                return numero
        except ValueError:                      # Manejo de error: no es número
            print("  [!] Valor inválido. Ingrese solo números enteros.")


def pedir_decimal_no_negativo(mensaje):
    """
    Solicita un número decimal mayor o igual a cero (importe).
    Valida que sea numérico y no negativo.
    Retorna el float validado.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("  [!] Este campo no puede estar vacío.")
            continue
        try:
            numero = float(entrada)
            if numero < 0:
                print("  [!] El importe no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("  [!] Valor inválido. Ejemplo correcto: 1500.50")
