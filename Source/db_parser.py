import csv

def db_parser(filename):
    chord_dict = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 2:
                    continue

                # First element is the chord name
                chord_name = row[0].strip()

                # Calculate first fingering (columns 2-7)
                try:
                    offsetA = int(row[1]) if row[1] and row[1].isdigit() else 1
                    fingerA = [
                        (int(x) + offsetA - 1) if x and x.isdigit() else None
                        for x in row[2:8]
                    ]
                except ValueError:
                    fingerA = None

                # Calculate second fingering (columns 9-14), if available
                fingerB = None
                try:
                    if len(row) > 8:
                        offsetB = int(row[8]) if row[8] and row[8].isdigit() else 1
                        fingerB = [
                            (int(x) + offsetB - 1) if x and x.isdigit() else None
                            for x in row[9:15]
                        ]
                        if all(f is None for f in fingerB):
                            fingerB = None
                except ValueError:
                    fingerB = None

                # Calculate third fingering (columns 17-22), if available
                fingerC = None
                try:
                    if len(row) > 16:
                        offsetC = int(row[15]) if row[15] and row[15].isdigit() else 1
                        fingerC = [
                            (int(x) + offsetC - 1) if x and x.isdigit() else None
                            for x in row[16:22]
                        ]
                        if all(f is None for f in fingerC):
                            fingerC = None
                except ValueError:
                    fingerC = None

                # Populate the chord dictionary
                chord_dict[chord_name] = {"Offset A": offsetA, "Finger A": fingerA}
                if fingerB:
                    chord_dict[chord_name]["Offset B"] = offsetB
                    chord_dict[chord_name]["Finger B"] = fingerB
                if fingerC:
                    chord_dict[chord_name]["Offset C"] = offsetC
                    chord_dict[chord_name]["Finger C"] = fingerC

        return chord_dict

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        exit(1)
