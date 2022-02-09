# Inicio do teste:


## Coleta

Iniciando pela coleta apos saber como os csvs são estruturados, irei tentar gerar um script simples de coleta utilizando a biblioteca urllib por ser padrão do python no caso.
O projeto tera apenas componentes padrões assim como foi pedido.

Como inicio de integração e depois de alguma busca finalmente encontrei uma forma de baixar os arquivos utilizando apenas as bibliotecas padrão do python.
Depois de muita busca não encontrei uma forma de baixar um arquivo de um servidor sftp no python sem utilizar de uma biblioteca externa, eu decidi optar por utilizar a biblioteca https://www.paramiko.org/ por ser escrita puramente em python e oferecer um client funcional.8