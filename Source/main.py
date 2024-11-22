import os
from db_parser import db_parser
from file_parser import file_parser

def main():
    filename = input("Enter the file to parse (in 'Test' folder): ")
    test_folderpath = "Test"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(os.path.dirname(current_dir), test_folderpath)
    database_dir = os.path.join(os.path.dirname(current_dir), "Database")
    filepath = os.path.join(test_dir, filename)
    db_path = os.path.join(database_dir, "GuitarDict.csv")

    # Retrieve the information necessary to parse the song
    chord_dict = db_parser(db_path)
    chord_list = file_parser(filepath)

    # Ask the user for the version
    while True:
        version = input("Which version?\n1. Constrained\n2. Original\nEnter the version number (1/2): ").strip()
        if version == "1":
            from brute_force_constraint import minimum_movement_brute_force
            break
        elif version == "2":
            from brute_force import minimum_movement_brute_force
            break
        else:
            print("Invalid version. Please enter '1' or '2'.")

    
    # Find the optimal sequence using brute-force   
    for chord in chord_list:
        if chord in chord_dict:
            print(f"Chord: {chord}")
            for key, value in chord_dict[chord].items():
                print(f"  {key}: {value}")
        else:
            print(f"Chord: {chord} is not in the dictionary.")

    optimal_indices, optimal_sequence, min_cost = minimum_movement_brute_force(chord_list, chord_dict)

    # Print if there is an optimal solution 
    if optimal_indices:
        print(f"Optimal sequence found with cost: {min_cost}")
        print("Chosen fingerings:", optimal_indices)
        print("Optimal Sequence:", optimal_sequence)
    else:
        print("No optimal sequence found.")

if __name__ == "__main__":
    main()