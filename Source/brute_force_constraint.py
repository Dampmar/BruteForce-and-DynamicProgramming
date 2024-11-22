from itertools import product 
import math

def calculate_movement_displacement(a, b):
    """Calculate the cost of moving between chord play forms (fingering)"""
    average_fret_a = calculate_average_fret(a)
    average_fret_b = calculate_average_fret(b)

    # Increases the impact of big distances, and decreases that of small distances
    return (average_fret_a - average_fret_b)**2

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
    Only considers fingerings whose lowest fret does not exceed the 7th fret.
    Returns a list of indices representing chosen fingerings for each chord.
    """
    # Generate all possible fingerings for each chord in the song, considering the constraint. Looks to generate all possible solutions while using iterables instead of recursion
    chord_fingerings = []
    for chord in chord_list:
        if chord in chord_dict:
            fingerings = []
            # Filter available fingerings based on the 7th fret constraint
            for key in ['Finger A', 'Finger B', 'Finger C']:
                if key in chord_dict[chord]:
                    fingering = chord_dict[chord][key]
                    fingerings.append(fingering)

            # Check if any valid fingerings remain
            if fingerings:
                chord_fingerings.append(fingerings)
            else:
                print(f"Warning: No valid fingerings for chord '{chord}'.")
                return None 
        else:
            print(f"Warning: Chord '{chord}' not found in dictionary.")
            return None 

    # Generate all possible combinations and track their indices 
    min_cost = float('inf')
    min_cost_sequence = None 
    min_cost_indices = None 

    # Generate combinations of indices for possible fingerings for each chord, to use a loop
    for idx_combination in product(*[range(len(f)) for f in chord_fingerings]):
        # Create the sequence of fingerings based on the indices
        sequence = [chord_fingerings[i][idx_combination[i]] for i in range(len(chord_list))]
        
        # Revise the constraint for each sequence, if constraint is broken continue with next
        if any(min(fret for fret in fingering if fret is not None) > 7 for fingering in sequence):
            continue 

        # Calculate the total movement cost for this sequence of fingerings
        cost = total_movement_cost(sequence)

        # Update the best sequence if this one has a lower cost
        if cost < min_cost:
            min_cost_sequence = sequence
            min_cost = cost                             # Overwritting of solution
            min_cost_indices = list(idx_combination)    # Sigma vector saving
    
    # Normalize the results from (frets**2) to (frets)
    min_cost = math.sqrt(min_cost)
    min_cost = round(min_cost, 2)
    
    # Return the indices of the best sequence (vector) and the total cost
    return min_cost_indices, min_cost_sequence, min_cost