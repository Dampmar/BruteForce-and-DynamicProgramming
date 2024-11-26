from brute_force_bounded import calculate_movement_displacement
import math

def minimum_movement_dynamic_programming(chord_list, chord_dict):
    """Dynamic Programming solution to find the sequence of chord fingerings that displaces the hand the least."""
    def is_valid_fingering(fingering):
        """Check if the fingering's minimum fret is 7 or less."""
        valid_frets = [fret for fret in fingering if fret is not None]
        if not valid_frets:
            return False
        return min(valid_frets) <= 7

    chord_fingerings = []
    for chord in chord_list:
        if chord in chord_dict:
            fingerings = []
            for key in ['Finger A', 'Finger B', 'Finger C']:
                if key in chord_dict[chord]:
                    fingering = chord_dict[chord][key]
                    fingerings.append(fingering)

            # Check if any fingerings are available
            if fingerings:
                chord_fingerings.append(fingerings)
            else:
                print(f"Warning: No valid fingerings for chord '{chord}'.")
                return None
        else:
            print(f"Warning: Chord '{chord}' not found in dictionary.")
            return None

    n = len(chord_list)
    Oracle = [{} for _ in range(n)]  # Each entry is a dictionary
    Solution = [{} for _ in range(n)]  # Tracks previous indices

    # Initialize the base case
    for f, fingering in enumerate(chord_fingerings[0]):
        if is_valid_fingering(fingering):  # Only consider valid fingerings
            Oracle[0][f] = 0

    # Fill the Oracle
    for i in range(1, n):
        for f, fingering in enumerate(chord_fingerings[i]):  # Current fingerings
            if not is_valid_fingering(fingering):  # Skip invalid fingerings
                continue
            Oracle[i][f] = float('inf')  # Start with a high cost
            for f_prev, prev_fingering in enumerate(chord_fingerings[i - 1]):  # Previous fingerings
                if not is_valid_fingering(prev_fingering):  # Skip invalid previous fingerings
                    continue
                cost = Oracle[i - 1][f_prev] + calculate_movement_displacement(prev_fingering, fingering)
                if cost < Oracle[i][f]:
                    Oracle[i][f] = cost
                    Solution[i][f] = f_prev

    # Find the minimum cost and corresponding fingering for the last chord
    min_cost = float('inf')
    min_cost_index = None
    for f, cost in Oracle[n - 1].items():
        if cost < min_cost:
            min_cost = cost
            min_cost_index = f

    # Reconstruct the optimal sequence and indexes
    sequence = []
    indexes = []
    f = min_cost_index
    for i in range(n - 1, -1, -1):
        sequence.append(chord_fingerings[i][f])
        indexes.append(f)
        f = Solution[i].get(f, None)
    sequence.reverse()
    indexes.reverse()

    # Normalize the cost
    min_cost = math.sqrt(min_cost)
    min_cost = round(min_cost, 2)

    return indexes, sequence, min_cost
