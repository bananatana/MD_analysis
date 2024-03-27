def merge_pdb_files(file1, file2, output):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Write content of the first file
        for line in lines1[:-1]:  # Exclude the last line (END) of the first file
            out.write(line)

        # If there are no lines starting with "END" in the first file, add one
        if not any(line.startswith('END') for line in lines1):
            out.write('END\n')

        # Write content of the second file
        for line in lines2:
            out.write(line)

        # If there are no lines starting with "END" in the second file, add one
        if not any(line.startswith('END') for line in lines2):
            out.write('END\n')

    print(f"Merged PDB saved to '{output}'")

if __name__ == "__main__":
    file1_path = "7xy7_HID_membrane.pdb"
    file2_path = "selected_water_fixed.pdb"
    output_path = "7XY6_HID_protein_merged.pdb"

    merge_pdb_files(file1_path, file2_path, output_path)
