# CommII_LabB1_G4
Laboratorio de comunicaciones II
-David Josué Díaz Ortiz, 2204269, Estudiante Ing. Electrónica.
-Duban Yesid Cortes Tabares, 2214644, Estudiante Ing. Electrónica.



# Práctica 5 – Modulación M-QAM

## Descripción general
Esta práctica desarrolla la implementación y análisis de la **modulación M-QAM (Quadrature Amplitude Modulation)** utilizando la plataforma **GNU Radio**.  
El propósito es analizar el comportamiento de las señales digitales moduladas con diferentes órdenes de modulación, así como comparar su desempeño en presencia de ruido, tanto en banda base como en su versión pasabanda.

## Objetivos

- Programar y simular modulaciones digitales basadas en constelaciones (M-QAM, PSK, etc.).  
- Analizar la forma de onda, constelación, espectro y tasa de bits para diferentes modulaciones.  
- Comparar el rendimiento entre modulaciones **BPSK, QPSK, 8PSK y 16-QAM** bajo condiciones similares.  
- Implementar una versión pasabanda simulada mediante un **up-converter** en el flujo de bloques de GNU Radio.

## Estructura del repositorio

| Carpeta / Archivo | Descripción |
|-------------------|-------------|
| `/GNURadio/` | Contiene los archivos `.grc` utilizados para el diseño y simulación de los esquemas de modulación. |
| `/Informe/` | Carpeta destinada al informe en formato IEEE, con resultados, figuras y análisis descriptivos. |
| `/Practica_5_David/` | Archivos, simulaciones y resultados generados por el integrante David. |
| `/Practica_5_Duban/` | Archivos, simulaciones y resultados generados por el integrante Duban. |
| `README.md` | Documento guía que orienta al lector sobre la organización y propósito del laboratorio. |

## Descripción de la práctica

El experimento se basa en un esquema configurable de **modulación y demodulación M-QAM**, implementado en GNU Radio.  
Se simulan varios órdenes de modulación (2, 4, 8, 16) para analizar la relación entre eficiencia espectral y tolerancia al ruido.  
Las figuras obtenidas incluyen constelaciones, espectros de potencia y señales pasabanda, las cuales se interpretan dentro del informe principal.

## Herramientas utilizadas

- **GNU Radio Companion (GRC)** – entorno de diseño de bloques.  
- **Linux (Ubuntu)** – sistema operativo base para la simulación.  
- **Git y GitHub** – control de versiones y alojamiento del proyecto.  
- **Python** – análisis y procesamiento de datos complementarios.

## 🔗 Enlace al repositorio

> [https://github.com/David2204269/CommII_LabB1_G4.git)

