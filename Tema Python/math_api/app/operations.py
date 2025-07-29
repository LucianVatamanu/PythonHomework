import logging
logger = logging.getLogger(__name__)

_fib_cache = {}
_fact_cache = {} 

def compute_pow(base: float, exponent: float) -> float:
    return base ** exponent

def compute_fibonacci(n: int) -> int:
    if n in _fib_cache:
        return _fib_cache[n]
    logger.info(f"Calcul fibonacci({n})")
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        result = b
    _fib_cache[n] = result
    return result

def compute_factorial(n: int) -> int:
    if n in _fact_cache:
        return _fact_cache[n]
    logger.info(f"Calcul factorial({n})")

    if n == 0 or n == 1:
        result = 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
    _fact_cache[n] = result
    return result
