from typing import Any, List
from .queue import Queue, QueueDequeueError, QueuePeekError, LifoQueue


class StackException(Exception):
    pass


class StackPopError(StackException):
    pass


class StackPeekError(StackException):
    pass


class Stack:
    def __init__(self, queue: LifoQueue = LifoQueue()) -> None:
        self._queue = queue

    def __str__(self) -> str:
        return str(self._queue)

    @property
    def is_empty(self) -> bool:
        return self._queue.is_empty

    def push(self: Queue, element) -> None:
        self._queue.enqueue(element)

    def pop(self) -> Any:
        try:
            return self._queue.dequeue()
        except QueueDequeueError as exc:
            raise StackPopError from exc

    def peek(self, count=1, raise_exc=False) -> List[Any]:
        try:
            return self._queue.peek(count, raise_exc)
        except QueuePeekError as exc:
            raise StackPeekError from exc

    def peek_last(self, raise_exc=False) -> Any:
        try:
            return self._queue.peek_last(raise_exc=raise_exc)
        except QueuePeekError as exc:
            raise StackPeekError from exc