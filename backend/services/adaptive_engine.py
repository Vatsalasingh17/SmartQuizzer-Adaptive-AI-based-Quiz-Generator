def calculate_next_difficulty(score: float, current: str):
    """
    Determine the next difficulty level based on a given score and current difficulty.

    Args:
        score (float): Performance score, typically between 0.0 and 1.0.
        current (str): Current difficulty level ("easy", "medium", "hard", etc.)

    Returns:
        str: The next difficulty level.
    """

    # If the score is high (>= 0.8), increase difficulty to "hard".
    # If it's already "hard", it remains "hard".
    if score >= 0.8:
        return "hard"

    # If the score is moderate (>= 0.5), keep the current difficulty unchanged.
    elif score >= 0.5:
        return current

    # If the score is low (< 0.5), reduce difficulty to "easy".
    else:
        return "easy"
