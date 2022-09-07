
from treys import Card
from treys import Evaluator


def best_hand_check(player, comm):
    """

    """
    evaluator = Evaluator()
    print(player)
    print(comm)
    Card.print_pretty_cards(comm + player)
    # rank = evaluator.evaluate(comm, player)
    # print(evaluator.evaluate(comm, player))
    # rank_class = evaluator.get_rank_class(rank)
    # print(evaluator.class_to_string(rank_class))


