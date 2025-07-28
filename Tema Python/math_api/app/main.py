from fastapi import FastAPI
from app.models import PowRequest, PowResponse
from app.operations import compute_pow
from app.storage import save_request
import asyncio

app = FastAPI()

@app.post("/pow", response_model=PowResponse)
async def pow_endpoint(data: PowRequest):
    result = await compute_pow(data.base, data.exponent)
    await save_request("pow", f"base={data.base}, exponent={data.exponent}", result)
    return PowResponse(result=result)



from app.models import (
    PowRequest, PowResponse,
    FibonacciRequest, FibonacciResponse,
    FactorialRequest, FactorialResponse
)
from app.operations import (
    compute_pow, compute_fibonacci, compute_factorial
)

# /pow deja există

@app.post("/fibonacci", response_model=FibonacciResponse)
async def fibonacci_endpoint(data: FibonacciRequest):
    result = await compute_fibonacci(data.n)
    await save_request("fibonacci", f"n={data.n}", result)
    return FibonacciResponse(result=result)

@app.post("/factorial", response_model=FactorialResponse)
async def factorial_endpoint(data: FactorialRequest):
    result = await compute_factorial(data.n)
    await save_request("factorial", f"n={data.n}", result)
    return FactorialResponse(result=result)
