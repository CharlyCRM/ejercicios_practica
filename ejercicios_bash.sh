#!/bin/bash

################################################################################
# EJERCICIOS DE BASH — BLOQUES INDEPENDIENTES PARA PRACTICAR
# ----------------------------------------------------------------------------
# Cómo usar este fichero:
#   1) Cada ejercicio está completamente comentado y separado por un banner.
#   2) Para probar un ejercicio, DESCOMENTA sus líneas y ejecútalo:  bash ejercicios_bash.sh
#   3) Vuelve a comentar antes de pasar al siguiente, para evitar interferencias.
#   4) Muchos bloques escriben en disco: lee la descripción antes de activarlos.
################################################################################

################################################################################
# 01) VARIABLES DE ENTORNO
################################################################################
# Descripción: Muestra valores típicos del entorno de usuario.
# Activación: descomenta las 4 líneas inferiores.
# ----------------------------------------------------------------------------
# echo "El usuario actual es: $USER"
# echo "Tu directorio de trabajo es: $HOME"
# echo "Tu shell es: $SHELL"
# echo "Rutas de búsqueda de programas (PATH): $PATH"
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 02) ENTRADA CON read + OPERACIÓN MATEMÁTICA
################################################################################
# Descripción: Pide dos enteros y calcula su suma usando expr.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# echo "Introduce un número entero"
# read numero1
# echo "Introduce otro número entero"
# read numero2
# total=$(expr $numero1 + $numero2)
# echo "La suma de $numero1 + $numero2 es: $total"
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 03) CREACIÓN DINÁMICA DE FICHEROS
################################################################################
# Descripción: Crea un fichero vacío con el nombre indicado por teclado.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# echo "Introduce el nombre del fichero: "
# read nombre_fichero
# touch "$nombre_fichero"
# echo "Fichero $nombre_fichero creado correctamente"
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 04) USO DE date
################################################################################
# Descripción: Formatea y muestra la fecha actual (DD/MM/YYYY).
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# fecha_actual=$(date +"%d/%m/%Y")
# echo "La fecha de hoy es: $fecha_actual"
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 05) pwd y ls
################################################################################
# Descripción: Muestra el directorio actual y lista su contenido.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# echo "Te encuentras en: $(pwd)"
# echo "El contenido del directorio es el siguiente:"
# ls
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 06) MOVERSE Y CREAR CARPETAS (mkdir, cd, rm)
################################################################################
# Descripción: Crea un árbol temporal de directorios, lo muestra y lo borra.
# Activación: descomenta el bloque. ¡Atención! Borra carpetas llamadas
#             "proyecto_temporal" si existen en el directorio actual.
# ----------------------------------------------------------------------------
# hora=$(date +%H:%M:%S)
# echo "[$hora] Creando directorio: proyecto_temporal"
# mkdir -p "proyecto_temporal"
# echo "[$hora] Directorio creado en: $(pwd)/proyecto_temporal"
# echo "[$hora] Creando subdirectorio: resultado_temporal"
# cd "proyecto_temporal"
# mkdir -p "resultado_temporal"
# echo "[$hora] Subdirectorio creado en: $(pwd)/resultado_temporal"
# echo "[$hora] Volviendo al directorio original..."
# cd ..
# echo "[$hora] Eliminando directorios..."
# rm -r proyecto_temporal
# echo "[$hora] Proceso completado. Los directorios han sido eliminados"
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 07) CONDICIONALES CON [ ] (TEST)
################################################################################
# Descripción: Pide la edad y comprueba si es mayor o menor de edad.
# Activación: descomenta el bloque.
# Notas: Operadores numéricos en test: -eq ==; -ne !=; -lt <; -le <=; -gt >; -ge >=
# ----------------------------------------------------------------------------
# echo "Introduce tu edad: "
# read edad_usuario
# if [ "$edad_usuario" -ge 18 ]; then
#   echo "Eres mayor de edad"
# else
#   echo "Eres menor de edad"
# fi
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 08) CONDICIONALES CON (( ... )) (ARITMÉTICA)
################################################################################
# Descripción: Comprueba si un número entero es par o impar usando módulo.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# read -p "Introduce un número entero: " numero_entero
# resto_division=$((numero_entero % 2))
# if [ "$resto_division" -eq 0 ]; then
#   echo "El valor introducido es par"
# else
#   echo "El valor introducido es impar"
# fi
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 09) COMPROBAR SI UN FICHERO EXISTE (-f)
################################################################################
# Descripción: Pide un nombre y verifica si existe un fichero regular.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# read -p "Introduce el nombre del fichero: " nombre_fichero
# if [ -f "$nombre_fichero" ]; then
#   echo "El fichero $nombre_fichero existe"
# else
#   echo "El fichero $nombre_fichero no existe"
# fi
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 10) COMPROBAR PERMISOS DE EJECUCIÓN (-x)
################################################################################
# Descripción: Verifica si un fichero tiene permiso de ejecución.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# read -p "Introduce el nombre del fichero: " nombre_fichero
# if [ -x "$nombre_fichero" ]; then
#   echo "El fichero $nombre_fichero tiene permisos de ejecución"
# else
#   echo "El fichero $nombre_fichero no tiene permisos de ejecución"
# fi
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 11) MENÚ CON case
################################################################################
# Descripción: Muestra un menú simple y ejecuta una opción con case.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# echo "-- Menú Principal --"
# echo "1: Ver fecha y hora"
# echo "2: Ver directorio actual"
# echo "3: Salir"
# echo "----------------------------"
# read -p "Introduce una opción: " opcion
# case $opcion in
#   1)
#     echo "La hora actual es $(date)"
#     ;;
#   2)
#     echo "Directorio actual: $PWD"
#     ;;
#   3)
#     echo "Gracias por usar nuestra aplicación"
#     ;;
#   *)
#     echo "Opción no válida"
#     ;;
# esac
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 12) BUCLE for — CUENTA ATRÁS
################################################################################
# Descripción: Imprime una cuenta atrás de 5 a 1 y luego "Despegue".
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# echo "Iniciando cuenta atrás..."
# for numero_actual in $(seq 5 -1 1); do
#   echo "$numero_actual"
# done
# echo "Despegue 🚀"
# ────────────────────────────────────────────────────────────────────────────

################################################################################
# 13) BUCLE for + ls — LISTAR DIRECTORIOS
################################################################################
# Descripción: Recorre la salida de ls e imprime cada elemento.
# Activación: descomenta el bloque.
# ----------------------------------------------------------------------------
# echo "Directorio actual: $PWD"
# echo ""
# for elemento in $(ls); do
#   echo "$elemento"
# done
# ────────────────────────────────────────────────────────────────────────────
