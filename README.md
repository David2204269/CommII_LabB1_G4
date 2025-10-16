# CommII_LabB1_G4
Laboratorio de comunicaciones II

  - David Josué Díaz Ortiz, 2204269, Estudiante Ing. Electrónica.
  - Duban Yesid Cortes Tabares, 2214644, Estudiante Ing. Electrónica.


# Práctica 4 – Modulación M-PSK

## Descripción general
Esta práctica presenta la implementación de la **modulación M-PSK (Phase Shift Keying)** utilizando **GNU Radio**, con el objetivo de comprender la representación de símbolos digitales mediante variaciones de fase.  
La práctica se desarrolla completamente en software, incorporando la **envolvente compleja** y los conceptos de constelación, ancho de banda y relación símbolo-bit.

##  Objetivos

- Implementar un transmisor M-PSK a partir de la teoría explicada en clase.  
- Utilizar **GNU Radio** para generar señales VCO mediante bloques prediseñados o programación en **Python**.  
- Verificar y analizar las constelaciones obtenidas, así como la influencia del ruido en los símbolos.  
- Determinar los parámetros característicos de la señal: **ancho de banda, eficiencia y rata de símbolos**.  
- Representar las señales tanto en **radiofrecuencia (RF)** como en su **envolvente compleja (EC)**.  
- Implementar y comparar una modulación **Q-PSK**, verificando las diferencias en ancho de banda y velocidad de símbolos.

##  Estructura del repositorio

| Carpeta / Archivo | Descripción |
|-------------------|-------------|
| `/GNURadio/` | Archivos `.grc` con los diagramas de flujo de las modulaciones M-PSK y Q-PSK. |
| `/Informe/` | Contiene el informe en formato IEEE con resultados, figuras y análisis. |
| `/Practica_4_David/` | Archivos y simulaciones realizadas por el integrante David. |
| `/Practica_4_Duban/` | Archivos y simulaciones realizadas por el integrante Duban. |
| `README.md` | Documento guía que orienta al lector sobre la estructura y propósito del laboratorio. |

## Descripción de la práctica

La práctica desarrolla un sistema digital que implementa la **modulación M-PSK** empleando bloques de **GNU Radio**.  
Se genera una señal portadora mediante un bloque **VCO** y se modula la fase de acuerdo con una tabla de verdad programada manualmente.  
Posteriormente, se obtiene la **envolvente compleja** de la señal y se analiza su **espectro de potencia**, identificando los puntos donde el espectro pasa por cero y su relación con la **rata de símbolos**.  

También se implementa una **modulación Q-PSK**, repitiendo el proceso de análisis y comparación con la M-PSK inicial, para observar variaciones en el desempeño espectral y temporal.

## Herramientas utilizadas

- **GNU Radio Companion (GRC)** – entorno de diseño de sistemas digitales.  
- **Linux (Ubuntu)** – sistema operativo para ejecución de las simulaciones.  
- **Python** – programación de tablas de verdad y señales VCO.  
- **Git y GitHub** – control de versiones y almacenamiento del proyecto.

## Resultados esperados

El repositorio incluye:

- Diagramas de constelación para M-PSK y Q-PSK.  
- Espectros de potencia de la envolvente compleja.  
- Comparaciones entre modulaciones en cuanto a **ancho de banda, velocidad de bits y símbolos**.  
- Ejemplos de constelaciones personalizadas desarrolladas por los integrantes del grupo.

## Enlace al repositorio

> [https://github.com/David2204269/CommII_LabB1_G4.git)



