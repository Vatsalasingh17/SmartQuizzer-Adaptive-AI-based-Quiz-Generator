def calculate_next_difficulty(score: float, current: str):
    if score >= 0.8:
        return "hard" if current != "hard" else "hard"
    elif score >= 0.5:
        return current
    else:
        return "easy"
