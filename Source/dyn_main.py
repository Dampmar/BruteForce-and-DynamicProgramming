import os
from db_parser import db_parser
from file_parser import file_parser
from dynamic_prog import minimum_movement_dynamic_programming

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

    optimal_indices, optimal_sequence, min_cost = minimum_movement_dynamic_programming(chord_list, chord_dict)

    # Print if there is an optimal solution 
    if optimal_indices:
        print(f"Optimal sequence found with cost: {min_cost}")
        print("Chosen fingerings:", optimal_indices)
        print("Optimal Sequence:", optimal_sequence)
    else:
        print("No optimal sequence found.")

if __name__ == "__main__":
    main()