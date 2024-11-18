from itertools import product
from helpers import calculate_movement_cost, total_movement_cost
from db_parser import db_parser
from file_parser import file_parser

def brute_force_optimal_fingerings(chord_list, chord_dict):
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
    best_cost = float('inf')
    best_sequence = None
    best_indices = None

    # Generate combinations of indices for the possible fingerings for each chord
    for idx_combination in product(*[range(len(f)) for f in chord_fingerings]):
        # Create the sequence of fingerings based on the indices
        sequence = [chord_fingerings[i][idx_combination[i]] for i in range(len(chord_list))]
        
        # Calculate the total movement cost for this sequence
        cost = total_movement_cost(sequence)
        
        # Update the best sequence if this one has a lower cost
        if cost < best_cost:
            best_cost = cost
            best_sequence = sequence
            best_indices = list(idx_combination)

    # Return the indices of the best sequence and the total cost
    return best_indices, best_cost

# Example usage
if __name__ == "__main__":
    # Load chord dictionary from your CSV file
    chord_dict = db_parser('GuitarDict.csv')

    # Load the list of chords from the song file
    chord_list = file_parser('/Users/dampmaringmail.com/Desktop/GitHub Repos/BruteForce-and-DynamicProgramming/Source/Example.txt')  # Ensure file_parser updates chord_list

    # Find the optimal sequence using brute-force
    optimal_indices, min_cost = brute_force_optimal_fingerings(chord_list, chord_dict)

    if optimal_indices:
        print(f"Optimal sequence found with cost {min_cost}:")
        print("Chosen fingerings:", optimal_indices)
    else:
        print("No optimal sequence found.")
