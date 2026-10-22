#Aqui confere se o monitoria.py esta funcionando. Tem um teste para cada critério de aceitação e diz “ok” ou “falhou” para cada um
#Rodando os testes a gente prova que a história esta coerente

import unittest
from datetime import datetime

from monitoria import (Agenda, Horario, HorarioCanceladoError,
                       HorarioOcupadoError, CANCELADO, RESERVADO, MONITORES)


class TestReservaDeHorario(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.inicio = datetime(2026, 10, 21, 14, 0)

    def test_listar_horario_livre(self):
        # Critério 1: lista apenas os horários livres da disciplina

        calculo = Horario("Cálculo", MONITORES["Cálculo"], self.inicio)
        ocupado = Horario("Cálculo", MONITORES["Cálculo"], self.inicio, estado=RESERVADO)
        cancelado = Horario("Cálculo", MONITORES["Cálculo"], self.inicio, estado=CANCELADO)
        fisica = Horario("Física", MONITORES["Física"], self.inicio)
        poo = Horario("POO", MONITORES["POO"], self.inicio)
        estruturas = Horario("Estruturas de Dados",
                             MONITORES["Estruturas de Dados"], self.inicio)
        for h in (calculo, ocupado, cancelado, fisica, poo, estruturas):
            self.agenda.adicionar_horario(h)

        self.assertEqual(self.agenda.listar_horarios_livres("Cálculo"), [calculo])
        self.assertEqual(self.agenda.listar_horarios_livres("Física"), [fisica])
        self.assertEqual(self.agenda.listar_horarios_livres("POO"), [poo])
        self.assertEqual(self.agenda.listar_horarios_livres("Estruturas de Dados"),
                         [estruturas])

    def test_horario_reservado(self):
        # Critério 2: reserva fica registrada e o horário sai da lista de livres

        horario = Horario("POO", MONITORES["POO"], self.inicio)
        self.agenda.adicionar_horario(horario)

        reserva = self.agenda.reservar("Emanuela", horario)

        self.assertEqual(reserva.aluno, "Emanuela")
        self.assertIs(reserva.horario, horario)
        self.assertEqual(reserva.horario.monitor, "Luiz")
        self.assertIn(reserva, self.agenda.reservas)
        self.assertNotIn(horario, self.agenda.listar_horarios_livres("POO"))

    def test_horario_ocupado(self):
        # Critério 3: horário já reservado é recusado

        horario = Horario("Física", MONITORES["Física"], self.inicio)
        self.agenda.adicionar_horario(horario)
        self.agenda.reservar("Emanuela", horario)

        with self.assertRaises(HorarioOcupadoError) as erro:
            self.agenda.reservar("Laura", horario)
        self.assertIn("ocupado", str(erro.exception))
        self.assertEqual(len(self.agenda.reservas), 1)

    def test_horario_cancelado(self):
        # Critério 4: horário cancelado é recusado

        horario = Horario("Estruturas de Dados", MONITORES["Estruturas de Dados"],
                          self.inicio, estado=CANCELADO)
        self.agenda.adicionar_horario(horario)

        with self.assertRaises(HorarioCanceladoError) as erro:
            self.agenda.reservar("Emanuela", horario)
        self.assertIn("cancelado", str(erro.exception))
        self.assertEqual(len(self.agenda.reservas), 0)

    def test_30_minutos(self):
        # Critério 5: o horário termina 30 minutos depois do início

        horario = Horario("Cálculo", MONITORES["Cálculo"], datetime(2026, 10, 21, 14, 0))
        self.agenda.adicionar_horario(horario)
        self.agenda.reservar("Carneiro", horario)
        self.assertEqual(horario.fim(), datetime(2026, 10, 21, 14, 30))

        horario = Horario("Cálculo", MONITORES["Cálculo"], datetime(2026, 10, 21, 14, 45))
        self.agenda.adicionar_horario(horario)
        self.agenda.reservar("Neres", horario)
        self.assertEqual(horario.fim(), datetime(2026, 10, 21, 15, 15))

if __name__ == "__main__":
    unittest.main()
