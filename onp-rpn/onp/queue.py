from abc import abstractmethod
from copy import deepcopy
from typing import Any, List, Optional, Type


class QueueException(Exception):
    pass


class QueueDequeueError(QueueException):
    pass

class QueuePeekError(QueueException):
    pass


class Queue:
    def __init__(self, init_data: Optional[List[Any]] = None) -> None:
        if init_data is None:
            init_data = []
        self._queue = init_data
        self._length = len(init_data)

    def __str__(self) -> str:
        return str([str(_) for _ in self._queue])

    @property
    def is_empty(self) -> bool:
        return self._length < 1

    @abstractmethod
    def dequeue(self) -> Any:
        pass

    @abstractmethod
    def enqueue(self, element) -> None:
        pass


class FifoMixin:
    def enqueue(self: Queue, element) -> None:
        self._queue.append(element)
        self._length += 1

    def dequeue(self: Queue) -> Any:
        if self.is_empty:
            raise QueueDequeueError
        element = self._queue.pop(0)
        self._length -= 1
        return element

    def peek(self: Queue, count=1, raise_exc=False) -> List[Any]:
        if count > self._length:
            if raise_exc is True:
                raise QueuePeekError
            return self._queue
        return self._queue[0:count]

    def peek_last(self):
        try:
            return self.peek()[0]
        except IndexError as exc:
            raise QueuePeekError from exc


class LifoMixin:
    def enqueue(self: Queue, element):
        self._queue.append(element)
        self._length += 1

    def dequeue(self: Queue) -> Any:
        if self.is_empty:
            raise QueueDequeueError
        element = self._queue.pop()
        self._length -= 1
        return element

    def peek(self: Queue, count=1, raise_exc=False) -> List[Any]:
        if count > self._length:
            if raise_exc is True:
                raise QueuePeekError
            return self._queue
        return self._queue[-count:]

    def peek_last(self, raise_exc=False) -> Any:
        try:
            return self.peek(raise_exc=raise_exc)[0]
        except IndexError as exc:
            if not raise_exc:
                return None
            raise QueuePeekError from exc


class LifoQueue(LifoMixin, Queue):
    pass


class FifoQueue(FifoMixin, Queue):
    pass
