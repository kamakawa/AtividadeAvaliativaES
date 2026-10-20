from datetime import datetime

from monitoria import (Agenda, Horario, HorarioCanceladoError,
                       HorarioOcupadoError, CANCELADO, MONITORES)


def mostrar_livres(agenda, disciplina):
    print(f"Horários livres de {disciplina}:")
    for h in agenda.listar_horarios_livres(disciplina):
        inicio = h.inicio.strftime("%d/%m %H:%M")
        fim = h.fim().strftime("%H:%M")
        print("  " + inicio + " - " + fim + " (monitor " + h.monitor + ")")


def tentar_reservar(agenda, aluno, horario):
    try:
        agenda.reservar(aluno, horario)
        inicio = horario.inicio.strftime("%d/%m %H:%M")
        print(aluno + " reservou " + inicio + ".")
    except (HorarioOcupadoError, HorarioCanceladoError) as erro:
        print(f"{aluno} não conseguiu reservar: {erro}")


if __name__ == "__main__":
    agenda = Agenda()
    h1 = Horario("Cálculo", MONITORES["Cálculo"], datetime(2026, 10, 21, 14, 0))
    h2 = Horario("Cálculo", MONITORES["Cálculo"], datetime(2026, 10, 21, 14, 30))
    h3 = Horario("Cálculo", MONITORES["Cálculo"], datetime(2026, 10, 21, 15, 0),
                 estado=CANCELADO)
    h4 = Horario("Física", MONITORES["Física"], datetime(2026, 10, 21, 14, 0))
    h5 = Horario("POO", MONITORES["POO"], datetime(2026, 10, 22, 10, 0))
    h6 = Horario("Estruturas de Dados", MONITORES["Estruturas de Dados"],
                 datetime(2026, 10, 22, 11, 0))
    for h in (h1, h2, h3, h4, h5, h6):
        agenda.adicionar_horario(h)

    for disciplina in MONITORES:
        mostrar_livres(agenda, disciplina)

    tentar_reservar(agenda, "Emanuela", h1)
    tentar_reservar(agenda, "Laura", h1)
    tentar_reservar(agenda, "Laura", h3)
    tentar_reservar(agenda, "Emanuela", h5)
    mostrar_livres(agenda, "Cálculo")
    mostrar_livres(agenda, "POO")
