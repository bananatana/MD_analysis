import numpy as np

def read_pdb(filename):
    atoms = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('ATOM') or line.startswith('HETATM'):
                atom_type = line[12:16].strip()
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                if atom_type == 'OW': atom_type = 'O'
                if atom_type == 'HW': atom_type = 'H'
                if atom_type == 'HW1': atom_type = 'H'
                if atom_type == 'HW2': atom_type = 'H'
                atoms.append((atom_type, np.array([x, y, z])))
    return atoms

def compute_distances(atoms):
    oxygens = [atom for atom in atoms if atom[0] == 'O']
    hydrogens = [atom for atom in atoms if atom[0] == 'H']
    
    water_molecules = []
    for o_atom in oxygens:
        distances = [(h_atom, np.linalg.norm(o_atom[1] - h_atom[1])) for h_atom in hydrogens]
        distances.sort(key=lambda x: x[1])
        
        # Assuming the two closest hydrogens form a water molecule with the oxygen
        # and the distance is within a reasonable range for O-H bonds
        if distances[0][1] < 1.5 and distances[1][1] < 1.5:
            water_molecules.append((o_atom, distances[0][0], distances[1][0]))
    
    return water_molecules

def write_pdb(water_molecules, output_file):
    with open(output_file, 'w') as file:
        atom_id = 1
        res_id = 1
        for water in water_molecules:
            o_atom, h1_atom, h2_atom = water

            # Write oxygen atom
            file.write(f"ATOM  {atom_id:>5}  OW  HOH A{res_id:>4}    {o_atom[1][0]:>8.3f}{o_atom[1][1]:>8.3f}{o_atom[1][2]:>8.3f}  1.00  0.00           O\n")
            atom_id += 1

            # Write first hydrogen atom
            file.write(f"ATOM  {atom_id:>5} 1H   HOH A{res_id:>4}    {h1_atom[1][0]:>8.3f}{h1_atom[1][1]:>8.3f}{h1_atom[1][2]:>8.3f}  1.00  0.00           H\n")
            atom_id += 1

            # Write second hydrogen atom
            file.write(f"ATOM  {atom_id:>5} 2H   HOH A{res_id:>4}    {h2_atom[1][0]:>8.3f}{h2_atom[1][1]:>8.3f}{h2_atom[1][2]:>8.3f}  1.00  0.00           H\n")
            atom_id += 1

            res_id += 1

# Example usage
atoms = read_pdb('selected_water.pdb')
water_molecules = compute_distances(atoms)
write_pdb(water_molecules, 'selected_water_fixed.pdb')

