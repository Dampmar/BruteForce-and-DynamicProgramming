def calculate_movement_cost(finger1, finger2):
    """Calculate the movement cost between two chord fingerings based on fret averages."""
    fret_average1 = calculate_fret_average(finger1)
    fret_average2 = calculate_fret_average(finger2)
    return (fret_average1 - fret_average2) ** 2

def calculate_fret_average(finger):
    """Calculate the average fret position for a given chord fingering."""
    accum = 0
    frets = 0
    
    for fret in finger:
        if fret is not None:  # Count only played strings
            accum += fret
            frets += 1

    # Avoid division by zero if all strings are muted
    return accum / frets if frets > 0 else 0.0

# Example fingerings (None means the string is muted)
finger1 = [3, 2, 0, 0, 3, None]   # C major chord
finger2 = [1, 3, 3, 2, 1, 1]     # F major barre chord

cost = calculate_movement_cost(finger1, finger2)
print(f"Movement cost between finger1 and finger2: {cost}")