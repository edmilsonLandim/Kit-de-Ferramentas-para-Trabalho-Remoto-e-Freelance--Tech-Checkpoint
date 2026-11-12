# AI Productivity Sprint - Workflow Profissional Assistido por IA

**Sessão 1 - AI Literacy para Produtividade** | Percurso Upskilling | Entregáveis 1
**Cliente (estudo de caso):** Cabo Digital Travel - turismo e experiências locais
**Papel:** freelancer / consultor digital em regime remoto
**Ferramenta de IA:** Claude (Anthropic), modelo Claude Opus 5.5 - conversa de 12/11/2026
**Outras ferramentas:** Google Docs (edição e versão final); Trello, Slack e Google Meet
(ferramentas do cliente, referidas nos outputs)

> Os outputs de IA estão transcritos sem edição. Por baixo de cada um indico o que alterei
> na revisão humana. Registo completo da conversa:
> `lab-assincrono/evidencias/conversa-claude-2026-11-12.md`.

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
4. Conteúdos e automações mais avançadas ficam para depois do piloto.

**Oportunidades de melhoria**
- Biblioteca de respostas-modelo multilingues (PT/EN/FR) geradas e revistas com IA.
- Prompt padrão com o tom de voz da marca, usado por toda a equipa.
- Triagem de pedidos por categoria (informação, reserva, alteração, reclamação).
- SOPs curtos criados a partir de explicações da equipa (transcrição + IA).
- Resumo semanal do quadro Trello para a direção.

**Riscos e limitações**
- **Alucinações**: a IA pode inventar preços, horários ou políticas de cancelamento.
- **Privacidade**: dados de clientes (nomes, contactos, documentos, pagamentos) não devem
  ser colados em ferramentas de IA (RGPD).
- **Tom genérico**: respostas "de robô" prejudicam uma marca de experiências locais.
- **Dependência**: a equipa deixar de rever o que envia.
- **Adoção**: equipa pequena e ocupada; processos complexos não serão usados.

---

## Parte 2 - Estratégia de trabalho

**Objetivos principais**
- Reduzir o tempo de primeira resposta a clientes e torná-la consistente.
- Dar à equipa um processo simples, documentado e repetível com apoio de IA.
- Propor à direção um piloto de 3 meses com fases e entregas claras.

**Outputs selecionados**
1. **Email profissional** à direção: diagnóstico e proposta de projeto piloto.
2. **SOP simples**: "Resposta a pedidos de clientes com apoio de IA".

**Ferramentas**
| Etapa | Ferramenta |
|---|---|
| Geração e crítica | Claude (o mesmo modelo, em papéis diferentes: autor e cliente exigente) |
| Edição e versão final | Google Docs |
| Contexto do cliente | Trello, Slack, Google Meet (referidos nos outputs) |

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

**Output inicial**
> **Assunto:** Proposta: Aumentar a produtividade da vossa equipa com Inteligência Artificial
>
> Exmos. Senhores,
>
> O meu nome é [Nome] e trabalho como consultor em transformação digital, ajudando empresas
> do setor do turismo a tirar partido da Inteligência Artificial no dia a dia.
>
> Sabemos que o turismo é um setor exigente: pedidos de clientes a qualquer hora, várias
> línguas, reservas, parceiros e uma forte pressão para estar presente online. A IA pode
> ajudar a vossa equipa a responder mais depressa e a dedicar mais tempo ao que realmente
> importa: a experiência do cliente.
>
> Algumas áreas onde podemos começar:
> - **Atendimento ao cliente:** respostas rápidas e personalizadas a emails e mensagens, em várias línguas;
> - **Marketing e conteúdos:** criação de publicações, descrições de experiências e newsletters;
> - **Gestão de reservas:** automatização de confirmações, lembretes e follow-ups;
> - **Análise de dados:** identificação de tendências de procura e de avaliações de clientes;
> - **Tarefas administrativas:** relatórios, resumos de reuniões e documentação interna.
>
> Empresas que adotam estas ferramentas conseguem poupar várias horas por semana e melhorar
> a satisfação dos clientes.
>
> Gostaria de agendar uma breve reunião para perceber as vossas necessidades e apresentar
> uma proposta à medida. Teria disponibilidade nas próximas semanas?
>
> Com os melhores cumprimentos,
> [Nome]

**Problemas identificados**
- Bem escrito, mas genérico: não menciona a Cabo Digital Travel nem os seus problemas.
- Afirmação sem prova: "poupar várias horas por semana".
- Lista de 5 serviços tipo catálogo, sem prioridade nem plano.
- Próximo passo vago ("nas próximas semanas").

**Prompt de crítica (iteração 2)**
```
Age como diretor de operações de uma pequena empresa de turismo que recebe muitas
propostas de freelancers. Avalia o email abaixo de 1 a 5 em: personalização, clareza,
credibilidade, proposta concreta e próximo passo. Indica as 3 alterações mais importantes.
[email]
```
Resposta da IA: personalização **1**, clareza **4**, credibilidade **2**, proposta concreta
**1**, próximo passo **2**. Alterações: (1) mostrar que conhece os problemas da empresa;
(2) trocar a lista de serviços por um piloto pequeno com início, duração e resultado;
(3) próximo passo concreto e sem afirmações sem prova.

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
- Pela IA (iteração 3): personalização com os problemas do caso; piloto em 3 fases
  alinhado com os 3 meses; sem números inventados; indicador marcado "[a confirmar]".
- Na revisão humana:
  - retirei "é uma ótima notícia, mas" (demasiado informal num primeiro contacto);
  - troquei "na próxima semana" por duas opções concretas ("terça ou quinta de manhã");
  - confirmei que só são referidas ferramentas que o cliente já usa.

**Versão final**
> **Assunto:** Proposta de piloto de 3 meses – resposta a clientes e organização da equipa
>
> Bom dia,
>
> Obrigado pela partilha do contexto da Cabo Digital Travel. Percebo que o crescimento dos
> últimos meses trouxe pressão em pontos concretos: clientes que esperam demasiado por uma
> resposta, comunicação que varia consoante quem responde, tarefas difíceis de priorizar e
> muito tempo gasto em trabalho repetitivo, sem procedimentos escritos.
>
> Proponho começar com um piloto de 3 meses, usando as ferramentas que já utilizam (Google
> Workspace, Trello, Slack e Meet):
>
> 1. **Mês 1 – Comunicação com clientes:** respostas-modelo para os pedidos mais frequentes
>    e um prompt com o tom da marca. *Resultado:* respostas mais rápidas e consistentes.
> 2. **Mês 2 – Organização:** quadro Trello com regras de prioridade e procedimentos
>    escritos para as tarefas mais repetidas. *Resultado:* menos dependência de pessoas-chave.
> 3. **Mês 3 – Consolidação:** rever o que funcionou, ajustar e preparar os passos
>    seguintes. *Resultado:* um processo estável que a equipa usa sem apoio.
>
> Os indicadores de sucesso, como o tempo médio de resposta (atual: [a confirmar]), seriam
> definidos convosco na primeira reunião.
>
> Teriam disponibilidade para uma conversa de 30 minutos no Google Meet na terça ou na
> quinta de manhã?
>
> Com os melhores cumprimentos,
> [Nome]
> Consultor de operações digitais e IA aplicada

### OUTPUT 2 - SOP "Resposta a pedidos de clientes com apoio de IA"

**Prompt inicial**
```
Cria um procedimento para responder a clientes usando IA.
```

**Output inicial**
> **Procedimento: Resposta a Clientes com Apoio de IA**
>
> 1. **Receção e leitura da mensagem** – ler a mensagem na íntegra e identificar o pedido
>    principal e o tom do cliente.
> 2. **Classificação** – identificar o tipo de pedido (informação, reclamação, pedido de
>    serviço, suporte técnico) e o nível de urgência.
> 3. **Preparação do prompt** – fornecer à IA o contexto necessário: mensagem do cliente,
>    informação relevante (produto, encomenda, políticas) e tom desejado. Exemplo: *"És um
>    assistente de apoio ao cliente da empresa X. Responde à seguinte mensagem de forma
>    cordial e profissional: [mensagem do cliente]"*.
> 4. **Geração da resposta** – gerar a resposta e, se necessário, pedir ajustes.
> 5. **Revisão humana** – verificar exatidão da informação, tom e personalização.
> 6. **Envio** – enviar pelo canal original.
> 7. **Registo e follow-up** – registar a interação e agendar seguimento, se aplicável.
>
> **Boas práticas:** não partilhar dados sensíveis (dados de cartão, palavras-passe) com a
> IA; criar uma biblioteca de prompts; rever periodicamente as respostas.

**Problemas identificados**
- **Privacidade**: o passo 3 manda colar a mensagem completa do cliente na IA, e as boas
  práticas só excluem cartões e palavras-passe (ficam de fora nomes, contactos,
  documentos e números de reserva).
- Genérico: categorias de comércio eletrónico ("encomenda", "suporte técnico") que não
  servem uma empresa de turismo; sem línguas, canais nem ferramentas do cliente.
- Reclamações seguem o mesmo fluxo que um pedido de informação.
- Sem prazos de resposta nem responsáveis.
- Ponto positivo a manter: já incluía revisão humana antes do envio.

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
- Pela IA: anonimização antes de usar IA; categorias de turismo com prazos; responsáveis;
  reclamações com decisão humana; checklist e regras de privacidade.
- Na revisão humana:
  - **retirei a categoria "Parceiros"**: saía do âmbito (pedidos de clientes) e merece
    um SOP próprio;
  - **passei o encaminhamento de reclamações do passo 8 para o passo 2**: no output da
    IA a reclamação só era encaminhada depois de já ter passado pela IA e pela redação;
  - **acrescentei o passo de partir das respostas-modelo**, que a IA não incluiu e é o
    que mais acelera a resposta;
  - marquei o canal "#operações" como "[a confirmar]": foi a IA que o sugeriu, não
    sabemos se existe.

**Versão final**

> **SOP-01 | Resposta a pedidos de clientes com apoio de IA**
> Cabo Digital Travel · v1.0 · Revisão: [a validar]
>
> **Objetivo:** responder de forma rápida, consistente e correta aos pedidos de clientes,
> com apoio de IA e sem expor dados pessoais.
> **Âmbito:** pedidos de clientes recebidos por email e WhatsApp, em PT, EN e FR.
> **Responsáveis:** atendimento (quem estiver de turno) classifica, prepara e envia;
> responsável de operações trata reclamações, reembolsos e exceções; direção aprova
> alterações a preços e políticas.
>
> | Categoria | Exemplos | Prazo 1.ª resposta | Uso de IA |
> |---|---|---|---|
> | Informação | preços, horários, o que inclui | 4 h úteis [a validar] | Sim |
> | Reserva | nova reserva, disponibilidade | 4 h úteis [a validar] | Sim, após confirmar disponibilidade |
> | Alteração / cancelamento | mudança de data, nº de pessoas | 8 h úteis [a validar] | Sim, após confirmar a política |
> | Reclamação / reembolso | problema na experiência | 24 h [a validar] | Só para rever a redação; decisão humana |
>
> **Passos**
> 1. Ler o pedido, classificá-lo e registá-lo no Trello (lista "Pedidos em curso") com
>    categoria e prazo.
> 2. Reclamação ou reembolso? Encaminhar já no Slack (#operações [a confirmar]) para o
>    responsável de operações, que decide a resposta.
> 3. Procurar a resposta-modelo correspondente na pasta partilhada "Respostas-modelo".
> 4. Se for preciso adaptar, retirar da mensagem todos os dados pessoais (nome, email,
>    telefone, nº de reserva, documentos, pagamentos).
> 5. Colar na IA o pedido anonimizado e a resposta-modelo, com o prompt padrão da empresa
>    e a língua do cliente.
> 6. Confirmar na fonte oficial (tabela de preços, calendário, política de cancelamento)
>    todos os factos da resposta.
> 7. Rever tom e língua, repor o nome do cliente e os dados necessários, e enviar.
> 8. Mover o cartão para "Respondido". Se a mesma pergunta surgir 3 vezes na semana,
>    propor nova resposta-modelo.
>
> **Checklist de revisão:** ☐ factos confirmados na fonte ☐ sem dados pessoais na IA
> ☐ nome e língua corretos ☐ tom da marca ☐ próximo passo claro para o cliente.
>
> **Privacidade:** a IA só recebe texto anonimizado. Nunca colar documentos de
> identificação, dados de pagamento, contactos ou números de reserva. Em caso de dúvida,
> responder sem IA.

---

## Parte 4 - Revisão crítica e otimização

**Principais limitações identificadas**
- Os prompts genéricos deram textos bem escritos mas vazios: serviam para qualquer
  empresa e incluíam afirmações sem prova ("poupar várias horas por semana").
- No SOP inicial, a IA mandava colar a mensagem completa do cliente, com uma regra de
  privacidade incompleta.
- Mesmo com um bom prompt, a IA criou uma categoria fora do âmbito, pôs as reclamações no
  fim do processo e inventou um canal de Slack.
- A IA não conhece as políticas reais do cliente (preços, cancelamentos): esses factos
  têm sempre de vir de uma fonte da empresa.

**Melhorias implementadas**
- Prompt estruturado P-C-T-F-R com restrições explícitas.
- Iteração de crítica com a IA no papel do cliente, antes de refinar.
- Marcadores "[a confirmar]" / "[a validar]" em vez de valores inventados.
- Revisão humana com checklist de 6 critérios nos dois outputs.

**Estratégias utilizadas**
- Prompting iterativo: gerar → criticar com critérios → refinar → rever.
- *Role prompting*: a IA como cliente exigente para avaliar o email.
- Restrições de formato (limite de palavras, secções fixas) para outputs mais utilizáveis.

**Aprendizagens principais**
- A qualidade do output depende mais do contexto e das restrições do que da ferramenta.
- A IA acelera o primeiro rascunho, mas o valor profissional está na validação e na
  adaptação ao cliente.
- Um output bem formatado pode ter erros de lógica (ordem dos passos) que só uma leitura
  atenta apanha.

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
| Crítica livre | Crítica com **grelha fixa de 5 critérios** (1-5), aplicada a todas as versões | Comparar versões de forma objetiva |
| Validação no fim | **Ponto de privacidade no início** (anonimizar antes de usar IA) | O risco acontece ao colar os dados |
| Revisão só do texto | Revisão também da **lógica e da ordem** dos passos | Foi onde a IA errou no SOP |
| Sem registo | **Registo de versões e prompts** (ficheiro de evidências) | Evidência e melhoria contínua |

**Workflow final estruturado**
```
1. BRIEFING      Ler o pedido; definir objetivo, público e output
2. PRIVACIDADE   Anonimizar dados; decidir se a IA pode ser usada
3. PROMPT        Prompt-base do cliente + tarefa + formato + restrições
4. GERAR v1      Claude / ChatGPT
5. CRITICAR      Grelha: personalização, clareza, credibilidade, proposta, próximo passo
6. REFINAR v2    Ajustar o prompt com as alterações principais da crítica
7. VALIDAR       Revisão humana: factos na fonte, tom, lógica, checklist
8. ENTREGAR      Versão final no Google Docs; registar prompts e versões
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

**Iteração extra: workflow v2 aplicado ao email**

Avaliei a versão final da Parte 3 com a grelha. A IA deu 4 em personalização, clareza,
credibilidade e proposta concreta, e 5 no próximo passo. Sugeriu dar a cada fase uma
entrega verificável e passar o detalhe para um anexo. Prompt usado:
```
[prompt-base Cabo Digital Travel]
Tarefa: melhora o email abaixo aplicando a sugestão da avaliação: uma entrega verificável
por fase e referência a um anexo de uma página com o plano.
Formato: manter máximo 220 palavras e a mesma estrutura.
[versão final do email]
```

**Versão melhorada (v2)**
> **Assunto:** Piloto de 3 meses para acelerar a resposta a clientes – Cabo Digital Travel
>
> Bom dia,
>
> Obrigado pela partilha do contexto da Cabo Digital Travel. O crescimento dos últimos meses
> trouxe pressão em pontos concretos: clientes que esperam demasiado por uma resposta,
> comunicação que varia consoante quem responde e muito tempo gasto em tarefas repetitivas,
> sem procedimentos escritos.
>
> Proponho um piloto de 3 meses com as ferramentas que já utilizam (Google Workspace,
> Trello, Slack e Meet), com uma entrega verificável por mês:
>
> 1. **Mês 1 – Comunicação com clientes:** biblioteca com respostas-modelo para as 15
>    perguntas mais frequentes, em PT, EN e FR, e um prompt com o tom da marca.
> 2. **Mês 2 – Organização:** quadro Trello com regras de prioridade e 3 a 5 procedimentos
>    escritos das tarefas mais repetidas.
> 3. **Mês 3 – Consolidação:** relatório de resultados face aos indicadores acordados e
>    plano para a fase seguinte.
>
> Em anexo envio o plano numa página. Os indicadores (por exemplo, tempo médio de primeira
> resposta – atual [a confirmar]) seriam definidos convosco na primeira reunião.
>
> Teriam disponibilidade para 30 minutos no Google Meet na terça ou na quinta de manhã?
>
> Com os melhores cumprimentos,
> [Nome]
> Consultor de operações digitais e IA aplicada

Revisão humana da v2: aceite sem alterações. As "15 perguntas" são um âmbito de trabalho
que eu proponho, não um resultado prometido; ficam para confirmar na reunião.

**Evolução das versões (grelha 1-5, avaliação da IA conferida por mim)**
| Critério | Inicial | Final (Parte 3) | v2 |
|---|---|---|---|
| Personalização | 1 | 4 | 5 |
| Clareza | 4 | 4 | 5 |
| Credibilidade | 2 | 4 | 4 |
| Proposta concreta | 1 | 4 | 5 |
| Próximo passo | 2 | 5 | 5 |

A credibilidade fica em 4 porque o email ainda não mostra trabalho anterior. A melhoria
seguinte seria juntar um link para o portfólio, que vou construir neste módulo.

**Anexo do email - plano do piloto (1 página)**
| Mês | Entrega | Como se verifica |
|---|---|---|
| 1 | 15 respostas-modelo em PT/EN/FR + prompt de tom da marca + SOP-01 | Pasta partilhada revista e aprovada pela direção |
| 2 | Quadro Trello com regras de prioridade + 3 a 5 SOPs | Equipa usa o quadro numa semana de trabalho normal |
| 3 | Relatório de resultados + plano da fase seguinte | Indicadores comparados com o ponto de partida |

**Ganhos de produtividade (estimativa pessoal)**
| Tarefa | Sem IA (estimativa) | Com workflow v2 |
|---|---|---|
| Email de proposta personalizado | ~45 min | ~20 min |
| SOP de uma página | ~90 min | ~30 min |

O tempo poupado está sobretudo no primeiro rascunho. A validação humana continua a demorar
o mesmo, e deve.

---

## Parte 7 - Reflexão crítica

**Dificuldades.** Os primeiros outputs pareciam bons: bem escritos, organizados e
educados. A dificuldade não foi gerar texto, foi perceber o que estava errado num texto bem
escrito. O email servia para qualquer empresa e o procedimento mandava colar a mensagem do
cliente na IA.

**Estratégias de prompting.** Passei de pedidos de uma linha para prompts estruturados
(papel, contexto, tarefa, formato, restrições) e introduzi uma iteração de crítica com a IA
no papel de cliente exigente. Na v2 criei um prompt-base reutilizável, que é o que mais
acelera trabalho repetido para o mesmo cliente.

**Diferenças entre versões.** O email passou de uma lista de serviços para um piloto em 3
fases com uma entrega verificável por mês, sem promessas sem prova. O SOP passou de 7
passos genéricos para um procedimento de turismo com categorias, prazos, responsáveis e
anonimização obrigatória antes de usar IA.

**Ganhos de produtividade.** Reduzi para menos de metade o tempo do primeiro rascunho. O
maior ganho é ter um processo repetível, que a equipa do cliente também pode usar.

**Limitações dos outputs de IA.** Tende para o genérico, faz afirmações sem prova, não
conhece as políticas reais da empresa e, mesmo com instruções claras, cometeu erros de
lógica (reclamações tratadas no fim do processo) e inventou um detalhe (o canal de Slack).

**Importância da validação humana.** Os erros mais importantes, a privacidade no SOP
inicial e a ordem dos passos no SOP refinado, só foram travados pela revisão. Num contexto
de turismo, uma política errada ou uma reclamação mal encaminhada custa dinheiro e
reputação. Por isso a validação está no workflow como passo obrigatório.

**Melhorias possíveis.** Testar as respostas-modelo com casos reais anonimizados; medir o
tempo de primeira resposta antes e depois do piloto; criar um guia de tom de voz da marca
para o prompt-base; gerar numa ferramenta e rever noutra para reduzir enviesamentos; mais
tarde, avaliar uma automação simples (formulário → cartão Trello) só quando o processo
manual estiver estável.

**Utilização estratégica da IA.** Usar IA estrategicamente não é automatizar tudo: é
escolher as tarefas onde ela acelera (rascunhos, estrutura, tradução, crítica) e manter nas
pessoas as decisões, os factos e a relação com o cliente.
