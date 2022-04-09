from .operator import Operator, OperatorFactory, Parenthesis, ParenthesisFactory
from .queue import FifoQueue
from .stack import Stack


class ONP(FifoQueue):
    def __str__(self) -> str:
        return " ".join([str(_) for _ in self._queue])


def translate_to_onp(input_equation: str):
    data = input_equation.strip().replace(" ", "")
    onp = ONP()
    operator_stack = Stack()
    for element in data:
        if new_operator := OperatorFactory(element):
            handle_operator(onp, operator_stack, new_operator)
            continue
        if (parenthesis := ParenthesisFactory(element)) in Parenthesis.__members__.values():
            handle_parenthesis(onp, operator_stack, parenthesis)
            continue
        onp.enqueue(element)
        
    unload_stack(onp, operator_stack)

    result = str(onp)
    return result


def unload_stack(onp: ONP, operator_stack: Stack):
    top = operator_stack.peek_last()
    while top:
        op = operator_stack.pop()
        if op not in Parenthesis.__members__.items():
            onp.enqueue(op)
        top = operator_stack.peek_last()


def handle_parenthesis(onp: ONP, operator_stack: Stack, parenthesis: Parenthesis):
    if parenthesis == Parenthesis.OPENING:
        operator_stack.push(parenthesis)
    else:
        top = operator_stack.peek_last()
        while top != Parenthesis.OPENING:
            op = operator_stack.pop()
            if op not in Parenthesis.__members__.items():
                onp.enqueue(op)
            top = operator_stack.peek_last()
        operator_stack.pop()


def handle_operator(onp: ONP, operator_stack: Stack, new_operator: Operator):
    if operator_stack.is_empty:
        operator_stack.push(new_operator)
    elif new_operator > operator_stack.peek_last():
        operator_stack.push(new_operator)
    else:
        top = operator_stack.peek_last()
        while top:
            print(top, top >= new_operator, new_operator)
            if top >= new_operator:
                onp.enqueue(operator_stack.pop())
            else:
                break
            top = operator_stack.peek_last()
        operator_stack.push(new_operator)
