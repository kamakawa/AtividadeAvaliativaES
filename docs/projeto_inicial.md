# **2. Projeto inicial**

## **2.1 História escolhida**

**HU2 - Reservar horário de monitoria.** É a única história de prioridade Alta e as demais (aviso de cancelamento, atendimento em grupo, faltas e relatório) dependem de a reserva existir.

---

## **2.2 Estrutura da solução**

A lógica fica em classes que os testes chamam diretamente. Nenhuma informação é digitada durante a execução e todos os dados ficam em memória.

**Horario**

* Representa um atendimento de monitoria: disciplina, monitor, data e hora de início, duração de 30 minutos, tipo (neste protótipo, sempre individual) e estado (livre, reservado ou cancelado).
* **Responsabilidades:** calcular o horário de término e informar se está livre.
* O cancelamento em si (HU1) está fora do escopo, mas os testes precisam de um horário cancelado. Por isso o Horario pode ser criado já no estado cancelado, e essa é a forma usada pelo teste do critério 4.

**Reserva**

* Liga um aluno a um horário.
* **Responsabilidade:** guardar quem reservou e qual horário foi reservado.

**Agenda**

* Guarda os horários e as reservas.
* **Responsabilidades:**
  * listar os horários livres de uma disciplina;
  * reservar um horário para um aluno, recusando a reserva quando o horário já está ocupado ou foi cancelado.
* Ao reservar com sucesso, é a Agenda quem cria a Reserva e muda o estado do Horario para reservado, de modo que a lista de reservas e o estado do horário não fiquem inconsistentes.

**Erros do domínio**

* Duas exceções próprias: horário ocupado e horário cancelado.
* **Responsabilidade:** representar as recusas com uma mensagem clara, para que os testes de falha as verifiquem.

**Arquivo principal**

* Apenas demonstra o uso das classes com dados de exemplo. Nenhuma regra fica nele.

---

## **2.3 Decisões de projeto**

* Os testes montam seus próprios dados (horários e alunos) e não dependem de entrada do usuário.
* Duração do atendimento: 30 minutos.
* Atendimento em grupo, faltas, relatórios e avisos não fazem parte deste protótipo.

---

## **2.4 Critérios de aceitação e testes**

**Critério 1:** Ao consultar uma disciplina, o sistema lista apenas os horários livres dela.

* **Teste que verifica:** test_listar_horario_livre
* **Cenário:** Sucesso

**Critério 2:** Ao reservar um horário individual livre, a reserva fica registrada para o aluno e o horário deixa de aparecer entre os livres.

* **Teste que verifica:** test_horario_reservado
* **Cenário:** Sucesso

**Critério 3:** Se o horário individual já estiver reservado, o sistema recusa a reserva e informa que está ocupado.

* **Teste que verifica:** test_horario_ocupado
* **Cenário:** Falha

**Critério 4:** Se o horário estiver cancelado, o sistema recusa a reserva e informa que foi cancelado.

* **Teste que verifica:** test_horario_cancelado
* **Cenário:** Falha

**Critério 5:** O horário reservado termina 30 minutos depois do início.

* **Teste que verifica:** test_30_minutos
* **Cenário:** Sucesso
