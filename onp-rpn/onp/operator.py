from enum import Enum
from functools import total_ordering
from typing import Optional, Tuple, Type


@total_ordering
class Operator:
    def __init__(self, op: str, prio: int) -> None:
        self.op: str = op
        self.prio: int = prio

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Operator):
            return self.op == __o.op or self.prio == __o.prio
        if isinstance(__o, Parenthesis):
            return False
        raise TypeError

    def __lt__(self, __o: object):
        if isinstance(__o, Operator):
            return self.prio < __o.prio
        if isinstance(__o, Parenthesis):
            return False
        raise TypeError

    def __str__(self) -> str:
        return str(self.op)


class OperatorFactory:
    allowed_operators = [
        ("+", 0), ("-", 0), ("*", 1), ("/", 1), ("^", 2)
    ]

    def __new__(cls: Type["OperatorFactory"], operator: str) -> Optional[Operator]:
        result = cls.get_operator(operator)
        if result is None:
            return None
        op, prio = result
        return Operator(op, prio)

    @classmethod
    def get_operator(cls, operator: str) -> Optional[Tuple[str, int]]:
        for op, prio in cls.allowed_operators:
            if op == operator:
                return op, prio
        return None


class Parenthesis(str, Enum):
    OPENING = "("
    CLOSING = ")"


class ParenthesisFactory:
    def __new__(cls: Type["ParenthesisFactory"], value: str) -> Optional[Parenthesis]:
        try:
            return Parenthesis(value)
        except ValueError:
            return None
