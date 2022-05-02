#************************************
# Universidade Técnica do Atlâtico (UTA)
# Sitemas de Telecomunicacoes (Pratica 1)
# Walter Dos Santos
# wsantos@uta.cv
#***********************************

from decimal import Decimal

class ArithmeticCoding:

    def __init__(self, frequency_table):
        self.probability_table = self.get_probability_table(frequency_table)

    def get_probability_table(self, frequency_table):
        """
        calcular as probabilidades da tabela
        """
        total_frequency = sum(list(frequency_table.values()))

        probability_table = {}
        for key, value in frequency_table.items():
            probability_table[key] = value / total_frequency

        return probability_table

    def get_encoded_value(self, encoder):
        """
        este metado retorna a messangem completa
        """
        last_stage = list(encoder[-1].values())
        last_stage_values = []
        for sublist in last_stage:
            for element in sublist:
                last_stage_values.append(element)

        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)
        return (last_stage_min + last_stage_max) / 2

    def process_stage(self, probability_table, stage_min, stage_max):
        """
        processa o encode e decode
        """
        stage_probs = {}
        stage_domain = stage_max - stage_min
        for term_idx in range(len(probability_table.items())):
            term = list(probability_table.keys())[term_idx]
            term_prob = Decimal(probability_table[term])
            cum_prob = term_prob * stage_domain + stage_min
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob
        return stage_probs

    def encode(self, msg, probability_table):

        encoder = []

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)


        for msg_term_idx in range(len(msg)):
            stage_probs = self.process_stage(probability_table, stage_min, stage_max)

            msg_term = msg[msg_term_idx]

            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]
            print(msg_term+" ->intervalo da letra:  "+str(stage_min) + " a " + str(stage_max))  # ---------------------------------------------------------
            encoder.append(stage_probs)

        stage_probs = self.process_stage(probability_table, stage_min, stage_max)

        encoder.append(stage_probs)
        print(encoder)

        encoded_msg = self.get_encoded_value(encoder)

        return encoder, encoded_msg

    def decode(self, encoded_msg, msg_length, probability_table):
        global msg_term
        decoder = []
        decoded_msg = ""


        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for idx in range(msg_length):
            stage_probs = self.process_stage(probability_table, stage_min, stage_max)

            for msg_term, value in stage_probs.items():
                if value[0] <= encoded_msg <= value[1]:
                    break

            # --------- poderia ficar no main :
            decoded_msg = decoded_msg + msg_term
            cal = (encoded_msg - stage_min) / (stage_max - stage_min)
            print(decoded_msg + " ->intervalo:  " + str(cal))
            #---------------------------------------------------------------

            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            decoder.append(stage_probs)

        stage_probs = self.process_stage(probability_table, stage_min, stage_max)
        decoder.append(stage_probs)

        return decoder, decoded_msg





#----------------------WAITING FOR UPDATES:

                # se conseguir melhorar algo, ou implementar alguma interface gráfica . . .