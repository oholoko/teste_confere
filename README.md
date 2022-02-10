# Inicio do teste:


## Coleta

Iniciando pela coleta apos saber como os csvs são estruturados, irei tentar gerar um script simples de coleta utilizando a biblioteca urllib por ser padrão do python no caso.
O projeto tera apenas componentes padrões assim como foi pedido.

Como inicio de integração e depois de alguma busca finalmente encontrei uma forma de baixar os arquivos utilizando apenas as bibliotecas padrão do python.
Depois de muita busca não encontrei uma forma de baixar um arquivo de um servidor sftp no python sem utilizar de uma biblioteca externa, eu decidi optar por utilizar a biblioteca https://www.paramiko.org/ por ser escrita puramente em python e oferecer um client funcional.

### Serializador


Com a coleta completa e criei alguns dicionarios para poder traduzir algumas das variaveis vindas dos csvs. 
Apos a leitura do CSV cada linha é processada individualmente para poder lidar com erros caso uma linha tenha defeito falta apenas um CLI e um Leitor para finalização do projeto
Um banco sera criado contendo os dados serializados e linkados. No CSV so encontrei os tipos:
1,2,9 então não consigo estruturar um banco de dados completo para fazer as coneções de chave primaria e secundaria. Mas ja notei que a estrura que mostra um banco de dados relacional utilizando as multiplas chaves.
Irei modelar ele amanhã e começar os proximos tipos.