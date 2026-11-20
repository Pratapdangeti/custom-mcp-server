import math
import statistics


def calculate_sum(values: list[float]) -> float:
    return float(sum(values))


def calculate_average(values: list[float]) -> float:
    if not values:
        raise ValueError("Input list cannot be empty")
    return float(statistics.mean(values))


def calculate_standard_deviation(values: list[float]) -> float:
    if len(values) < 2:
        raise ValueError("At least two values required")
    return float(statistics.stdev(values))


def calculate_percentage_change(old_value: float, new_value: float) -> float:
    if old_value == 0:
        raise ValueError("Old value cannot be zero")
    return ((new_value - old_value) / abs(old_value)) * 100


def calculate_level_drop(
    previous_level: float, current_level: float, tote_capacity: float
) -> float:
    if not 0 <= previous_level <= 100:
        raise ValueError("Invalid previous level")
    if not 0 <= current_level <= 100:
        raise ValueError("Invalid current level")
    if tote_capacity <= 0:
        raise ValueError("Capacity must be positive")

    drop_percentage = max(previous_level - current_level, 0)

    return (drop_percentage / 100) * tote_capacity
