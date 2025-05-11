# SD_ATV2
Atividade de Sistemas Distribuidos e Programa Paralela com objetivo de implementar um quiz cliente e servidor utilizando RPC

# Equipe 

- Eric Menezes
  
- Rodrigo Sarno

# RPC (Remote Procedure Call)

- O cliente e servidor foi implementado pela biblioteca xmlrpc que ja vem embutida no Python

# Classe em python necessaria para realizar a conexão cliente com o servidor

`class User:`

    def __init__(self, nome_usuario, quantidade_pts=0, num_perg=0, resp_cliente=None):
    
       self.nome_usuario = nome_usuario
       self.quantidade_pts = quantidade_pts
       self.num_perg = num_perg
       self.resp_cliente = resp_cliente


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

  ## Interoperabilidade

  - Capacidade de um cliente se conectar a servidores desde que utilize um padrão comum de comunicação, flexibilidade e compatibilidade na troca de mensagens
    
  ## Funcionamento geral da aplicação

  - Conectividade cliente-servidor, fluxo do jogo (envio de perguntas, recebimento de respostas, contagem de pontos)
 
  ## Documentação do projeto

  - README claro com instruções de uso, explicação da arquitetura e do protocolo de comunicação, referência ao padrão adotado para interoperabilidade
 
  ## Apresentação em vídeo

  - Demonstração funcional do sistema, explicação dos principais trechos do código, destaque para decisões técnicas relacionadas à interoperabilidade
 

  
 

  
