from langchain_core.tools import tool
import math
import statistics
from typing import List, Union, Optional


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b


@tool
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b


@tool
def divide(a: float, b: float) -> float:
    """Divide a by b and return the result. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


