import numpy as np
from gnuradio import gr
import math

# Definición de la clase como bloque síncrono en GNU Radio
class blk(gr.sync_block):  

    """This block implements a Baseband Voltage-Controlled Oscillator (Complex Envelope) 
       that generates a complex exponential signal with controllable amplitude and phase.

Inputs:
- First input (top): Amplitude (A) of the complex exponential signal (float32).
- Second input (bottom): Phase (Q) in radians (float32).

Output:
- A complex exponential signal defined as:
  y[n] = A · e^(jQ)   (complex64)

Notes for correct use:
- This block generates the complex envelope (CE) representation of a signal.
- The output is suitable for complex baseband signal processing and digital modulation schemes.
- The phase input (Q) directly determines the angle of the complex exponential.
- For real-valued RF outputs instead of complex baseband, use the RF VCO block."""



    # Constructor del bloque
    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   # Nombre del bloque en GNU Radio
            in_sig=[np.float32, np.float32], # Dos entradas: [Amplitud (A), Fase (Q)]
            out_sig=[np.complex64]           # Una salida: señal compleja (I + jQ)
        )
        
    # Función principal: procesa entradas y genera salida
    def work(self, input_items, output_items):
        A = input_items[0]      # Primera entrada -> amplitud de la señal (float32)
        Q = input_items[1]      # Segunda entrada -> fase en radianes (float32)
        y = output_items[0]     # Salida -> señal compleja (np.complex64)
        N = len(A)              # Número de muestras a procesar en esta ejecución

        # Señal de salida: representación de la envolvente compleja
        # Fórmula: y[n] = A * exp(j*Q) = A * (cos(Q) + j*sin(Q))
        y[:] = A * np.exp(1j * Q)

        # Retorna el número de muestras procesadas
        return len(output_items[0])
