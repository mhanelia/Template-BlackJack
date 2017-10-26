# Template-BlackJack

Black Jack!!

Um jogador contra a banca (o computador).

1. Quem ganha ?

Quem tiver a maior pontuação sem estourar 21 pontos

2. Quanto vale cada carta ?

 -> Ás vale 1 ponto;
 -> Cartas de números valem a mesma quantidade do número;
 -> Cartas de figuras (K, J, Q) valem 10.

3. Regras:

3.1. Tanto o jogador quando a banca recebem 2 cartas, porém a banca exibe somente uma carta, desta forma não é possível saber a soma dos pontos da banca, é uma aposta cega.

3.2. A compra (chamada de Hit), o jogador poderá (compra se quiser) comprar cartas enquanto sua pontuação for menor igual à 16. Quando terminar suas compras, será a vez da banca com a mesma regra.

3.3. Após as compras concluídas, será a hora de virar as cartas (a aposta é chamada de Bet), neste momento as cartas e pontuações da banca e do jogador são exibidas, e computado o vencedor.

4. Métodos obrigatórios:

4.1. Construtor
4.2. create_deck - Cria o baralho (deck)
4.3. shuffle  - Embaralha o deck
4.4. hit - compra de cartas, lembrando que cada carta comprada deve ser excluída do deck
4.5. two_first_cards - Distribui as 2 cartas iniciais para a banca e jogador
4.6. get_points - calcula os pontos de uma mão (conjuto de cartas do jogador ou banca)
4.7. show_hand - Mostra a mão do jogador (somente deste)
4.8. bet - Mostra a mão e pontos da banca, do jogador e computa o vencedor
