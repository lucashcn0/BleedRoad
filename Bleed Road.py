#Definições

define m = Character("Murilo")
define l = Character("Lis")
define b = Character("Bruna")
define c = Character("Caio")
define r = Character("Rafael")
define p = Character("Policial")
define g = Character("Gerente")



label start:

    "Todos acordam de ressaca após uma festa" 
    "levantar da cama ?"
    menu:
        "sim":

            scene quarto

            "Murilo levanta da cama e se arruma para descer, pois estava de pijama" 

            show murilo

            m "Nossa que resaca! Tenho que tomar uma água."

            scene black

            hide murilo

            "Murilo desce"

            show murilo

            m "Bom dia pessoal"

            hide murilo

            "Todos lhe dão bom dia"
            "Murilo vai para cozinha"

            scene cozinha

            show lis

            hide lis

            show murilo

            m "Oi meu amor, bom dia!"

            hide murilo

            show lis

            l "Oi bom dia meu amor!"

            hide lis

            show murilo at left

            show lis at right

            "Murilo se aproxima de Lis e da um beijo"

            hide lis

            show murilo

            m "Eai dormiu bem ?"

            hide murilo

            show lis

            l "dormi sim, e você ?"

            hide lis

            show murilo

            m "bem também"

            "Murilo bebe um copo de água"

            hide murilo

            show lis

            l "Que bom, vai lá pra sala que jaja eu vou também pra gente assistir tv"

            hide lis

            show murilo

            m "Tá bom estou indo lá"

            hide murilo

            scene black

            scene sala

            "na sala todos se acomodam no sofá e depois de ligarem a TV e colocarem no jornal,"
            "veem uma reportagem sobre um carro que atropelou uma garotinha na noite passada."

            "Quando percebem que o carro é o deles Lis tenta acalmar todos. Aos poucos,"
            "o grupo se acalma  até certo ponto , mas o clima continua tenso."

            "Todos estão muito pensativos sobre o que pode ter acontecido e quem poderia ter causado o acidente."
            
            "No meio disso, Caio começa a apontar o dedo para Murilo,"
            "já que o carro era dele, e também para o resto do grupo, o que faz com que todos comecem a se acusar."

            "O que começou como provocações leves logo se transforma em uma briga sobre quem teria mais culpa e quem tem mais chance de ser o 'assassino'."

            "No meio da discussão, Rafael fala:"

            show rafael

            r "A gente não vai chamar a polícia até saber quem estava dirigindo, né?"
            
            hide rafael

            "Chamar a policia ?"

            menu:
                "sim":

                    scene sala

                    show murilo

                    m "Cara acho melhor chamar a policia até porque de qualquer jeito alguem vai ser preso né"

                    hide murilo

                    show lis

                    l "Eu concordo, acho melhor chamar a policia mesmo"

                    hide lis

                    show caio

                    c "Mano eu não concordo acho melhor não chamar, até porque não sabemos como aconteceu"

                    hide caio

                    show rafael

                    r "É cara eu também acho melhor não chamar"

                    hide rafael

                    show bruna

                    b "É melhor sabermos melhor oque aconteceu"

                    hide bruna

                    show lis

                    l "É pensando bem, melhor não chamar mesmo, mas e se der errado?"

                    hide lis

                    show murilo

                    m "Tá bom, então não vamos chamar a ppolícia. mas como vamos saber quem atropelou?"

                    hide murilo
                    jump cp


                "não":
                    
                    scene sala 

                    show murilo

                    m "eu acho melhor não, só até a gente saber oque realmente aconteceu."

                    hide murilo

                    show lis

                    l "É eu concordo, melhor não chamar mesmo, mas e se der errado ?"

                    hide lis

                    show caio

                    c "É melhor não chamar mesmo"

                    hide caio

                    show rafael

                    r "É cara acho melhor não chamar mesmo não"

                    hide rafael

                    show bruna

                    b "É melhor sabermos oque aconteceu"

                    hide bruna
                    jump cp

        "não":

            jump nãolevantou

            label nãolevantou:

            "Murilo volta a dormir como se nada tivesse acontecido..."
            jump fim
  












label cp:

    scene sala

    "Um silêncio pertubador toma conta da sala, até ser quebrado por bruna:"

    show bruna

    b "Vamos tentar lembrar da noite passada. Somos cinco pessoas, acho que conseguimos montar alguma coisa, né?"

    hide bruna

    "Ir para outro comodo?"

    menu:
        "não":
            
            "Todos se sentam no chão. Ninguém tem ideia de como começar o interrogatório, até que Bruna fala:"

            show bruna

            b "Vamos tentar lembrar qualquer coisa que aconteceu ontem, porque aí as memórias voltam, né? Vai, Lis, começa."

            hide bruna

            show lis

            l "De ontem, eu só lembro que fiquei o tempo todo com o Murilo, bebendo umas e outras... Tinha mais alguém com a gente, mas não lembro quem."

            hide lis

            "Então todos olham para Murilo"

            show murilo

            m "É, do jeito que a Lis falou, eu lembro que estava com ela no bar... Mas não lembro de mais ninguém com a gente. Só lembro de nós dois."

            hide murilo

            show caio

            c "Ei, Bruna, você falou das pessoas, mas por que não fala de si mesma? Tá escondendo alguma coisa?"

            hide caio

            show bruna

            b "Quem deve estar escondendo algo é você, né, com essa cara de falso. Eu deveria chamar a polícia pra você logo!"

            hide bruna

            show lis

            l "PESSOAL, PAREM! Não era pra gente estar resolvendo isso agora?"    

            hide lis

            show caio at left

            show bruna at right

            c "Desculpa..."

            b "desculpa..."

            hide caio

            b "Tá bom, eu falo o que lembro pra acabar logo com isso. Só lembro que estava bebendo com um boyzinho que achei um fofo, e eu tava vendo de ficar com ele. Fora isso, não lembro de mais nada. E você, Caio?"

            hide bruna

            show caio

            c "Só lembro de quando a gente foi embora. Fora isso, mais nada. E você, Rafael?"

            hide caio

            show rafael

            r "Não lembro de nada… Acho que era eu que estava junto com a Lis e o Murilo."

            hide rafael

            "Com as cartas na mesa, o grupo fica ainda mais confuso. Mas então todos ouvem batidas na porta e logo Murilo foi ver quem era…"

            "Murilo abre a porta e se depara com um policial"

            show murilo

            m "Bom dia, posso ajudar ?"

            hide murilo

            show policial

            p "pode sim, seu vizinho me ligou ele falou que vocês estavam gritando muito sobre quem fez oque e ele falou que vocês mataram uma pessoa, é verdade isso?"

            hide policial

            menu:
                "não":

                    show murilo

                    m "A denovo isso? Ele sempre tenta fazer com que a gente seja preso porque a gente faz muita festa aqui sabe seu policia aí é sempre isso"

                    hide murilo

                    show policial

                    p "Certo certo, mas eu tenho que conferir isso sabe porque tem muita gente mentirosa, você me entende né?"

                    hide policial

                    show murilo

                    m "Isso é mesmo necessario seu policia? Eu estou falando a verdade."

                    hide murilo 

                    show policial

                    p "Então pense que isso é só rotina, até porque não tem nada a esconder certo?"

                    hide policial

                    scene black

                    "Todos são encaminhados para a delegacia junto ao  policial"

                    scene delegacia

                    show bruna

                    b "Nossa não acredito que isso tá acontecendo comigo em caramba "

                    hide bruna

                    show caio

                    c "Verdade, só porque eu falei pra não chamar a policia em"

                    hide caio

                    show rafael

                    r "Verdade mais aqui está meio vazio não está não?"

                    hide rafael

                    show policial

                    p "É porque estão em horário de almoço agora, mas vamos ao que interessa, eu vou levar comigo a Bruna prmeiro então vocês fiquem aqui sentados que eu já volto"

                    hide policial

                    "e assim aconteceu um por um até chegar na vez do Murilo"

                    show policial at right

                    p "agora só falta você Murilo, me acompanhe"

                    show murilo at left

                    m "Certo vamos logo com isso"

                    #scene sala de interrogatorio

                    p "Vou te fazer algumas perguntas para você tá bom?"

                    m "Tudo bem pode falar"

                    p "Oque exatamente tava acontecendo pro seu vizinho me chamar na sua casa?"

                    hide policial

                    hide murilo

                    menu:
                        "Eu e meus amigos estavamos vendo quem ia pagar a conta da semana":

                            show policial at right

                            show murilo at left

                            p "qual conta? porque as contas de água, luz e etc era semana passada já"

                            m "Era a conta do bar que ontem a gente saiu e bebeu demais e esquecemos de pagar"

                            hide policial

                            hide murilo
                            jump cd

                        " Eu e meus amigos estavamos jogando e nos empolgamos quando a gente ganhou e começamos a falar mais alto do que deveria":

                            show policial at right

                            show murilo at left

                            p "Que legal, qual jogo?"

                            m "Street fighter, conhece?"

                            p "Conheço sim, já joguei bastante com meus amigos antigamente"

                            hide policial

                            hide murilo
                            jump cd

                "sim":

                    show murilo

                    m "Então, a gente pensa que sim, porém nos não lembramos de nada e não sabemos se realmente matamos alguém entende?"

                    p "Então vou ter que levar todos vocês para interrogatório e vou prender quem matou."

                    "Todos são encaminhados para a delegacia junto ao  policial"

                    scene delegacia

                    show bruna

                    b "Nossa não acredito que isso tá acontecendo comigo em caramba "

                    hide bruna

                    show caio

                    c "Verdade, só porque eu falei pra não chamar a policia em"

                    hide caio

                    show rafael

                    r "Verdade mais aqui está meio vazio não está não?"

                    hide rafael

                    show policial

                    p "Todos quietos! Até segunda ordem todos são culpados, agora vem um de vocês comigo agora e sem falatório, estamos entendidos?"

                    hide policial

                    show bruna

                    b "Tá bom deixa que eu vou primeiro então"

                    hide bruna

                    show rafael

                    r "Se quiser eu vou primeiro, não deve ser tão ruim"

                    hide rafael

                    show bruna

                    b "Não, deixa que eu vou"

                    hide bruna

                    " E assim Bruna vai, logo depois Rafael, Caio, Lis e por fim..."

                    show policial at right

                    show murilo at left

                    p "Agora o último vem comigo"

                    m "Tô indo"

                    #scene sala de interrogatorio

                    p "Olha vou te fazer as perguntas só uma vez e você me responde, entendeu?"

                    m "Tá bom"

                    p "Vocês não sabem quem matou, mas porque vocês tem alguma duvida sobre isso? Até porque é difícil matar sem saber."

                    hide policial

                    hide murilo

                    menu:
                        " Porque ontem a noite fomos para uma festa e voltamos loucões, só que a gente atropelou alguém lá e só percebemos hoje de manhã e não sabemos quem estava dirigindo":

                            show policial at right

                            show murilo at left 

                            p "Eu deveria prender vocês por fazerem essas coisas e principalmente por ter matado alguém!! Mais infelizmente ainda não posso porque a lei não permite, só que um passo errado e eu prendo todos vocês!"

                            hide policial

                            hide murilo
                            jump cd4

                        "estávamos jogando pedras de um barranco, e acertamos alguém, porém só vimos depois e não sabemos quem jogou a pedra que matou a pessoa":

                            show policial at right

                            show murilo at left

                            p "Vocês são muito burros, quem joga uma pedra desse calibre em um barranco que não tem certeza se tem gente passando? Eu quando jovem fazia coisas assim mais nunca sem cuidado que nem vocês."

                            hide policial

                            hide murilo
                            jump cd4

        "sim":
            
            scene sala

            show murilo

            m "Certo. Vamos pro porão, pra nenhum vizinho escutar. Isso ainda é segredo. (Todos seguem juntos para o porão)."

            scene porao

            "Todos se sentam no chão. Ninguém tem ideia de como começar o interrogatório, até que Bruna fala:"

            show bruna

            b "Vamos tentar lembrar qualquer coisa que aconteceu ontem, porque aí as memórias voltam, né? Vai, Lis, começa."

            hide bruna

            show lis

            l "De ontem, eu só lembro que fiquei o tempo todo com o Murilo, bebendo umas e outras... Tinha mais alguém com a gente, mas não lembro quem."

            hide lis

            "Então todos olham para Murilo"

            show murilo

            m "É, do jeito que a Lis falou, eu lembro que estava com ela no bar... Mas não lembro de mais ninguém com a gente. Só lembro de nós dois."

            hide murilo

            show caio

            c "Ei, Bruna, você falou das pessoas, mas por que não fala de si mesma? Tá escondendo alguma coisa?"

            hide caio

            show bruna

            b "Quem deve estar escondendo algo é você, né, com essa cara de falso. Eu deveria chamar a polícia pra você logo!"

            hide bruna

            show lis

            l "PESSOAL, PAREM! Não era pra gente estar resolvendo isso agora?"    

            hide lis

            show caio at left

            show bruna at right

            c "Desculpa..."

            b "desculpa..."

            hide caio

            b "Tá bom, eu falo o que lembro pra acabar logo com isso. Só lembro que estava bebendo com um boyzinho que achei um fofo, e eu tava vendo de ficar com ele. Fora isso, não lembro de mais nada. E você, Caio?"

            hide bruna

            show caio

            c "Só lembro de quando a gente foi embora. Fora isso, mais nada. E você, Rafael?"

            hide caio

            show rafael

            r "Não lembro de nada… Acho que era eu que estava junto com a Lis e o Murilo."

            hide rafael

            menu:
                "Gente perai lembrei de uma coisa, acho que a gente tinha ido lá no posto de gasolina encher o tanque":

                    scene garagem

                    "Todos entram no carro. Lis e Murilo vão na frente, o resto atrás. Rafael comenta:"

                    show caio at left 

                    c "Olha só quem tá dirigindo, né..."

                    show lis at right

                    l "É, Caio… Mas o Murilo emprestou o carro pra todo mundo antes, né?"

                    hide caio

                    hide lis

                    "O carro segue em silêncio, apenas o som da estrada e do rádio ao fundo."

                    scene posto 

                    "Chegando ao posto, Murilo pede para falarem com o gerente. Caio vai conversar com ele."

                    show caio at left

                    c "Então, eu e meus amigos estávamos vendo quem pagou a gasolina ontem pra decidir quem paga da próxima, sabe? Você poderia mostrar as gravações de ontem à noite, por favor?"

                    "O gerente, um senhor gentil, sorri:"

                    show gerente at right

                    g "Claro, por que não? Sei como é, vocês jovens vivendo a vida."

                    b "(cochichando):É... vivendo até demais pro meu gosto."

                    hide caio

                    hide gerente

                    "O gerente mostra a gravação. Os jovens veem Murilo trocando de lugar com alguém que estava no banco de trás, mas o rosto da pessoa não aparece claramente, todos agradecem ao gerente e voltam para casa."

                    scene sala

                    show murilo at right

                    m "Pelo menos sabemos que não fui eu, né…"

                    "A sala fica em silêncio. Todos pensam: quem Murilo pediu para dirigir no lugar dele? Não poderia ser a Lis — ela sempre anda no banco do passageiro. Estão todos confusos… Até que alguém solta:"

                    show rafael at left

                    r "Não fui eu. Eu estava sentado no meio."

                    m "Como assim? Você estava sentado no meio, Rafael?"

                    r "É ué. Eu estava no meio, qual o problema?"

                    hide murilo

                    show bruna at right

                    b "O que quer dizer que você lembra de mais coisas do que falou, né? Quem nos garante que não foi você que atropelou?"

                    "todos olham desconfiados para o Rafael. Até que..."

                    hide bruna

                    hide rafael

                    show murilo

                    m "espera… Então tá tudo resolvido. Se não foi o Rafael, e ele estava sentado no meio, ele pode nos dizer quem estava dirigindo, certo?"

                    hide murilo

                    show rafael at left

                    r "(suando):“E-eu não sei. Não consegui ver…"

                    show lis at right

                    l "Como assim você não pode falar?"

                    r "Só não posso. Me deixem em paz."

                    hide lis

                    show murilo at right

                    m "Se não falar, vamos chamar a polícia."

                    r "Pois chame"

                    "Rafael é preso e condenado a 3 anos de cadeia."
                    jump pr 

                "É nossa situação não é boa, nós não lembramos de nada de realmente útil":

                    scene porao

                    show bruna

                    b " É vc jura? Nós matamos alguém e nem sabemos quem que foi!"

                    hide bruna
                    jump ds

                    menu:
                        "Eu sei mais temos que nos acalmar e tentar resolver isso porque aí pelo menos só um de nós vai preso":

                            scene porao

                            show bruna

                            b "É todos nós sabemos disso mais isso não muda nada! a nossa situação é a mesma!"

                            hide bruna
                            jump ds
                             
                        "É eu tô começando a achar que é melhor chamar a policia":

                            scene porao

                            show rafael at left

                            r "Não, melhor não murillo até porque nós já concordamos que isso é uma má ideia"

                            show murilo at right

                            m " É nós concordamos mas..."

                            r "ntão pronto, não vamos chamar"

                            hide murilo

                            hide rafael
                            jump ds


label ds:

    scene porao

    show murilo at right

    m "Olha, tudo isso não está levando a lugar nenhum, eu vou chamar a polícia!"

    show caio at left

    c "Murilo você não pode fazer isso, a gente já combinou com o grupo de não chamar."

    m "ntão me fala uma ideia melhor do que isso, porque já estamos nessa a horas e nada mudou!"

    c "..."

    hide murilo

    hide caio

    show lis

    l "É eu concordo, não está levando a lugar nenhum essa conversa, então acho melhor liugar para a policia"

    hide lis

    "Rafael vendo uma certa pessoa ficando dessesperado prontamente fala..."

    show rafael at right

    r "Chega! Olha tá bom fui eu, eu adimito então vamos parar com isso e eu vou lá me entregar"

    show caio at left

    c "Isso é serio ?"

    r " S-sim, fui eu, eu me lembro do que aconteceu ontem a noite e eu tentei varrer isso para baixo do tapete, mais fui eu sim"

    c "Olha está bem, se você está dizendo, eu te acompanho até a delegacia, e depois que você sair da prisão a gente continuará sendo amigos"

    hide caio

    show murilo at left

    m "Olha se você tá confessando não tem o porque eu discordar, e como o Caio disse nó iremos continuar sendo amigos, então se cuida lá em e de vez em quando vamos te visitar"

    hide rafael

    hide murilo

    "E assim Rafael foi preso e tudo acabou... ou era oque todos pensavam"
    jump pr


label pr:

    scene casa

    "Após a prisão, todos estão cabisbaixos. Rafael era um dos melhores amigos do grupo."

    "O Murilo encontra Bruna chorando e murmurando:"

    menu:
        "Ir lá ver porque a Bruna está chorando":

            show bruna at left

            b "(chorando): Por quê? Era pra ter sido eu… Você não poderia ter ido pra lá. Não podia…"

            show murilo at right

            m "Bruna, do que você está falando?"

            b "(exausta): Se eu te contar, você não conta pra ninguém, né?"

            m "Não conto."

            b "uem atropelou a garota fui eu. E o Rafa quis me proteger. Eu queria ter falado antes… Mas não tive coragem. Me perdoa, por favor."

            m "Não é pra mim que você tem que se desculpar. É pro Rafael."

            hide murilo

            hide bruna

            "Murilo se afasta, deixando Bruna chorando ainda mais. Porém Agora, o Murilo está diante de um difícil impasse"

            menu:
                "contar a verdade para que a justiça seja feita":

                    "Murilo conta a verdade para a autoridade fazendo com que ele quebre sua promessa e faça com que a Bruna seja presa"
                    jump fi


                "manter o silêncio, respeitando a decisão de Rafael":

                    "Então o Murilo deixa como o Rafael quis, e também por conta que ele falou para Bruna que não iria falar nada"
                    jump fr
            
        "Ignorar isso e só seguir seu caminho em paz":

            "Murilo passa reto e não da nem bola pra AMIGA DELE CHORANDO e fica por isso mesmo, seu MONSTRO"
            jump fc
                




                

                    
                    
















label cd4:

    #scene de sala de interrogatorio

    show policial at right

    show murilo at left

    p "Mas vamos continuar o interrogatório, segunda pergunta agora, que horas vocês voltaram para a casa?"

    menu:
        "Eu não sei direito, acho que voltamos umas 1hr da manhã":

            show policial at right

            show murilo at left

            p "É sempre nesses horarios que as coisas acontecem."

            hide policial

            hide murila
            jump cd5

        "Voltamos por volta das 4hrs da manhã se não me engano":

            show policial at right

            show murilo at left

            p "Vocês ficaram curtindo demais pra quem matou alguém em, da até raiva"

            hide policial

            hide Murilo
            jump cd5


label cd5:

    #scene sala de  interrogatorio

    show policial at right

    show murilo at left

    p "vamos para a última pergunta, está bem? quando vocês estavam voltando para a casa, vocês passaram em algum lugar?"

    hide policial

    hide murilo

    menu:
        "Não, a gente estava só voltando pra casa mesmo e não quisemos passar em nenhum lugar porque eu estava querendo usar o banheiro, aí apressei todo mundo.":

            #scene sala de  interrogatorio

            show policial at right

            show murilo at left

            p "Hum tá bom então, Vou te levar pra perto dos seus amigos, e espere o pior"

            hide policial

            hide murilo
            jump cd6
        
        "A gente passou em um posto de gasolina se não me engano porque a gasolina estava quase acabando, aí ja estava no caminho e passamos por lá":

            #scene sala de  interrogatorio

            show policial at right

            show murilo at left

            p "É então acho que está certo, Vou te levar pra perto dos seus amigos, e espere o pior"

            hide policial

            hide murilo
            jump cd6
    
label cd6:

    scene delegacia

    show policial at right

    show murilo at left

    "O Murilo é levado pra carceraria junto dos demais para esperar o julgamento"

    hide policial

    m "E então como foi o interrogatório de vocês?"

    show lis at right

    l "Eu fiquei co-om tanto me-medo (diz lis quase chorando)"

    hide lis

    m "passou já, fica tranquila que vai tudo dar certo"

    show bruna 

    b "O meu foi bem tranquilo, ele só me fez umas perguntas e eu respondi com sinceridade"

    hide bruna

    hide murilo

    show rafael

    r "Eu não consegui responder todas porque eu não me lemrbo de muita coisa não"

    hide rafael

    show murilo

    m " agora é só esperar o julgamento pra gente saber oque tem por vir"
    jump fj



        
















                    

label cd:

    show policial at right

    show murilo at left

    p "Beleza agora a segunda pergunta, você viu o jornal de hoje?"

    m "Eu vi sim"

    p "Então você sabe que houve um assasinato de uma criança, não é?"

    m "Sim, mais oque que tem? Nem eu e nem os meus amigos sabemos nada sobre isso."

    p "Eu não disse que vocês tem, só tô falando que ela era da sua região e também tem um bar lá perto de onde ocorreu o acidente"

    m "Tudo bem mais oque que tem? eu fui no bar sim, mais eu não atropelei ninguém"

    p "Não é você que tem que dizer isso, é a justiça, mas vamos para a proxima pergunta, que horas você voltou para sua casa ontem a noite?"

    hide policial

    hide murilo

    menu:
        "Eu não sei direito, acho que voltamos umas 1hr da manhã":

            scene delegacia

            show policial at right

            show murilo at left

            p "Entendo, porque a autopsia da criança mostra o horario que ela morreu, e foi bem proximo do seu horário... mas ok"

            m "lá vem você denovo com isso, já falei que não fomos nós, fala logo as perguntas para eu poder ir em bora."

            hide policial

            hide murilo
            jump cd2


        "Voltamos por volta das 4hrs da manhã se não me engano":

            scene delegacia

            show policial at right

            show murilo at left 

            p "Noite cheia em, aposto que você meteu o pé n jaca, mas isso é bem tarde né, sua namorada gosta que você fique até tão tarde nos bares?"

            m "Ela tava junto seu policia, então tá tudo bem"

            p "Não foi bem isso que ela disse... mas ok" 

            m "Que? Como assim?"  

            p "Vamos continuar o interrogatorio"

            hide policial

            hide murilo
            jump cd2




label cd2:

    scene delegacia

    show policial at right

    show murilo at left

    p "Vamos para a última pergunta, está bem? quando vocês estavam voltando para a casa, vocês passaram em algum lugar?"

    hide policial

    hide murilo

    menu:
        "Não, a gente estava só voltando pra casa mesmo e não quisemos passar em nenhum lugar porque eu estava querendo usar o banheiro, aí apressei todo mundo.":

            scene delegacia

            show policial at right

            show murilo at left

            p "Bom... já te perguntei tudo oque eu queria, mas as respostas não batem, sabe oque isso significa né?"

            m "Como assim? Eu tenho certeza do que eu estou falando então eu não estou mentindo"

            p "Eu não estou falando que está mentindo e nem que não está, mas eu vou conferir isso com todos vocês."

            hide policial

            hide murilo
            jump cd3

        "A gente passou em um posto de gasolina se não me engano porque a gasolina estava quase acabando, aí ja estava no caminho e passamos por lá":

            scene delegacia

            show policial at right

            show murilo at left

            p "Hum entendo, você sabe qual é o nome desse posto?"

            m "Era um petrobras se não me engano mais realmente não lembro direito, ele provavelmente está perto do bar."

            hide policial

            hide murilo
            jump cd3


label cd3:

    scene delegacia

    show policial at right

    show murilo at left

    p "Ótimo isso é tudo que eu queria saber, agora vou te levar onde os outros estão ok?"

    m "Tudo bem"
    jump fj









label fc:
    "FINAL CORAÇÃO DE GELO"

label fj:
    "FINAL JULGAMENTO"

label fi:
    "FINAL INCONFIAVEL"

label fr:
    "FINAL REPEITOSO"

label fim:

return
