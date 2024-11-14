def file_parser(filename):
    chord_list = []

    try:
        with open(filename, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                chord_name = line.strip()
                if chord_name:
                    chord_list.append(chord_name)
            
            for chord in chord_list:
                print(f"{chord.ljust(10)}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        exit(1)

file_parser('GuitarChords.txt')