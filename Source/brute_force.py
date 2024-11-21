from itertools import product 

def calculate_movement_displacement(a, b):
    """Calculate the cost of moving between chord play forms (fingering)"""
    average_fret_a = calculate_average_fret(a)
    average_fret_b = calculate_average_fret(b)

    # Increases the impact of big distances, and decreases that of small distances
    return (average_fret_a - average_fret_b) ** 2

def calculate_average_fret(x):
    """Calculate the average fret of a manner of chord play form (fingering)"""
    accum : int = 0
    frets : int = 0
    for fret in x:
        if fret is not None:
            accum += fret
            frets += 1
    return accum / frets if frets > 0 else 0.0

def total_movement_cost(sequence):
    """Calculate the total movement cost for a given sequence of chord play forms"""
    cost = 0
    # The first chord played doesn't add cost, start at the second
    for i in range(1, len(sequence)):
        cost += calculate_movement_displacement(sequence[i-1], sequence[i])
    return cost 

def minimum_movement_brute_force(chord_list, chord_dict):
    """
    Find the optimal sequence of chord fingerings using a brute-force approach.
    Returns a list of indices representing chosen fingerings for each chord.
    """
    # Generate all possible fingerings for each chord in the song
    chord_fingerings = []
    for chord in chord_list:
        if chord in chord_dict:
            fingerings = []
            # Append available fingerings from the dictionary
            fingerings.append(chord_dict[chord]['Finger A'])
            if 'Finger B' in chord_dict[chord]:
                fingerings.append(chord_dict[chord]['Finger B'])
            if 'Finger C' in chord_dict[chord]:
                fingerings.append(chord_dict[chord]['Finger C'])
            chord_fingerings.append(fingerings)
        else:
            print(f"Warning: Chord '{chord}' not found in dictionary.")
            return None

    # Generate all possible combinations of fingerings and track their indices
    min_cost = float('inf')
    min_cost_sequence = None
    min_cost_indices = None

    # Generate combinations of indices for the possible fingerings for each chord
    for idx_combination in product(*[range(len(f)) for f in chord_fingerings]):
        # Create the sequence of fingerings based on the indices
        sequence = [chord_fingerings[i][idx_combination[i]] for i in range(len(chord_list))]
        
        # Calculate the total movement cost for this sequence
        cost = total_movement_cost(sequence)
        
        # Update the best sequence if this one has a lower cost
        if cost < min_cost:
            min_cost = cost
            min_cost_sequence = sequence
            min_cost_indices = list(idx_combination)

    # Return the indices of the best sequence and the total cost
    return min_cost_indices, min_cost_sequence, min_cost