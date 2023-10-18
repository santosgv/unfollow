# unfollow
Bot para o instagram onde e listado os seguidores e as pessoas no qual voce segue e compara ambas e cria um arquivo .txt de usuarios que nao segue voce.


## Tecnologias utilizadas
- `PyAutoGUI`
- `Selenium`
- `Python3`

## Configuração do ambiente
~~~linux

git clone https://github.com/santosgv/unfollow.git

~~~

## Instale as bibliotecas necessarias
~~~linux

pip install -r requirements.txt
~~~

## Crie o arquivo .env e adicione as variaveis 

~~~linux
usuario='seu_usuario'
senha='Sua_senha'
loop=1000
~~~

## O bot ira consultar este arquivo para conseguir logar na Conta do Instagram a variavel loop e a quantidade de scrolldown o mesmo ira realizar para conseguir obter todos os usuarios. 

## (NOTA) CASO TENHA MAIS DE 1K DE SEGUIDORES E POSSIVEL QUE SEJA NECESSARIO AUMENTAR O NUMERO DE LOOPS E POR CONTA DESSE LOOP O TEMPO DE EXECUÇAO DO BOOT DEVE DEMORAR MAIS PARA FINALIZAR TODAS AS FUNÇOES PROPOSTAS

## (AVISO) NAO ABUSE DESSE SCRIPT POIS E POSSIVEL TOMAR BAN E BLOCK PELO INSTAGRAM, OTIMIZEI O MAXIMO PARA PARECER COMO UMA PESSOA UTILIZANDO O INSTAGRAM PELO NAVEGADOR, A QUANTIDADE MAXIMA DE SEGUIR E DEIXAR DE SEGUIR E DE 205 USUARIOS POR EXECUÇAO DO BOT, VOCE PODE AUMENTAR A QUANTIDADE MAS COM ISSO PODE OCASIONAR OS PROBLEMAS JA CITADOS ACIMA E CAUSANDO A MA UTILIZADE DA FERRAMENTA

## Para alterar a quantidade basta mudar a quantidade nessa variavel no codigo

~~~python
for linha in tamanho[:205]: # altere o numero para a quantidade desejada
~~~
## O bot tem as seguintes funcionalidades

        1)  APENAS LISTAR OS USUARIO QUE TE SEGUE ?

            Gera um arquivo sequidores.txt contento todos os usuarios que segue Voce

        2)  APENAS LISTAR OS USUARIOS QUE VOCE SEGUE ?

            Gera um arquivo seguindo.txt contendo todos os usuarios que Voce Segue

        3)  VERIFICAR OS USUARIOS QUE NAO TE SEGUE DE VOLTA ?

            Compara os arquivos de sequidores.txt e seguindo.txt e gera um novo arquivo chamado nao_segue_de_volta.txt

        4)  DEIXAR DE SEGUIR USUARIOS ?

            Deixa de seguir todos os usuarios listados no arquivo nao_segue_de_volta.txt

        5)  SEGUIR USUARIOS ?

            Segue todos os usuarios listados no arquivo nao_segue_de_volta.txt ()

        0)  Sair do boot?

            Sai do Bot

### Print da quantidade de Seguindo antes do Bot
![WhatsApp Image 2023-10-18 at 15 54 24](https://github.com/santosgv/unfollow/assets/54445515/d2b0989b-7e18-4e11-907d-8b36ddf19593)

### Print apos a utilizaçao do Deixar de Seguir

![WhatsApp Image 2023-10-18 at 15 54 31](https://github.com/santosgv/unfollow/assets/54445515/335e07fd-6c07-40fc-b1ef-8687580c3e50)

## APROVEITANDO NAO DEIXE DE ME SEGUIR <a href="https://www.instagram.com/vitim_gone/">instagram</a> 😎

