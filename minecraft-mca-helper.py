def get_coordinate(prompt: str) -> int:
    """ Prompts the user for a coordinate and safely returns it as an integer. """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def process_region(region_id: int) -> None:
    """ Processes coordinates for a single region and prints all corresponding .mca files. """
    x1 = get_coordinate(f"Region {region_id} - Enter the first x-Coordinate: ")
    z1 = get_coordinate(f"Region {region_id} - Enter the first z-Coordinate: ")
    x2 = get_coordinate(f"Region {region_id} - Enter the second x-Coordinate: ")
    z2 = get_coordinate(f"Region {region_id} - Enter the second z-Coordinate: ")

    # Koordinaten von klein nach groß sortieren
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_z, max_z = min(z1, z2), max(z1, z2)

    print(f"The top-left corner is x: {min_x} / z: {min_z}")
    print(f"The bottom-right corner is x: {max_x} / z: {max_z}")
    print("List of all mca-files in that region:")

    file_count = 0
    # Iteration durch das Raster inkl. der Endpunkte (+1)
    for x in range(min_x, max_x + 1):
        for z in range(min_z, max_z + 1):
            print(f"{x}.{z}.mca")
            file_count += 1

    print(f"Region {region_id} contains a total of {file_count} .mca-files\n")

def main() -> None:
    """ Main entry point to query the amount of regions and execute the processing. """
    try:
        num_regions = int(input("Enter the amount of regions (from 1 to 9): "))
    except ValueError:
        print("Amount of regions invalid!")
        return

    # Validierung der Regionen-Anzahl
    if not (1 <= num_regions <= 9):
        print("Amount of regions invalid!")
        return

    # Durchlauf für jede Region
    for region_id in range(1, num_regions + 1):
        process_region(region_id)

if __name__ == "__main__":
    main()