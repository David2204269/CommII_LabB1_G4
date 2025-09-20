import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):  # solo argumentos por defecto aquí
        gr.sync_block.__init__(
            self,
            name='e_Diff',        # nombre que aparecerá en GRC
            in_sig=[np.float32],  # señal de entrada
            out_sig=[np.float32]  # señal de salida
        )
        # Guardar la última muestra anterior
        self.prev_sample = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]   # Señal de entrada
        y0 = output_items[0] # Señal de salida (diferenciada)

        # Crear array de salida con la misma longitud que x
        y = np.empty_like(x)

        # Primera diferencia usa la muestra previa guardada
        y[0] = x[0] - self.prev_sample

        # Diferencias internas
        y[1:] = x[1:] - x[:-1]

        # Actualizar la última muestra para la próxima llamada
        self.prev_sample = x[-1]

        # Copiar a salida
        y0[:] = y

        return len(y0)
