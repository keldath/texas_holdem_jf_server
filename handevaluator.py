
from treys import Card
from treys import Evaluator
from itertools import combinations


def best_hand_check(player, comm):
    """
        built on Evaluator and combinations
        this func will rank all the possible combos
        from a given 7 cards
        Evaluator seems not to produce the best
        hand layout , so had to add itertools
    player , community -> given cards
    output: best-> hand and type
    """
    evaluator = Evaluator()

    joined_cards = player + comm
    # joined_cards = ['Kd', '4d', '4c', 'Jd', 'Qs', '8s', '5d']
    all_combos = []
    combo_iter = combinations(joined_cards, 5)

    for co in combo_iter:
        all_combos.append(co)

    def parser(cards):
        parsed = []
        for card in cards:
            parsed.append(Card.new(card))
        return parsed
    # print(player, comm)
    # worst hand according to the treys rank system is 7462
    # see https://github.com/ihendley/treys
    # so placed 9999 as a limit...no reason could use 7462
    # best rank is 1 which is a royal flush
    best_rank = 9999
    best_hand = []
    best_hand_type = ''
    for combo in all_combos:
        combo_cards_of_player = []
        combo_cards_of_comm = []
        for card in combo:
            if card in player:
                combo_cards_of_player.append(card)
            else:
                combo_cards_of_comm.append(card)
        # print(combo_cards_of_player, combo_cards_of_comm)
        comm_p = parser(combo_cards_of_player)
        player_p = parser(combo_cards_of_comm)
        # no need for this.
        # Card.print_pretty_cards(comm_p + player_p)
        rank = evaluator.evaluate(comm_p, player_p)
        rank_class = evaluator.get_rank_class(rank)
        hand_type = evaluator.class_to_string(rank_class)

        if rank < best_rank:
            best_rank = rank
            best_hand = combo_cards_of_player + combo_cards_of_comm
            best_hand_type = hand_type

    print(best_hand)
    print(best_rank)
    print(best_hand_type)
    print([best_hand, best_hand_type])
    return [best_hand, best_hand_type]


