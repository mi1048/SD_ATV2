# SD_ATV2
Atividade de Sistemas Distribuidos e Programa Paralela com objetivo de implementar um quiz cliente e servidor utilizando RPC

# Equipe 

- Eric Menezes
  
- Rodrigo Sarno

# RPC (Remote Procedure Call)

- O cliente e servidor foi implementado pela biblioteca xmlrpc que ja vem embutida no Python

# Detalhes da Atividade

- O projeto da unidade envolve a criação de uma aplicação distribuída que simula um quiz de perguntas e respostas. Deve-se implementar um servidor usando RPC ou Socket, o qual gerenciará as regras do jogo e permitirá que múltiplas aplicações clientes se conectem para participar.

# Requisitos do projeto incluem:

- O servidor deve implementar as regras para gerenciar a pontuação dos jogadores, baseando-se em seus acertos e erros (resposta correta, 1 ponto).

- As aplicações clientes precisam ser capazes de se conectar ao servidor para iniciar e realizar suas jogadas. A dinâmica do jogo envolve receber perguntas do servidor e submeter respostas.

- Cada servidor oferecerá um serviço de quiz diferente que pode ser separado por domínio, área, complexidade, etc. (Ex: SRV01 = Tecnologia, SRV02 = Filmes, etc.)

- A linguagem de programação e as regras específicas de cada servidor e cliente serão definidas individualmente, por cada equipe, mas os trabalhos devem pensar na interoperabilidade. Assim, uma aplicação cliente de uma equipe deve poder acessar um servidor de outra equipe (naturalmente, dependendo da implementação do ‘outro’ servidor)

- Dica: Isso implica que o modelo de troca de dados deve ser padronizado e compartilhado por todas as equipes.

  # Principais criterios de avaliação

  ## Clareza na implementação

  - Organização do código, legibilidade e boas práticas, Implementações coerentes e funcionais para cliente e servidor, respeitando seus papéis distintos no sistema
    
  ## Manipulação de objetos e serialização de dados

  - Uso adequado de estruturas de dados, serialização/deserialização correta (ex: JSON, XML, etc.), Troca eficiente de informações entre cliente e servidor

  ## Funcionamento geral da aplicação

  - 
 
  ## Documentação do projeto
 
  ## Apresentação em vídeo
  
