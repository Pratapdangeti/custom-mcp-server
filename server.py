from mcp.server.fastmcp import FastMCP

from math_functions import (
    calculate_sum,
    calculate_average,
    calculate_standard_deviation,
    calculate_percentage_change,
    calculate_level_drop,
)

mcp = FastMCP(
    "custom-math-mcp",
    host="0.0.0.0",
    port=8080,
    stateless_http=True,
    json_response=True,
)


@mcp.tool()
def sum_values(values: list[float]) -> float:
    """Calculate sum of numeric values."""
    return calculate_sum(values)


@mcp.tool()
def average_values(values: list[float]) -> float:
    """Calculate arithmetic mean of numeric values."""
    return calculate_average(values)


@mcp.tool()
def standard_deviation(values: list[float]) -> float:
    """Calculate sample standard deviation."""
    return calculate_standard_deviation(values)


@mcp.tool()
def percentage_change(old_value: float, new_value: float) -> float:
    """Calculate percentage change between two values."""
    return calculate_percentage_change(old_value, new_value)


@mcp.tool()
def level_drop_gallons(
    previous_level: float, current_level: float, tote_capacity: float
) -> float:
    """
    Calculate gallons consumed from a percentage
    decrease in tote level.
    """
    return calculate_level_drop(previous_level, current_level, tote_capacity)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
