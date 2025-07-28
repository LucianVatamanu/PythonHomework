from pydantic import BaseModel

class PowRequest(BaseModel):
    base: float
    exponent: float

class PowResponse(BaseModel):
    result: float

from pydantic import BaseModel, Field

# Fibonacci
class FibonacciRequest(BaseModel):
    n: int = Field(ge=0, description="n trebuie să fie >= 0")

class FibonacciResponse(BaseModel):
    result: int

# Factorial
class FactorialRequest(BaseModel):
    n: int = Field(ge=0, description="n trebuie să fie >= 0")

class FactorialResponse(BaseModel):
    result: int