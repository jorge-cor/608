"""
crie uma class carros

instancie a class e mostre os atributos

Adicione um metodo para travar

adicione um metodo que calcule a diststancia que o carro andou (pode receber o tempo em horas)
    garanta que a hora e uma str com o formato " 00:00 " (sem usar o datetime)

"""

# todo -por fazer
# fixme - a dar erro, tem de ser revisto


class Carro:
    def __init__(self, marca: str, modelo: str, ano: str,velocidade: int = 0 ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelaracao(self, acelaracao: int):
        self.velocidade += acelaracao
        print(f"a velocidade e agora {self.velocidade} Km/h")

    def travar(self, reducao):
        self.velocidade -= reducao
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Travou! Velocidade atual: {self.velocidade} Km/h")

    def calcular_distancia(self, horas):
        distancia = self.velocidade * horas
        return distancia

    def hora(self, hora_partida,horas_viagem):
        if ":" not in hora_partida:
            hora_partida += ":00"

        partes = hora_partida.split(":")

        if len(partes) != 2:
            print("Erro: Formato deve ser HH:MM")
            return None

        try:
            h_inicio = int(partes[0])
            m_inicio = int(partes[1])

            if not (0 <= h_inicio <= 23) or not (0 <= m_inicio <= 59):
                print("Erro: Horas ou minutos fora do intervalo possível.")
                return None

        except ValueError:
            print("Erro: A hora deve conter apenas números.")
            return None

        duracao_h = int(horas_viagem)
        duracao_m = int((horas_viagem - duracao_h) * 60)

        total_m = m_inicio + duracao_m
        total_h = h_inicio + duracao_h
        total_h += total_m // 60

        m_final = total_m % 60
        h_final = total_h % 24
        return f"{h_final:02d}:{m_final:02d}"

o_meu_carro = Carro("Toyota", "Auris", ano="2017", velocidade=0 )
o_teu_carro = Carro("Tesla", "Model 3", ano="2024", velocidade=0)

print(f"{o_meu_carro.marca}, {o_meu_carro.modelo}, {o_meu_carro.ano}")
print(f"{o_teu_carro.marca}, {o_teu_carro.modelo}, {o_teu_carro.ano}")

o_meu_carro.acelaracao(50)
o_teu_carro.acelaracao(10)
o_meu_carro.acelaracao(50)

o_meu_carro.travar(30)
o_meu_carro.travar(30)

tempo_viagem = 2
meu_km_percorridos = o_meu_carro.calcular_distancia(tempo_viagem)
print(f"A manter esta velocidade, em {tempo_viagem} horas o meu carro percorreria {meu_km_percorridos} Km.")

teu_km_percorridos = o_teu_carro.calcular_distancia(tempo_viagem)
print(f"A manter esta velocidade, em {tempo_viagem} horas o Teu carro percorreria {teu_km_percorridos} Km.")

hora_partida="20"

chegada = o_meu_carro.hora(hora_partida, tempo_viagem)
print(f"o meu carro saiu às {hora_partida}, viajou {tempo_viagem}h \n Chega às {chegada} com uma distamcia de {meu_km_percorridos} Km.\n")
chegada = o_teu_carro.hora(hora_partida, tempo_viagem)
print(f"o teu carro saiu às {hora_partida}, viajou {tempo_viagem}h \n Chega às {chegada} com uma distamcia de {teu_km_percorridos} Km.")