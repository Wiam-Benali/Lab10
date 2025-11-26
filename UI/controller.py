import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        try:
            input_val = int(self._view.guadagno_medio_minimo.value)

            self._model.costruisci_grafo(input_val)

            num_nodes = self._model.get_num_nodes()
            num_edges = self._model.get_num_edges()
            self._view.lista_visualizzazione.controls.append(ft.Text(f'Numero di Hubs: {num_nodes}'))
            self._view.lista_visualizzazione.controls.append(ft.Text(f'Numero di Tratte: {num_edges}'))



            for tratta in self._model._edges:
                self._view.lista_visualizzazione.controls.append(ft.Text(f'{tratta.partenza},{tratta.arrivo} - {tratta.val}'))
            self._view.update()

        except ValueError:
            self._view.show_alert("Numero di Guadagno medio minimo non valido")
