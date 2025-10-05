import numpy as np
from gnuradio import gr
import math

# Definición del bloque como clase hija de gr.sync_block (bloque síncrono en GNU Radio)

class blk(gr.sync_block):  
    """This block implements a Radio Frequency Voltage-Controlled Oscillator (RF VCO) 
       that generates a sinusoidal signal with controllable amplitude and phase.

Inputs:
- First input (top): Amplitude (A) of the sinusoidal signal (float32).
- Second input (bottom): Phase offset (Q) in radians (float32).

Output:
- A sinusoidal signal defined as: 
  y[n] = A * cos(2π * fc * n / samp_rate + Q)  (float32)

Parameters:
- fc: Carrier frequency in Hz (default: 128,000 Hz).
- samp_rate: Sampling rate in samples per second (default: 320,000 Hz).

Notes for correct usage:
- The block preserves phase continuity across consecutive work calls.
- The output frequency is determined by fc and may experience aliasing if fc ≥ samp_rate/2.
- To satisfy the Nyquist criterion and avoid distortion, samp_rate must be greater than 2*fc.
- The phase input (Q) can be used to apply phase modulation to the carrier signal."""



    # Constructor del bloque: define parámetros iniciales y entradas/salidas
    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   # Nombre del bloque en GNU Radio
            in_sig=[np.float32, np.float32],  # Dos entradas: [Amplitud (A), Fase (Q)]
            out_sig=[np.float32]              # Una salida: señal RF en formato float
        )
        self.fc = fc              # Frecuencia central de la portadora (Hz)
        self.samp_rate = samp_rate # Frecuencia de muestreo (Hz)
        self.n_m = 0              # Contador de muestras acumuladas (para continuidad de la señal)

    # Función principal que procesa las entradas y genera la salida
    def work(self, input_items, output_items):
        A = input_items[0]        # Primera entrada -> amplitud de la señal
        Q = input_items[1]        # Segunda entrada -> fase de la señal
        y = output_items[0]       # Señal de salida (vector donde se almacenan los resultados)
        N = len(A)                # Número de muestras que se van a procesar en esta llamada

        # Vector de índices de muestra, ajustado con el contador acumulado
        n = np.linspace(self.n_m, self.n_m+N-1, N)
        self.n_m += N             # Se actualiza el contador para mantener la continuidad temporal

        # Señal de salida: coseno modulado en amplitud (A) y fase (Q)
        # Fórmula: y[n] = A * cos(2*pi*fc*n/samp_rate + Q)
        y[:] = A * np.cos(2*math.pi*self.fc*n/self.samp_rate + Q)

        # Retorna el número de muestras procesadas
        return len(output_items[0])

