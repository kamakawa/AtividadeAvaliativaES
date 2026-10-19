# **1\. Histórias de usuário**

## **HU1 \- Aviso de cancelamento de atendimento**

**Trecho do e-mail:** "...mas às vezes precisa cancelar por causa de prova. Os alunos reclamam que só descobrem o cancelamento quando chegam na sala."

**História:** Como aluno, eu quero ser avisado quando um atendimento que reservei for cancelado para não ir à sala à toa.

**Critérios de aceitação:**

1. Quando o monitor cancela um horário, o sistema registra um aviso para cada aluno que o reservou.  
2. Alunos que não reservaram o horário cancelado não recebem aviso.  
3. O aviso informa disciplina, data e horário do atendimento cancelado.

**Prioridade:** Média

**Justificativa:** É uma forte reclamação dos alunos, mas só funciona depois que a reserva existe.

---

## **HU2 \- Reservar horário de monitoria**

**Trecho do e-mail:** "A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento."

**História:** Como aluno, eu quero reservar um horário livre de monitoria de uma disciplina para garantir meu atendimento sem precisar combinar por mensagem.

**Critérios de aceitação:**

1. Ao consultar uma disciplina, o sistema lista apenas os horários livres dela.  
2. Ao reservar um horário individual livre, a reserva fica registrada para o aluno e o horário deixa de aparecer entre os livres.  
3. Se o horário individual já estiver reservado, o sistema recusa a reserva e informa que está ocupado.  
4. Se o horário estiver cancelado, o sistema recusa a reserva e informa que foi cancelado.  
5. O horário reservado termina 30 minutos depois do início.

**Prioridade:** Alta

**Justificativa:** A cliente disse "Se a reserva de horários funcionar, já ajuda muito." e as outras histórias dependem dela.

---

## **HU3 \- Atendimento em grupo**

**Trecho do e-mail:** "Cada atendimento dura 30 minutos, mas alguns monitores preferem atender em grupo, quando várias pessoas têm a mesma dúvida."

**História:** Como monitor, eu quero abrir um horário para atendimento em grupo para resolver de uma vez a mesma dúvida de várias pessoas.

**Critérios de aceitação:**

1. O monitor consegue marcar um horário dele como atendimento em grupo.  
2. Em um horário em grupo, mais de um aluno consegue reservar o mesmo horário.  
3. Quando o horário em grupo atinge 5 reservas, o sistema recusa novas reservas e informa que está lotado.  
4. Um mesmo aluno não consegue reservar duas vezes o mesmo horário em grupo.

**Prioridade:** Baixa

**Justificativa:** Nem todos os monitores atendem em grupo, e a reserva individual funciona sem isso.

---

## **HU4 \- Registro de faltas**

**Trecho do e-mail:** "Também tem o problema das faltas. Quando o aluno reserva e não aparece, o horário fica perdido. Alguns monitores sugeriram bloquear quem falta muito, mas outros acham isso exagerado."

**História:** Como monitor, eu quero registrar que um aluno reservou e não compareceu para manter o histórico de faltas de cada aluno.

**Critérios de aceitação:**

1. O sistema só permite ao monitor registrar falta em reserva de um horário dele e recusa o registro se o horário for de outro monitor.  
2. O sistema recusa o registro de falta se a reserva não existir.  
3. O sistema só aceita o registro depois do horário do atendimento.  
4. Uma reserva que já teve a falta registrada não pode ser marcada de novo.  
5. O sistema informa o total de faltas registradas de cada aluno.

**Prioridade:** Baixa

**Justificativa:** Cria o histórico, mas os monitores não decidiram qual regra vão aplicar.

---

## **HU5 \- Relatório mensal de horas atendidas**

**Trecho do e-mail:** "A coordenação precisa de um relatório mensal com as horas atendidas por cada monitor, porque isso conta para o pagamento da bolsa. Essas informações de bolsa não podem ficar visíveis para todo mundo."

**História:** Como coordenador, eu quero um relatório mensal com as horas atendidas por cada monitor para calcular o pagamento da bolsa.

**Critérios de aceitação:**

1. Para o mês informado, o relatório mostra o total de horas atendidas de cada monitor.  
2. Atendimentos cancelados e reservas com falta registrada não contam como horas atendidas.  
3. Só entram no relatório atendimentos do mês solicitado.  
4. Se um usuário que não é da coordenação pedir o relatório, o sistema recusa.

**Prioridade:** Média

**Justificativa:** Conta para o pagamento da bolsa, mas depende de atendimentos já registrados.

