# CommII_LabB1_G4  
Laboratorio de comunicaciones II  

  - David Josué Díaz Ortiz, 2204269, Estudiante Ing. Electrónica.  
  - Duban Yesid Cortes Tabares, 2214644, Estudiante Ing. Electrónica.  

---

# Práctica 6 – Waveforming con Filtro Coseno Alzado  

## Descripción general  
Esta práctica tiene como objetivo la implementación y análisis del **formador de pulsos basado en el Filtro Coseno Alzado (Raised Cosine Filter)** dentro del entorno **GNU Radio Companion (GRC)**.  
El propósito es estudiar cómo la forma del filtro afecta la eficiencia espectral, la interferencia intersimbólica (ISI) y la calidad general de la señal modulada, tanto en presencia como en ausencia de ruido.  

El laboratorio aborda tanto el **filtro Coseno Alzado (RC)** como su variante **Raíz de Coseno Alzado (RRC)**, comparando su efecto sobre el ancho de banda, el diagrama de ojo, la constelación y la densidad espectral de potencia (PSD).

---

## Objetivos  

- Practicar los métodos de **waveforming** mediante el uso del filtro **Coseno Alzado y Raíz de Coseno Alzado**.  
- Verificar los parámetros y características propias de ambos tipos de filtros.  
- Analizar el **ancho de banda ocupado (BW)** y su dependencia con el factor de roll-off β.  
- Observar la **Interferencia Intersimbólica (ISI)** mediante el diagrama de ojo.  
- Evaluar el efecto del **ruido** sobre el desempeño del sistema y la degradación de la constelación.  

---

##  Estructura del repositorio  

| Carpeta / Archivo | Descripción |
|-------------------|-------------|
| `/GNURadio/` | Contiene los archivos `.grc` con los flujogramas de simulación del formador de pulsos y modulación digital. |
| `/Informe/` | Carpeta que incluye el informe formal con los resultados, gráficas y conclusiones. |
| `/Practica_6_David/` | Archivos y simulaciones desarrolladas por el integrante David. |
| `/Practica_6_Duban/` | Archivos y simulaciones desarrolladas por el integrante Duban. |
| `README.md` | Documento guía que describe la organización y propósito del laboratorio. |

---

## Descripción de la práctica  

El experimento se centra en el diseño y evaluación de señales moduladas bajo distintos esquemas de **waveforming**, utilizando filtros rectangulares, coseno alzado y raíz de coseno alzado.  
Se analizan las siguientes configuraciones experimentales:

1. **Forma rectangular sin filtrado**, sin ruido.  
2. **Forma rectangular con filtrado (BW = Rs)**, observando la aparición de ISI.  
3. **Coseno alzado con β = 1**, sin ruido — verificación de ancho de banda \( BW = W(1+β) \) con \( W = Rs/2 \).  
4. **Coseno alzado con β = 0**, sin ruido.  
5. **Coseno alzado con β = 0.5**, sin ruido.  
6. **Raíz de coseno alzado con β = 0.5**, sin ruido — comparación del diagrama de ojo con el caso anterior.  
7. **Repetición de todos los casos anteriores con modulación 16-QAM y presencia de ruido.**

Los resultados incluyen:
- Señales en el dominio del **tiempo y frecuencia (PSD)**.  
- **Constelaciones** en el origen y después del canal.  
- **Diagramas de ojo** que permiten identificar el instante libre de ISI.  
- Cálculo y comparación del **ancho de banda medido vs teórico**.  

---

## Herramientas utilizadas  

- **GNU Radio Companion (GRC)** – diseño y simulación de sistemas digitales.  
- **Linux (Ubuntu)** o **Windows** – entorno de ejecución.  
- **Git y GitHub** – control de versiones y almacenamiento colaborativo.  
- **Python** – análisis y generación de resultados adicionales.  

---

## Enlace al repositorio  

> [https://github.com/David2204269/CommII_LabB1_G4.git](https://github.com/David2204269/CommII_LabB1_G4.git)

