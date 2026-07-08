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
def listar_mascotas():
    """
    Recorre el archivo mascotas[] con un ciclo y muestra
    todos los registros almacenados, campo por campo.
    """
    encabezado("LISTADO DE MASCOTAS REGISTRADAS")

    if len(mascotas) == 0:            # Condicional: verificar si el archivo está vacío
        print("\n  No hay mascotas registradas en el sistema.")
    else:
        for mascota in mascotas:      # Estructura repetitiva: recorrer cada registro
            print(f"\n  ID: {mascota['id_mascota']}  |  Nombre: {mascota['nombre']}  "
                  f"|  Especie: {mascota['especie']}  |  Raza: {mascota['raza']}")
            print(f"      Edad: {mascota['edad']} año/s  |  "
                  f"Dueño: {mascota['nombre_duenio']}  |  Tel: {mascota['telefono']}")
            separador_simple()
    pausar()


def buscar_mascota_por_id():
    """
    Recorre el archivo mascotas[] buscando un registro
    cuyo campo id_mascota coincida con el ID ingresado.
    Muestra todos los campos si lo encuentra.
    """
    encabezado("BUSCAR MASCOTA POR ID")

    id_buscado = pedir_entero_positivo("  Ingrese el ID de la mascota a buscar: ")

    encontrada = False                # Bandera de control
    for mascota in mascotas:          # Estructura repetitiva: recorrer el archivo
        if mascota["id_mascota"] == id_buscado:   # Condicional: comparar el campo ID
            encontrada = True
            print(f"\n  ID Mascota   : {mascota['id_mascota']}")
            print(f"  Nombre       : {mascota['nombre']}")
            print(f"  Especie      : {mascota['especie']}")
            print(f"  Raza         : {mascota['raza']}")
            print(f"  Edad         : {mascota['edad']} año/s")
            print(f"  Dueño        : {mascota['nombre_duenio']}")
            print(f"  Teléfono     : {mascota['telefono']}")
            break                     # Se encontró: salir del ciclo

    if not encontrada:
        print(f"\n  [!] No se encontró ninguna mascota con ID #{id_buscado}.")
    pausar()


def existe_mascota(id_mascota):
    """
    Función auxiliar: verifica si existe una mascota con el ID dado.
    Retorna True si la encuentra, False si no.
    Se usa para validar referencias cruzadas entre archivos.
    """
    for mascota in mascotas:
        if mascota["id_mascota"] == id_mascota:
            return True
    return False


# ============================================================
#  FUNCIONES DE TURNOS
# ============================================================

def registrar_turno():
    """
    Crea un nuevo registro de turno y lo agrega al archivo turnos[].
    Antes de registrar, valida que exista la mascota referenciada.
    El estado inicial de todo turno es siempre 'pendiente'.
    """
    global contador_id_turno

    encabezado("REGISTRAR NUEVO TURNO")

    id_mascota = pedir_entero_positivo("  ID de la mascota: ")

    # Validación de integridad: la mascota debe existir
    if not existe_mascota(id_mascota):
        print(f"\n  [!] No existe ninguna mascota con ID #{id_mascota}.")
        print("      Registre primero la mascota antes de crear un turno.")
        pausar()
        return                        # Sale de la función sin registrar

    registro = {
        "id_turno":      contador_id_turno,
        "id_mascota":    id_mascota,
        "fecha":         pedir_fecha("  Fecha del turno (DD/MM/AAAA) : "),
        "hora":          pedir_hora( "  Hora del turno  (HH:MM)      : "),
        "tipo_consulta": pedir_texto("  Tipo de consulta (vacunación, control, cirugía, etc.): "),
        "estado":        "pendiente", # Campo con valor predeterminado
    }

    turnos.append(registro)
    contador_id_turno += 1

    print(f"\n  [OK] Turno registrado con ID #{registro['id_turno']}. Estado: PENDIENTE.")
    pausar()


def listar_turnos():
    """
    Recorre el archivo turnos[] y muestra todos los registros.
    Incluye todos los estados sin filtrar.
    """
    encabezado("LISTADO DE TURNOS")

    if len(turnos) == 0:
        print("\n  No hay turnos registrados en el sistema.")
    else:
        for turno in turnos:
            print(f"\n  ID Turno: {turno['id_turno']}  |  "
                  f"ID Mascota: {turno['id_mascota']}  |  "
                  f"Fecha: {turno['fecha']}  |  Hora: {turno['hora']}")
            print(f"      Tipo consulta: {turno['tipo_consulta']}  |  "
                  f"Estado: {turno['estado'].upper()}")
            separador_simple()
    pausar()


def actualizar_estado_turno():
    """
    Permite cambiar el campo 'estado' de un turno existente.
    Busca el turno por ID y lo modifica directamente en el archivo.
    """
    encabezado("ACTUALIZAR ESTADO DE TURNO")

    id_turno = pedir_entero_positivo("  ID del turno a actualizar: ")

    encontrado = False
    for turno in turnos:
        if turno["id_turno"] == id_turno:
            encontrado = True
            print(f"  Estado actual   : {turno['estado'].upper()}")
            nuevo_estado = pedir_estado_turno(
                "  Nuevo estado (pendiente / atendido / cancelado): "
            )
            turno["estado"] = nuevo_estado          # Se modifica el campo directamente
            print(f"\n  [OK] Estado del turno #{id_turno} actualizado a: {nuevo_estado.upper()}.")
            break

    if not encontrado:
        print(f"\n  [!] No se encontró ningún turno con ID #{id_turno}.")
    pausar()
# ============================================================
#  FUNCIONES DE ATENCIÓN MÉDICA
# ============================================================

def registrar_atencion():
    """
    Crea un nuevo registro de atención médica y lo agrega al archivo atenciones[].
    Valida que exista la mascota antes de registrar.
    El campo 'importe' se acumulará en las estadísticas.
    """
    global contador_id_atencion

    encabezado("REGISTRAR ATENCIÓN MÉDICA")

    id_mascota = pedir_entero_positivo("  ID de la mascota: ")

    if not existe_mascota(id_mascota):
        print(f"\n  [!] No existe ninguna mascota con ID #{id_mascota}.")
        print("      Registre primero la mascota.")
        pausar()
        return

    registro = {
        "id_atencion": contador_id_atencion,
        "id_mascota":  id_mascota,
        "diagnostico": pedir_texto("  Diagnóstico                     : "),
        "tratamiento": pedir_texto("  Tratamiento indicado            : "),
        "servicio":    pedir_texto("  Servicio realizado (vacunación, desparasitación, cirugía, etc.): "),
        "importe":     pedir_decimal_no_negativo("  Importe cobrado ($)             : "),
    }

    atenciones.append(registro)
    contador_id_atencion += 1

    print(f"\n  [OK] Atención médica registrada con ID #{registro['id_atencion']}.")
    pausar()


def listar_atenciones():
    """
    Recorre el archivo atenciones[] y muestra todos los registros de
    atenciones médicas almacenados, campo por campo.
    """
    encabezado("LISTADO DE ATENCIONES MÉDICAS")

    if len(atenciones) == 0:
        print("\n  No hay atenciones médicas registradas en el sistema.")
    else:
        for atencion in atenciones:
            print(f"\n  ID Atención  : {atencion['id_atencion']}  |  "
                  f"ID Mascota: {atencion['id_mascota']}")
            print(f"  Diagnóstico  : {atencion['diagnostico']}")
            print(f"  Tratamiento  : {atencion['tratamiento']}")
            print(f"  Servicio     : {atencion['servicio']}")
            print(f"  Importe      : ${atencion['importe']:.2f}")
            separador_simple()
    pausar()

