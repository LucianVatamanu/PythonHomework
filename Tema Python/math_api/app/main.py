from fastapi import FastAPI
from app.models import (
    PowRequest, PowResponse,
    FibonacciRequest, FibonacciResponse,
    FactorialRequest, FactorialResponse
)
from app.operations import (
    compute_pow, compute_fibonacci, compute_factorial
)
from app.storage import save_request
import asyncio
import logging

# Configurare logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

# pow
@app.post("/pow", response_model=PowResponse)
async def pow_endpoint(data: PowRequest):
    result = compute_pow(data.base, data.exponent)
    save_request("pow", f"base={data.base}, exponent={data.exponent}", result)
    logger.info(f"/pow: base={data.base}, exponent={data.exponent} → {result}")
    return PowResponse(result=result)

# fibonacci
@app.post("/fibonacci", response_model=FibonacciResponse)
async def fibonacci_endpoint(data: FibonacciRequest):
    result = compute_fibonacci(data.n)
    save_request("fibonacci", f"n={data.n}", result)
    logger.info(f"/fibonacci: n={data.n} → {result}")
    return FibonacciResponse(result=result)

# factorial
@app.post("/factorial", response_model=FactorialResponse)
async def factorial_endpoint(data: FactorialRequest):
    result = compute_factorial(data.n)
    save_request("factorial", f"n={data.n}", result)
    logger.info(f"/factorial: n={data.n} → {result}")
    return FactorialResponse(result=result)
