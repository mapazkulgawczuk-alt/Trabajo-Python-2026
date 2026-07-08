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
            def pedir_fecha(mensaje):
    """
    Solicita una fecha en formato DD/MM/AAAA.
    Valida formato, y rangos de día, mes y año.
    Retorna la fecha como string validado.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("  [!] La fecha no puede estar vacía.")
            continue
        partes = entrada.split("/")
        if len(partes) != 3:
            print("  [!] Formato incorrecto. Use DD/MM/AAAA  (ejemplo: 15/07/2025)")
            continue
        dia_str, mes_str, anio_str = partes
        # Validar que sean dígitos
        if not (dia_str.isdigit() and mes_str.isdigit() and anio_str.isdigit()):
            print("  [!] Día, mes y año deben ser valores numéricos.")
            continue
        dia, mes, anio = int(dia_str), int(mes_str), int(anio_str)
        # Validar rangos
        if not (1 <= dia <= 31):
            print("  [!] El día debe estar entre 01 y 31.")
            continue
        if not (1 <= mes <= 12):
            print("  [!] El mes debe estar entre 01 y 12.")
            continue
        if len(anio_str) != 4:
            print("  [!] El año debe tener exactamente 4 dígitos.")
            continue
        return entrada                           # Fecha válida


def pedir_hora(mensaje):
    """
    Solicita una hora en formato HH:MM.
    Valida formato y rangos (0-23 para hora, 0-59 para minutos).
    Retorna la hora como string validado.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("  [!] La hora no puede estar vacía.")
            continue
        partes = entrada.split(":")
        if len(partes) != 2:
            print("  [!] Formato incorrecto. Use HH:MM  (ejemplo: 09:30)")
            continue
        hora_str, min_str = partes
        if not (hora_str.isdigit() and min_str.isdigit()):
            print("  [!] Los valores de hora y minutos deben ser numéricos.")
            continue
        hora, minuto = int(hora_str), int(min_str)
        if not (0 <= hora <= 23):
            print("  [!] La hora debe estar entre 00 y 23.")
            continue
        if not (0 <= minuto <= 59):
            print("  [!] Los minutos deben estar entre 00 y 59.")
            continue
        return entrada


def pedir_estado_turno(mensaje):
    """
    Solicita el estado de un turno.
    Solo acepta los valores: pendiente, atendido, cancelado.
    Retorna el estado en minúsculas.
    """
    estados_validos = ["pendiente", "atendido", "cancelado"]
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada in estados_validos:          # Validación con lista de valores permitidos
            return entrada
        else:
            print("  [!] Estado inválido. Opciones válidas: pendiente / atendido / cancelado")


# ============================================================
#  FUNCIONES DE MASCOTAS
# ============================================================

def registrar_mascota():
    """
    Crea un nuevo registro (diccionario) de mascota con todos sus campos
    y lo agrega al archivo simulado (lista mascotas[]).
    Usa el contador global para asignar un ID único.
    """
    global contador_id_mascota

    encabezado("REGISTRAR NUEVA MASCOTA")

    # Se construye el registro como un diccionario
    # Cada clave es un campo del registro
    registro = {
        "id_mascota":    contador_id_mascota,
        "nombre":        pedir_texto("  Nombre de la mascota        : "),
        "especie":       pedir_texto("  Especie (perro, gato, etc.) : "),
        "raza":          pedir_texto("  Raza                        : "),
        "edad":          pedir_entero_positivo("  Edad en años               : "),
        "nombre_duenio": pedir_texto("  Nombre del dueño            : "),
        "telefono":      pedir_texto("  Teléfono del dueño          : "),
    }

    mascotas.append(registro)         # Se agrega el registro al archivo
    contador_id_mascota += 1          # Se incrementa el contador (acumulador de IDs)

    print(f"\n  [OK] Mascota registrada exitosamente con ID #{registro['id_mascota']}.")
    pausar()

            if numero < 0:
                print("  [!] El importe no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("  [!] Valor inválido. Ejemplo correcto: 1500.50")
