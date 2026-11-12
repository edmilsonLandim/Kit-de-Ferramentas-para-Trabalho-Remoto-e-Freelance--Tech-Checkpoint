# AI Productivity Sprint - Workflow Profissional Assistido por IA

**Sessão 1 - AI Literacy para Produtividade** | Percurso Upskilling | Entregáveis 1
**Cliente (estudo de caso):** Cabo Digital Travel - turismo e experiências locais
**Papel:** freelancer / consultor digital em regime remoto
**Ferramentas:** ChatGPT / Claude (geração e crítica), Google Docs (edição e versão final),
Trello e Slack (contexto do cliente)

> Os outputs abaixo foram gerados com IA e revistos por mim. Os números marcados com `[a
> confirmar]` são hipóteses a validar com o cliente: não foram inventados como factos.

---

## Parte 1 - Análise do contexto

**Principais desafios identificados**
1. Demora na resposta a clientes internacionais (perda de reservas).
2. Comunicação digital inconsistente (tom, língua e informação variam por pessoa).
3. Dificuldade em organizar tarefas e prioridades numa equipa parcialmente remota.
4. Excesso de tarefas administrativas repetitivas (respostas, relatórios, confirmações).
5. Ausência de documentação operacional padronizada (dependência de pessoas-chave).
6. Produção de conteúdos promocionais difícil de escalar.
7. Ferramentas (Google Workspace, Trello, Slack, IA) usadas sem integração.

**Prioridades identificadas** (impacto no cliente final × esforço)
1. **Tempo e consistência de resposta a clientes**: maior impacto direto em receita.
2. **Documentação mínima (SOPs)** para as tarefas mais repetidas.
3. **Organização de tarefas** no Trello com regras de prioridade claras.
4. Conteúdos e automações mais avançadas ficam para a fase 2 do piloto.

**Oportunidades de melhoria**
- Biblioteca de respostas-modelo multilingues (PT/EN/FR) geradas e revistas com IA.
- Prompt padrão com o tom de voz da marca, usado por toda a equipa.
- Triagem de pedidos por categoria (informação, reserva, alteração, reclamação).
- SOPs curtos criados a partir de explicações faladas da equipa (transcrição + IA).
- Resumo semanal automático do quadro Trello para a direção.

**Riscos e limitações**
- **Alucinações**: a IA pode inventar preços, horários ou políticas de cancelamento.
- **Privacidade**: dados de clientes (nomes, passaportes, pagamentos) não devem ser
  colados em ferramentas de IA públicas (RGPD).
- **Tom genérico**: respostas "de robô" prejudicam uma marca de experiências locais.
- **Dependência**: a equipa deixar de rever o que envia.
- **Adoção**: equipa pequena e ocupada; processos complexos não serão usados.

---

## Parte 2 - Estratégia de trabalho

**Objetivos principais**
- Reduzir o tempo de primeira resposta a clientes e torná-la consistente.
- Dar à equipa um processo simples, documentado e repetível com apoio de IA.
- Propor à direção um piloto de 3 meses com fases e indicadores claros.

**Outputs selecionados**
1. **Email profissional** à direção: diagnóstico e proposta de projeto piloto.
2. **SOP simples**: "Resposta a pedidos de clientes com apoio de IA".

**Ferramentas**
| Etapa | Ferramenta |
|---|---|
| Análise e geração | ChatGPT ou Claude |
| Crítica do output | Segunda conversa (ou outra ferramenta) no papel de revisor |
| Edição e versão final | Google Docs |
| Contexto do cliente | Trello, Slack, Google Meet (referidos no SOP) |

**Workflow definido (v1)**
1. Ler o caso e extrair desafios e prioridades.
2. Escrever prompt estruturado (Papel, Contexto, Tarefa, Formato, Restrições).
3. Gerar a versão inicial.
4. Pedir à IA uma crítica com critérios explícitos.
5. Refinar o prompt e gerar nova versão.
6. Validação humana (factos, tom, privacidade, utilidade).
7. Versão final no Google Docs.

**Critérios de validação**
| Critério | Pergunta de controlo |
|---|---|
| Clareza | Um colaborador novo percebe o que fazer à primeira leitura? |
| Exatidão | Há algum número, prazo ou política que a IA tenha inventado? |
| Adequação | O tom é profissional, próximo e coerente com uma marca de turismo? |
| Utilidade | Resolve um problema real do caso? Tem próximo passo claro? |
| Concisão | Pode ser lido em menos de 2 minutos? |
| Privacidade | Exige colar dados pessoais na IA? (tem de ser "não") |

---

## Parte 3 - Prompting e produção de outputs

### OUTPUT 1 - Email à direção

**Prompt inicial**
```
Escreve um email para uma empresa de turismo a propor melhorar a produtividade com IA.
```

**Output inicial (resumo do que a IA devolveu)**
> Assunto: Proposta de Colaboração
> Caro(a) Cliente, espero que esteja bem. A Inteligência Artificial está a revolucionar o
> setor do turismo. Com as nossas soluções inovadoras podemos aumentar a sua produtividade
> em 50% e reduzir custos significativamente. Oferecemos chatbots, automação de marketing,
> análise de dados e muito mais. Ficaria encantado em agendar uma reunião...

**Problemas identificados**
- Genérico: não menciona a Cabo Digital Travel nem nenhum dos seus problemas.
- **Inventa um número** ("50%") sem base.
- Lista de serviços tipo catálogo, sem prioridade nem plano.
- Sem proposta concreta nem próximo passo com data.

**Prompt de crítica (iteração 2)**
```
Age como diretor de operações de uma pequena empresa de turismo que recebe muitas
propostas de freelancers. Avalia o email abaixo de 1 a 5 em: personalização, clareza,
credibilidade, proposta concreta e próximo passo. Indica as 3 alterações mais importantes.
[email]
```
Resposta resumida: personalização 1, credibilidade 2 (número sem fonte), proposta concreta 1;
alterações: referir os problemas reais, propor um piloto pequeno com fases, retirar promessas
não fundamentadas.

**Prompt refinado (iteração 3, P-C-T-F-R)**
```
Papel: és um consultor freelancer de operações digitais e IA aplicada, a trabalhar
remotamente.
Contexto: a Cabo Digital Travel (turismo e experiências locais, equipa pequena e
parcialmente remota, usa Google Workspace, Trello, Slack e Google Meet) cresceu com a
promoção digital e tem: demora na resposta a clientes, comunicação inconsistente, tarefas
desorganizadas, muitas tarefas repetitivas e nenhuma documentação padronizada. Quer uma
colaboração inicial de 3 meses começando por um piloto.
Tarefa: escreve o primeiro email para a direção, a mostrar que percebi os problemas e a
propor um projeto piloto.
Formato: português de Portugal; assunto específico; máximo 220 palavras; 1 parágrafo de
diagnóstico, piloto em 3 fases com um resultado por fase, próximo passo com proposta de
reunião de 30 min.
Restrições: não inventes números nem resultados garantidos; usa "[a confirmar]" quando
precisares de um valor; não prometas ferramentas que a empresa não usa; tom profissional e
próximo, sem jargão.
```

**Melhorias realizadas**
- Personalização com os problemas do caso; piloto em fases alinhado com os 3 meses.
- Remoção de promessas não fundamentadas; indicadores ficam "a confirmar" na reunião.
- Revisão humana: encurtei o 1.º parágrafo, troquei "solução" por exemplos concretos,
  adicionei duas datas alternativas e verifiquei que só são referidas ferramentas que o
  cliente já usa.

**Versão final**
> **Assunto:** Piloto de 3 meses para acelerar a resposta a clientes - Cabo Digital Travel
>
> Bom dia,
>
> Pelo que partilharam, o crescimento dos últimos meses trouxe três pontos de pressão: os
> clientes esperam demasiado por uma resposta, a comunicação varia consoante quem responde
> e muitas tarefas repetitivas ocupam tempo da equipa. Isto acontece com frequência quando
> uma equipa pequena cresce sem processos escritos, e resolve-se melhor por etapas.
>
> Proponho um piloto de 3 meses, com as ferramentas que já usam (Google Workspace, Trello,
> Slack):
>
> 1. **Mês 1 - Resposta a clientes:** biblioteca de respostas-modelo em PT/EN/FR e um
>    procedimento simples de resposta com apoio de IA, sempre revisto pela equipa.
> 2. **Mês 2 - Organização:** quadro Trello com regras de prioridade e 3 a 5 SOPs das
>    tarefas mais repetidas.
> 3. **Mês 3 - Escala:** resumo semanal automático para a direção e plano para conteúdos.
>
> Na primeira reunião definimos juntos os indicadores de sucesso (por exemplo, tempo médio
> de primeira resposta: atual [a confirmar] / objetivo [a definir]).
>
> Tem disponibilidade para uma chamada de 30 minutos no Google Meet na terça ou na quinta
> de manhã?
>
> Com os melhores cumprimentos,
> [Nome] | Consultor de operações digitais e IA aplicada

### OUTPUT 2 - SOP "Resposta a pedidos de clientes com apoio de IA"

**Prompt inicial**
```
Cria um procedimento para responder a clientes usando IA.
```

**Output inicial (resumo)**
> 1. Receber a mensagem. 2. Copiar a mensagem do cliente para o ChatGPT. 3. Pedir uma
> resposta. 4. Enviar a resposta. 5. Registar no sistema. Dica: use a IA para responder
> mais depressa a todos os clientes.

**Problemas identificados**
- **Risco de privacidade**: manda colar a mensagem completa (com dados pessoais) na IA.
- Sem revisão humana: a resposta é enviada tal como sai.
- Não distingue tipos de pedido (uma reclamação não pode ser tratada como um pedido de
  informação).
- Não diz quem faz, em que ferramenta, nem em quanto tempo.

**Prompt refinado (P-C-T-F-R)**
```
Papel: és um especialista em operações de atendimento para PME de turismo.
Contexto: Cabo Digital Travel, equipa pequena e parcialmente remota, pedidos por email e
WhatsApp em PT, EN e FR, usa Google Workspace, Trello e Slack. Problemas: demora e
inconsistência nas respostas.
Tarefa: escreve um SOP de uma página para responder a pedidos de clientes com apoio de IA.
Formato: objetivo, âmbito, responsáveis, tabela de categorias com prazo de resposta e se a
IA pode ser usada, passos numerados (máx. 8), checklist de revisão, regras de privacidade.
Restrições: a IA nunca recebe dados pessoais (nomes, contactos, documentos, pagamentos);
reclamações e pedidos de reembolso são tratados por uma pessoa; nenhuma resposta sai sem
revisão humana; prazos como propostas "[a validar]".
```

**Melhorias realizadas**
- Anonimização antes de usar IA; revisão humana obrigatória; categorias com prazos.
- Revisão humana: retirei um passo de "resposta automática no WhatsApp" que a IA sugeriu
  (a empresa não tem essa integração); simplifiquei de 11 para 8 passos; acrescentei o
  canal de Slack para escalar casos.

**Versão final**

> **SOP-01 | Resposta a pedidos de clientes com apoio de IA** · v1.0 · Responsável: [a definir]
>
> **Objetivo:** responder mais depressa e com tom consistente, sem perder qualidade nem
> expor dados de clientes.
> **Âmbito:** pedidos recebidos por email e WhatsApp (PT, EN, FR).
>
> | Categoria | Exemplo | Prazo de 1.ª resposta | IA pode redigir? |
> |---|---|---|---|
> | Informação | horários, preços, o que inclui | 4 h úteis [a validar] | Sim, com base nas respostas-modelo |
> | Reserva | marcar uma experiência | 4 h úteis [a validar] | Sim, a pessoa confirma disponibilidade |
> | Alteração | mudar data, nº de pessoas | 8 h úteis [a validar] | Sim, a pessoa confirma política |
> | Reclamação / reembolso | experiência correu mal | 24 h [a validar] | Só para melhorar a redação; decisão humana |
>
> **Passos**
> 1. Classificar o pedido numa das 4 categorias e criar cartão no Trello (lista "Pedidos").
> 2. Procurar a resposta-modelo correspondente na pasta partilhada "Respostas-modelo".
> 3. Se for preciso adaptar, **anonimizar** o pedido: retirar nomes, contactos, nº de
>    reserva e dados de pagamento.
> 4. Usar o prompt padrão da marca (tom próximo, profissional, na língua do cliente) para
>    adaptar a resposta-modelo.
> 5. **Rever**: factos (preço, horário, política) confirmados na fonte oficial; tom; língua.
> 6. Repor os dados do cliente e enviar.
> 7. Atualizar o cartão no Trello; reclamações vão também para `#atendimento` no Slack.
> 8. Se a mesma pergunta aparecer 3 vezes na semana, propor nova resposta-modelo.
>
> **Checklist antes de enviar:** ☐ factos verificados ☐ sem dados pessoais colados na IA
> ☐ nome do cliente correto ☐ língua e tom adequados ☐ próximo passo claro para o cliente.
>
> **Privacidade:** nunca colar em ferramentas de IA documentos de identificação, dados de
> pagamento ou contactos. Em caso de dúvida, não usar IA nesse pedido.

---

## Parte 4 - Revisão crítica e otimização

**Principais limitações identificadas**
- Os primeiros outputs eram genéricos e inventaram dados ("50% de produtividade").
- A IA sugeriu passos inseguros (colar dados pessoais) e integrações inexistentes.
- A IA não conhece as políticas reais do cliente (preços, cancelamentos): esses factos
  têm sempre de vir de uma fonte da empresa.

**Melhorias implementadas**
- Prompt estruturado P-C-T-F-R com restrições explícitas.
- Iteração de crítica com a IA no papel do cliente, antes de refinar.
- Marcador `[a confirmar]` em vez de números inventados.
- Revisão humana com checklist de 6 critérios em ambos os outputs.

**Estratégias utilizadas**
- Prompting iterativo em 3 passos: gerar → criticar com critérios → refinar.
- *Role prompting* (a IA como cliente exigente para avaliar).
- Restrições de formato (limite de palavras, secções fixas) para outputs mais utilizáveis.

**Aprendizagens principais**
- A qualidade do output depende mais do contexto e das restrições do que da ferramenta.
- A IA acelera o primeiro rascunho, mas o valor profissional está na validação e na
  adaptação ao cliente.
- Pedir à IA que se critique a si própria é rápido e revela problemas que eu não via.

---

## Parte 5 - Apresentação e discussão (pontos a apresentar)
- Análise: 7 desafios, prioridade à resposta a clientes.
- Workflow: 7 passos com validação humana obrigatória.
- Prompts: do genérico ao P-C-T-F-R, com iteração de crítica.
- Outputs: email com piloto de 3 meses; SOP-01 de resposta a clientes.
- Riscos: alucinações, privacidade, tom genérico, dependência.

---

## Parte 6 - Laboratório assíncrono: workflow otimizado (v2)

**O que mudou face à v1**
| v1 (sessão síncrona) | v2 (otimizado) | Porquê |
|---|---|---|
| Prompt escrito de raiz em cada tarefa | **Prompt-base reutilizável** com o contexto do cliente | Poupa tempo e garante consistência |
| Crítica livre | Crítica com **grelha fixa de 5 critérios** (1-5) | Comparar versões de forma objetiva |
| Validação no fim | **Ponto de privacidade no início** (anonimizar antes de usar IA) | O risco acontece ao colar os dados |
| Uma ferramenta | Gerar numa ferramenta, **rever noutra** | Reduz o enviesamento da mesma IA |
| Sem registo | **Registo de versões** (v1, v2, final) e prompts no Google Docs | Evidência e melhoria contínua |

**Workflow final estruturado**
```
1. BRIEFING      Ler o pedido; definir objetivo, público e output (5 min)
2. PRIVACIDADE   Anonimizar dados; decidir se a IA pode ser usada (1 min)
3. PROMPT        Prompt-base do cliente + tarefa + formato + restrições (3 min)
4. GERAR v1      ChatGPT/Claude (1-2 min)
5. CRITICAR      Grelha: personalização, clareza, exatidão, proposta, próximo passo (2 min)
6. REFINAR v2    Ajustar o prompt com as 3 alterações principais (2 min)
7. VALIDAR       Revisão humana: factos na fonte, tom, checklist (5 min)
8. ENTREGAR      Versão final no Google Docs; registar prompt e versões (2 min)
9. MELHORAR      Pedido repetido 3x → criar modelo/SOP novo
```

**Prompt-base reutilizável (cliente Cabo Digital Travel)**
```
Contexto fixo: trabalho como consultor freelancer para a Cabo Digital Travel, empresa de
turismo e experiências locais, equipa pequena e parcialmente remota (Google Workspace,
Trello, Slack, Meet). Tom da marca: próximo, profissional, acolhedor, sem jargão. Línguas:
PT-PT, EN, FR. Regras: não inventar preços, prazos ou políticas (usar "[a confirmar]");
não pedir nem usar dados pessoais; propor sempre um próximo passo.
Tarefa: ...
Formato: ...
```

**Iteração extra (aplicação do workflow v2 ao email)**

Grelha de avaliação (feita pela IA, conferida por mim):
| Critério | Inicial | Final (Parte 3) | Final v2 |
|---|---|---|---|
| Personalização | 1 | 4 | 5 |
| Clareza | 3 | 4 | 5 |
| Exatidão / credibilidade | 2 | 5 | 5 |
| Proposta concreta | 1 | 4 | 5 |
| Próximo passo | 2 | 4 | 5 |

Alteração da v2: um resultado mensurável por fase ("Mês 1: biblioteca com as 15 perguntas
mais frequentes em 3 línguas") e um anexo de uma página com o plano, para o email continuar
curto.

**Ganhos de produtividade estimados (pessoais, não do cliente)**
| Tarefa | Sem IA (estimativa) | Com workflow v2 |
|---|---|---|
| Email de proposta personalizado | ~45 min | ~20 min |
| SOP de uma página | ~90 min | ~30 min |

O tempo poupado está sobretudo no primeiro rascunho. A validação humana continua a
demorar o mesmo, e deve.

---

## Parte 7 - Reflexão crítica

**Dificuldades.** O primeiro resultado parecia bom à primeira vista, mas era genérico e
tinha um número inventado. A maior dificuldade não foi gerar texto: foi perceber o que
estava errado num texto bem escrito.

**Estratégias de prompting.** Passei de um pedido de uma linha para um prompt estruturado
(papel, contexto, tarefa, formato, restrições) e introduzi uma iteração de crítica, com a
IA a fazer de cliente exigente. Na v2 criei um prompt-base reutilizável, que é o que mais
acelera trabalho repetido para o mesmo cliente.

**Diferenças entre versões.** A versão inicial falava de "IA no turismo"; a final fala dos
problemas da Cabo Digital Travel, propõe um piloto em fases com as ferramentas que já usam
e deixa os indicadores para acordar com o cliente. No SOP, a versão inicial criava um
risco de RGPD; a final começa precisamente pela anonimização.

**Ganhos de produtividade.** Reduzi para menos de metade o tempo do primeiro rascunho. O
maior ganho não é escrever mais depressa: é ter um processo repetível, que a equipa do
cliente também pode usar.

**Limitações dos outputs de IA.** Inventa dados com confiança, tende para o genérico,
sugere integrações que não existem e não conhece as políticas reais da empresa.

**Importância da validação humana.** Os dois erros mais graves (número inventado e dados
pessoais na IA) só foram travados pela revisão. Num contexto de turismo, um preço ou uma
política errada enviada a um cliente custa dinheiro e reputação. Por isso a validação está
no workflow como passo obrigatório e não como opção.

**Melhorias possíveis.** Testar as respostas-modelo com casos reais anonimizados; medir o
tempo de primeira resposta antes e depois do piloto; criar um guia de tom de voz da marca
para incluir no prompt-base; avaliar mais tarde uma automação simples (por exemplo,
formulário → cartão Trello) só depois de o processo manual estar estável.

**Utilização estratégica da IA.** Usar IA estrategicamente não é automatizar tudo: é
escolher as tarefas onde acelera (rascunhos, estrutura, tradução, crítica) e manter nas
pessoas as decisões, os factos e a relação com o cliente.
