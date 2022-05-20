from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    
    # A is knight or knave
    Or(AKnight, AKnave),

    # A is not both knight and knave
    Not(And(AKnight, AKnave)),

    # if A is knight then A is not knave
    Implication(AKnight, Not(AKnave)),

    # if A is knave the A is not knight
    Implication(AKnave, Not(AKnight)),

    # if A is knight then puzzle 0 is true
    Implication(AKnight, And(AKnight, AKnave)),

    # if A is knave then puzzle 0 is false
    Implication(AKnave, Not(And(AKnight, AKnave)))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is knight or knave
    Or(AKnight, AKnave),

    # A is not both knight and knave
    Not(And(AKnight, AKnave)),

    # B is either knave or knight
    Or(BKnave, BKnight),

    # B both cannot be knave or knight
    Not(And(BKnight, BKnave)),

    # if A is knight then A tells truth
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is knave then A tells lie
    Implication(AKnave, Not(And(AKnave, BKnave)))
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is knight or knave
    Or(AKnight, AKnave),

    # A is not both knight and knave
    Not(And(AKnight, AKnave)),

    # B is either knave or knight
    Or(BKnave, BKnight),

    # B both cannot be knave or knight
    Not(And(BKnight, BKnave)),

    # if A is knight then A tells truth
    Implication(AKnight, BKnight),

    # if A is knave then A tells lie
    Implication(BKnight, AKnave),

    # if A is Kanve then B is Knight
    Implication(AKnave, BKnight),

    Implication(BKnave, AKnave)

    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is knight or knave
    Or(AKnight, AKnave),

    # A is not both knight and knave
    Not(And(AKnight, AKnave)),

    # B is either knave or knight
    Or(BKnave, BKnight),

    # B both cannot be knave or knight
    Not(And(BKnight, BKnave)),

    # C is either Knave or Knight
    Or(CKnave, CKnight),

    # C is not both Knave and Knight
    Not(And(CKnight, CKnave)),

    Implication(BKnave, CKnight),
    Implication(CKnight, AKnight),

    Implication(BKnight, CKnave),
    Implication(CKnave, AKnave),    

    Implication(BKnave, AKnight),

    Implication(AKnight, Or(AKnave, AKnight)),
    Implication(AKnave, Not(Or(AKnave, AKnight)))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            # print("in else")
            for symbol in symbols:
                # print(symbol)
                # print(model_check(knowledge, symbol))
                if model_check(knowledge, symbol):
                    # print("model checking")
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
