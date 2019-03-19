import sys
from typing import Any, Callable, Generic, Dict, Iterable, Mapping, Optional, Sequence, Tuple, Type, TypeVar, NamedTuple, Union, overload

_AnyCallable = Callable[..., Any]

_T = TypeVar("_T")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_S = TypeVar("_S")
@overload
def reduce(function: Callable[[_T, _S], _T],
           sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T],
           sequence: Iterable[_T]) -> _T: ...


class _CacheInfo(NamedTuple('CacheInfo', [
    ('hits', int),
    ('misses', int),
    ('maxsize', int),
    ('currsize', int)
])): ...

class _lru_cache_wrapper(Generic[_T]):
    __wrapped__ = ...  # type: Callable[..., _T]
    def __call__(self, *args: Any, **kwargs: Any) -> _T: ...
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...

class lru_cache():
    def __init__(self, maxsize: Optional[int] = ..., typed: bool = ...) -> None: ...
    def __call__(self, f: Callable[..., _T]) -> _lru_cache_wrapper[_T]: ...


WRAPPER_ASSIGNMENTS = ...  # type: Sequence[str]
WRAPPER_UPDATES = ...  # type: Sequence[str]

def update_wrapper(wrapper: _AnyCallable, wrapped: _AnyCallable, assigned: Sequence[str] = ...,
                   updated: Sequence[str] = ...) -> _AnyCallable: ...
def wraps(wrapped: _AnyCallable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[_AnyCallable], _AnyCallable]: ...
def total_ordering(cls: type) -> type: ...
def cmp_to_key(mycmp: Callable[[_T, _T], int]) -> Callable[[_T], Any]: ...

@overload
def partial(func: Callable[[_T], _S], arg: _T) -> Callable[[], _S]: ...
@overload
def partial(func: Callable[[_T, _T2], _S], arg: _T) -> Callable[[_T2], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3], _S], arg: _T) -> Callable[[_T2, _T3], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3, _T4], _S], arg: _T) -> Callable[[_T2, _T3, _T4], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3, _T4, _T5], _S], arg: _T) -> Callable[[_T2, _T3, _T4, _T5], _S]: ...

@overload
def partial(func: Callable[[_T, _T2], _S],
            arg1: _T,
            arg2: _T2) -> Callable[[], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3], _S],
            arg1: _T,
            arg2: _T2) -> Callable[[_T3], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3, _T4], _S],
            arg1: _T,
            arg2: _T2) -> Callable[[_T3, _T4], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3, _T4, _T5], _S],
            arg1: _T,
            arg2: _T2) -> Callable[[_T3, _T4, _T5], _S]: ...

@overload
def partial(func: Callable[[_T, _T2, _T3], _S],
            arg1: _T,
            arg2: _T2,
            arg3: _T3) -> Callable[[], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3, _T4], _S],
            arg1: _T,
            arg2: _T2,
            arg3: _T3) -> Callable[[_T4], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3, _T4, _T5], _S],
            arg1: _T,
            arg2: _T2,
            arg3: _T3) -> Callable[[_T4, _T5], _S]: ...

@overload
def partial(func: Callable[[_T, _T2, _T3, _T4], _S],
            arg1: _T,
            arg2: _T2,
            arg3: _T3,
            arg4: _T4) -> Callable[[], _S]: ...
@overload
def partial(func: Callable[[_T, _T2, _T3, _T4, _T5], _S],
            arg1: _T,
            arg2: _T2,
            arg3: _T3,
            arg4: _T4) -> Callable[[_T5], _S]: ...

@overload
def partial(func: Callable[[_T, _T2, _T3, _T4, _T5], _S],
            arg1: _T,
            arg2: _T2,
            arg3: _T3,
            arg4: _T4,
            arg5: _T5) -> Callable[[], _S]: ...

@overload
def partial(func: Callable[..., _S],
            *args: Any,
            **kwargs: Any) -> Callable[..., _S]: ...

# With protocols, this could change into a generic protocol that defines __get__ and returns _T
_Descriptor = Any

class partialmethod(Generic[_T]):
    func: Union[Callable[..., _T], _Descriptor]
    args: Tuple[Any, ...]
    keywords: Dict[str, Any]

    @overload
    def __init__(self, func: Callable[..., _T], *args: Any, **keywords: Any) -> None: ...
    @overload
    def __init__(self, func: _Descriptor, *args: Any, **keywords: Any) -> None: ...
    def __get__(self, obj: Any, cls: Type[Any]) -> Callable[..., _T]: ...
    @property
    def __isabstractmethod__(self) -> bool: ...

class _SingleDispatchCallable(Generic[_T]):
    registry = ...  # type: Mapping[Any, Callable[..., _T]]
    def dispatch(self, cls: Any) -> Callable[..., _T]: ...
    @overload
    def register(self, cls: Any) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    @overload
    def register(self, cls: Any, func: Callable[..., _T]) -> Callable[..., _T]: ...
    def _clear_cache(self) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> _T: ...

def singledispatch(func: Callable[..., _T]) -> _SingleDispatchCallable[_T]: ...
