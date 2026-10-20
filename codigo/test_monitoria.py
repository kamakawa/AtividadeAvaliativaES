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

        livre = Horario("Cálculo", MONITORES["Cálculo"], self.inicio)
        ocupado = Horario("Cálculo", MONITORES["Cálculo"], self.inicio, estado=RESERVADO)
        fisica = Horario("Física", MONITORES["Física"], self.inicio)
        poo = Horario("POO", MONITORES["POO"], self.inicio)
        estruturas = Horario("Estruturas de Dados",
                             MONITORES["Estruturas de Dados"], self.inicio)
        for h in (livre, ocupado, fisica, poo, estruturas):
            self.agenda.adicionar_horario(h)

        self.assertEqual(self.agenda.listar_horarios_livres("Cálculo"), [livre])
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

        with self.assertRaises(HorarioOcupadoError):
            self.agenda.reservar("Laura", horario)
        self.assertEqual(len(self.agenda.reservas), 1)

    def test_horario_cancelado(self):
        # Critério 4: horário cancelado é recusado

        horario = Horario("Estruturas de Dados", MONITORES["Estruturas de Dados"],
                          self.inicio, estado=CANCELADO)
        self.agenda.adicionar_horario(horario)

        with self.assertRaises(HorarioCanceladoError):
            self.agenda.reservar("Emanuela", horario)
        self.assertEqual(len(self.agenda.reservas), 0)

    def test_30_minutos(self):
        # Critério 5: o horário termina 30 minutos depois do início

        horario = Horario("Cálculo", MONITORES["Cálculo"], datetime(2026, 10, 21, 14, 0))

        self.assertEqual(horario.fim(), datetime(2026, 10, 21, 14, 30))


if __name__ == "__main__":
    unittest.main()
