from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione
from model.tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    pass
    @staticmethod
    def readAllHub():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM hub"
        cursor.execute(query)
        for row in cursor:
            result.append(Hub(row['id'],row['codice'],row['nome'],row['citta'],row['stato'],row['latitudine'],row['longitudine']))
        conn.close()
        cursor.close()
        return result

    @staticmethod
    def readAllspedizioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM spedizione"
        cursor.execute(query)
        for row in cursor:
            result.append(Spedizione(row['id'],
                                     row['id_compagnia'],
                                     row['numero_tracking'],
                                     row['id_hub_origine'],
                                     row['id_hub_destinazione'],
                                     row['data_ritiro_programmata'],
                                     row['distanza'],
                                     row['data_consegna'],
                                     row['valore_merce']))
        conn.close()
        cursor.close()
        return result


    @staticmethod
    def readAlldaotratte(val_limite):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select least(id_hub_origine,id_hub_destinazione) as partenza, greatest(id_hub_origine,id_hub_destinazione) as arrivo, sum(valore_merce)/count(*) as val
                    from spedizione
                    group by partenza,arrivo"""

        cursor.execute(query)
        for row in cursor:

            if row['val'] > val_limite:
                tratta = Tratta(row['partenza'],row['arrivo'],row['val'])
                result.append(tratta)
        conn.close()
        cursor.close()
        return result


