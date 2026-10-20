# Iago segue uma breve descrição da idéia do código
#Aqui define oq é um horário de monitoria, uma reserva e a agenda, e tem as regrinhas lá: listar só os horários livres, reservar e 
#recusar quando o horário está ocupado ou cancelado

from datetime import timedelta

DURACAO_MINUTOS = 30

LIVRE = "livre"
RESERVADO = "reservado"
CANCELADO = "cancelado"


MONITORES = {
    "Cálculo": "Iago",
    "Física": "Eric",
    "POO": "Luiz",
    "Estruturas de Dados": "Rodrigues",
}


class HorarioOcupadoError(Exception):
    """O horário já foi reservado por outro aluno"""


class HorarioCanceladoError(Exception):
    """O horário foi cancelado pelo monitor"""


class Horario:
    def __init__(self, disciplina, monitor, inicio, estado=LIVRE):
        self.disciplina = disciplina
        self.monitor = monitor
        self.inicio = inicio
        self.tipo = "individual"
        self.estado = estado

    def fim(self):
        return self.inicio + timedelta(minutes=DURACAO_MINUTOS)

    def esta_livre(self):
        return self.estado == LIVRE


class Reserva:
    def __init__(self, aluno, horario):
        self.aluno = aluno
        self.horario = horario


class Agenda:
    def __init__(self):
        self.horarios = []
        self.reservas = []

    def adicionar_horario(self, horario):
        self.horarios.append(horario)

    def listar_horarios_livres(self, disciplina):
        livres = []
        for h in self.horarios:
            if h.disciplina == disciplina and h.esta_livre():
                livres.append(h)
        return livres

    def reservar(self, aluno, horario):
        if horario.estado == CANCELADO:
            raise HorarioCanceladoError("Este horário foi cancelado")
        if horario.estado == RESERVADO:
            raise HorarioOcupadoError("Este horário já está ocupado")
        reserva = Reserva(aluno, horario)
        horario.estado = RESERVADO
        self.reservas.append(reserva)
        return reserva
