# Tutorial de Engenharia de Prompt - respostas Master ChatGPT e LLM

Link: https://www.youtube.com/watch?v=_ZvnD73m40o  
freecodecamp.org e MIT

✏️ Curso desenvolvido por @AniaKubow em parceria com MIT

⭐️ Conteúdo ⭐️ \
⌨️ (00:00) Introdução\
⌨️ (01:31) O que é Prompt Engineering?\
⌨️ (02:17) Introdução à IA\
⌨️ (03:52) Por que a Engenharia de Prompt é útil\
⌨️ (06:36) Lingüística\
⌨️ (08:04) Modelos de Linguagem\
⌨️ (14:35) Mentalidade de Engenharia de Prompt\
⌨️ (15:38) Usando GPT-4\
⌨️ (20:41) Melhores práticas\
⌨️ (31:20) Zero-Shot e Few-Shot Prompts\
⌨️ (35:06) Alucinações de IA\
⌨️ (36:43) Vetores/incorporação de texto\
⌨️ (40:28) Recapitulação\

---
#### O que é Prompt Engineering?  
A Engenharia de Prompt (O que é Prompt Engineering) é uma carreira surgiu com a ascenção da Inteligência Artificial. Envolve ***Escrita Humana***, refinando e otimizando prompts de comandos estruturados.  
Isso é feito com a intenção de otimizar ao máximo a interação entre Humanos e Intelência Artificial (Homem x Máquina)
Manter uma Biblioteca de Prompt atualizada é dos requisitos impostos ao Engenheiro de Prompt, bem  como relatar as descobertas e, em geral, ser um Líder Inovador nesse espaço.

---

#### Introdução à IA  
A Inteligência Artificial é a **Simulação** de processos humanos por máquinas.  
Pelo menos até agora, ela não pode pensar por si mesma tanto quanto pareça. Quando utilizamos uam IA, estamos na verdade utilizando modelos estatísticos de "Aprendizado de máquina" (Machine Learning). Os modelos são alimentados com grandes bases para aprendizado e otimizado para sugerir respostas baseados em algorítimos de recomendações.

Graças a esses Grandes Modelos de Linguagem (LLM - Large Language Model), agora é possível gerar:
* Respostas de Textos
* Imagens
* Músicas
* Vídeos
* e outros...

---

#### Por que a Engenharia de Prompt é útil?  
Com o crescimento exponencial da IA, até mesmo os seus arquitetos "lutam" para controlar as respostas geradas pelos grandes modelos de linguagem, então desenvolver um método de escrita lógico e estruturado gerará respostas mais próximas da qual precisamos.

Exemplos:  
Digamos que há um uma pessoa que está aprendendo Inglês e está em dúvida sobre um texto escrito. Ele poderia digitar o seguinte prompt:

**Usuário:**
```
"Olá, por favor, corrija esse parágrafo: Hi, I looking for a laptop for game that is powerful and affordable. You Can help me find one?"
```  
**Resposta:**
```Claro, aqui está o parágrafo corrigido:
"Hi, I'm looking for a powerful and affordable laptop for gaming. Can you help me find one?"
```

Note que a resposta é bem direta e não ajuda muito, não  aponta os erros de forma clara.
E, se ao invés de obter uma reposta direta para uma pergunta específica, essa pessoa pudesse obter, além da resposta, algum tipo de interação, como com um professor de idiomas? Isso seria muito mais proveitoso do que somente receber uma correção.

Com as intruções corretas podemos criar isso com IA!

**Exemplo:**
```
Quero que você atue como professor de Inglês falado. Falarei com você em inglê e você responderá em inglês para eu praticar meu Inglês falado. Quero que você mantenha minha resposta organizada, limitando a 100 palavras. Também quero que você corrija estritamento meu erros gramaticais e de digitação, e quero que você me faça uma pergunta em sua resposta. Agora vamos praticar, você poderia me fazer uma pergunta primeiro? Lembre-se, quero que você corrija estritamente meus erros gramaticais, de digitação e erros factuais.
```

**Resposta:**
```
Of course! Let's get started. Here's your question: What do you enjoy most about learning English?
```

Note que a resposta aqui é uma interação "Homem x Máquina", onde ela está gerando algumas perguntas e você estará aprendendo ao longo do caminho.

É uma experiência completamente diferente, graças a Prompt que escrevemos.

⌨️ Experimente mais um exemplo:

Treinamento em Linguagem SQL  
**Prompt:**
```
Estou buscando a sua orientação como professor de Linguagem SQL para avaliar e aprimorar meu conhecimento em SQL. Para começar, gostaria que você elaborasse um teste de múltipla escolha para determinar meu nível atual de habilidade. Após responder às perguntas, ficaria grato se você pudesse me fazer perguntas adicionais sobre Linguagem SQL, permitindo-me praticar e fortalecer meu entendimento a cada interação.

Por favor, aguarde minha resposta para cada pergunta antes de prosseguir para a próxima, seguindo o exemplo de dar feedback sobre a correção das minhas respostas. Por exemplo, se eu responder corretamente a uma pergunta, você pode me parabenizar e continuar com a próxima pergunta. Se eu responder incorretamente, você pode me corrigir e fornecer uma explicação para me ajudar a entender melhor.
```

Vamos nos aprofundar nisso mais adiante.

---
#### Lingüística
Começando pelo básico.  
Linguística é o estudo da linguagem, ele se concentra em tudo, desde como a palavra é escrita até como os sons da fala é interpretado.
* Fonética: 
    * Estudo de como os sons são percebidos.
* Fonologia:
    * Estudo dos padrões e mudanças sonoras
* Morfologia:
    * Estudo da estrutura da palavras
* Sintaxe:
    * Estudo da estrutura da frases
* Semântica:
    * Estudo do SIGNIFICADO linguístico
* Pragmática:
    * O estudo de como a linguagem é usada no contexto
* Linguística da História
    * Estudo da Mudança Linguística
* Sociolinguistica:
    * Estudo da relação "Liguagem x Sociedade"
* Linguistica Computacional:
    * Estudo de como os Computadores processam a liguagem humana
* Fisiolinguistica:
    * Estudo de como os humanos adquirem e utilizam a linguagem.

>Portanto, a Linguística é a chave para a engenharia de prompt! *Compreender as nuances da linguagem e como ela é utilizada em diferentes contextos é crucial para elaboração de instruções eficazes.*  
E não é só isso, utilizar uma estrutura de linguagem universalmente utilizado fará com que a IA traga respostas muito mais precisas.

---
#### Modelos de Linguagem
Um modelo de linguagem é um "Programa de Computador Inteligente" que aprende com uma vasta coleção de textos escritos. Reúne livros, artigos, sites e todo tipo de rescuros escritos que permitem obter conhecimento de como os humanos utilizam a linguagem.

>Eles funcionam analisando uma sentença de texto, analisa sua estrutura semântica e tenta sugerir a continuação do texto baseada no contexto LINGUÍSTICO da sentença.

Eles podem ser encontrados em:
* Serviços de atendimento ao cliente
* Chat bots
* Escrita criativa
* Etc

Eles podem nos ajudar a:
* Encontrar informações
* Obter sugestões
* Criar conteúdo

>Mas lembre-se, ainda que os modelos de linguagem sejam aburdamete eficientes, eles ainda precisam de seres humanos para criá-los e treiná-los. Eles são, na verdade, o resultado da engenhosidade dos seres humanos e o poder do algorítimos computacionais.

Cusiodidades dos modelos de Linguagens:
* ELIZA - Entre 1964 e 1968 - MIT: 
    * Foi criado para simular um pscólogo, afim de ajudar uma pessoa investigar seus pensamentos e sentimentos. O Modelo era capaz e identificar padrões de escrita e incentivar as pessoas que a questionarem seus sentimentos. Algumas pessoas chegaram a se sentir "atraídas" pela IA devido a impressão de "atenção" que a máquina dava aos usuários. 
* SHRDLU - Entre 1968 e 1969
    * Era capaz de entender comandos e recriar formas tridimensionais na tela. 

* GPT - 2010
    * Modelo 'Generativo pré-treinado'. Início do Deep Learning.

* GPT 1 - 2018
    * Surge o primeiro modelo de interação rápida criado pela empresa OpenAI. Ele foi treinando com um grande volume de livros, artigos e conteúdo da internet. Um modelo absurdamente treinado, porém modesto se comparado com seus decendentes que utilizamos hoje.

* GPT 2 - 2019

* GPT 3 - 2020
    * Equipado com mais de 300 bilhões de parâmetros.

* GPT 4 - 2023
    * Treinado com praticamente todos conteúdo acessível da Internet.

* 2024+: Dezenas de modelos estão sendo treinados, levando essa área a uma espécie de "Corrida técnológica".

> Parece que estamos apenas no começo quando se trata de modelos de linguagem e IA. Então aprender como aproveitar esse dados Engenharia de Prompt parece ser uma jogada inteligente para qualquer pessoa hoje.

---
#### (14:35)Mentalidade de Engenharia de Prompt

---
#### ⌨️ (15:38) Usando GPT-4\
#### ⌨️ (20:41) Melhores práticas\
#### ⌨️ (31:20) Zero-Shot e Few-Shot Prompts\
#### ⌨️ (35:06) Alucinações de IA\
#### ⌨️ (36:43) Vetores/incorporação de texto\
#### ⌨️ (40:28) Recapitulação\