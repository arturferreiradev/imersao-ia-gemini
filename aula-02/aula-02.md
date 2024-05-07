# Aula 02: Melhores técnicas em Engenharia de Prompt

## Introdução

Nesta aula, pude aprender diferentes técnicas de prompt utilizadas em Inteligência Artificial (IA). Foi abordado o conceito de prompt, destacado as melhores práticas para criar prompts eficazes e discutir três técnicas específicas: Zero-shot prompting, Few-shot prompting e Few-shot Chain-of-Thought prompting.

## Conceito de Prompt

Um prompt é uma instrução ou entrada fornecida a um modelo de IA para orientar sua geração de texto. É a forma como os humanos interagem com modelos de linguagem para obter respostas específicas ou realizar tarefas desejadas. Um prompt pode ser uma pergunta, uma declaração incompleta ou até mesmo um contexto inicial para a geração de texto.

## Melhores Práticas para Criar Prompts

1. **Clareza e Concisão**: O prompt deve ser claro e conciso, comunicando com precisão a tarefa desejada.
2. **Contextualização Adequada**: Forneça contexto relevante para orientar o modelo na direção certa.
3. **Especificidade**: Seja específico sobre o que você deseja que o modelo faça ou gere.
4. **Exemplos de Entrada e Saída**: Inclua exemplos de entrada e saída para ajudar o modelo a entender melhor a tarefa.
5. **Revisão Iterativa**: Experimente diferentes prompts e revise-os iterativamente com base nos resultados.

## Técnicas de Prompting

### Zero-shot Prompting

Na técnica de Zero-shot prompting, o modelo é solicitado a realizar uma tarefa sem ter sido explicitamente treinado para ela. Isso significa que o modelo deve inferir a resposta com base no prompt fornecido, sem acesso a exemplos de treinamento específicos para essa tarefa. Esta técnica é útil quando não há dados de treinamento disponíveis para uma tarefa específica.

### Few-shot Prompting

Few-shot prompting envolve fornecer ao modelo alguns exemplos de treinamento (geralmente poucos) para uma determinada tarefa, juntamente com o prompt. O modelo utiliza esses exemplos de treinamento para aprender a tarefa e gerar respostas relevantes. Essa técnica é eficaz quando há apenas uma pequena quantidade de dados de treinamento disponíveis.

### Few-shot Chain-of-Thought Prompting

Few-shot Chain-of-Thought prompting é uma extensão da técnica Few-shot prompting, na qual o modelo é solicitado a gerar uma série de respostas coesas e relacionadas a partir de exemplos de treinamento limitados. Isso envolve encadear múltiplas tarefas ou perguntas, e o modelo deve responder de forma consistente e lógica ao longo do "fluxo de pensamento". Essa técnica é útil para tarefas que exigem raciocínio complexo e sequencial.

## Desafios

1. Use a técnica de Few-shot Chain-of-Thought para um problema da sua vida real;✅
![GIF Desafio 01](assets/Desafio1.gif)
[Tabela Desafio 01](assets/Desafio1.csv) utilizada para input de dados no [Google AI Studio](https://aistudio.google.com/).  
[Resposta](assets/Desafio1.docx) gerada pelo Google AI Studio.

2. Escolha 10 textos do seu site de notícias preferido. Apresente para o Google AI Studio o padrão dos títulos e das suas respectivas notícias e quando chegar no décimo primeiro texto, apresente somente a notícia e peça para ele gerar um título. Veja se existe alguma técnica ou padrão; ✅

![GIF Desafio 02](assets/Desafio2.gif)
[Tabela Desafio 02](assets/Desafio2.csv) utilizada para input de dados no [Google AI Studio](https://aistudio.google.com/).  
[Resposta](assets/Desafio2.docx) gerada pelo Google AI Studio.

## Conclusão

Nesta aula, aprendi o conceito de prompt em Inteligência Artificial, foi destacado as melhores práticas para criar prompts eficazes e discutido três técnicas específicas: Zero-shot prompting, Few-shot prompting e Few-shot Chain-of-Thought prompting. Essas técnicas são ferramentas poderosas para orientar modelos de IA na geração de texto e realização de tarefas diversas. Experimente essas técnicas em seus próprios projetos para explorar todo o potencial dos modelos de linguagem modernos.
