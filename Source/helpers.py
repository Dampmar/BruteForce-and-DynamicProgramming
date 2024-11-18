def calculate_movement_cost(finger1, finger2):
    fret_average1 = calculate_fret_average(finger1)
    fret_average2 = calculate_fret_average(finger2)
    return (fret_average1 - fret_average2) ** 2

def calculate_fret_average(finger):
    accum : int = 0
    frets = 0
    for fret in finger:
        if fret is not None:
            accum += fret
            frets += 1
    return accum / frets if frets > 0 else 0.0

def total_movement_cost(sequence):
    """Calculate the total movement cost for a given sequence of chord fingerings."""
    cost = 0
    for i in range(1, len(sequence)):
        cost += calculate_movement_cost(sequence[i-1], sequence[i])
    return cost

if __name__ == "__main__":
    finger1 = [None,0,2,2,2,0]
    finger2 = [None,3,2,0,1,0]
    finger3 = [None,3,5,5,5,3]
    cost = calculate_movement_cost(finger1, finger2)
    cost += calculate_movement_cost(finger2, finger3)
    print(f"Movement cost between finger1 and finger2: {cost}")