
You and your GPCR have navigated through PYMEMDYN™ unscathed, and now it's time to prepare input for QligFEP™. Fear not, as there's a collection of scripts available to assist you with this task! 

First, you get the pdb file you want to use as your starting point. This document contains your GPCR embedded within the membrane (POPC), along with ligand(s), ions, and water(HOH) molecules. Several things should happen before we continue. 

1) Reasonable amount of membrane should be cut since the system is huge. I usually cut it with VMD. 
Open the pdb file in VMD
Graphic --> Representations
set representation to: 
'''(same resid as (all within 32 of resname LIG) and resname POPC) and not water and not resname LIG or all protein (obviously you need to check what is your LIG name and also how much you want to cut)'''
Save this representation as pdb
Save ligand representation as pdb

2) What about the water molecules? Due to heavy solvation in our systems, GROMACS begins assigning alphanumeric names to water molecules. This causes confusion in both Pymol and VMD, leading to scrambled residue names for water in the output files. Use this instead:

**get_waters.pml**

Obtain the desired radius of water surrounding your protein using this Pymol script. The numbering of water molecules may still appear scrambled, and you might notice an unusual patch of water, but there's no need to worry. 
Your output should be: selected_water.pdb

**process_solvent.py**

This Python script restores the correct numbering of water molecules. Output is selected_waters_fixed.pdb

**merge.sh**

This script combines the previously obtained protein and membrane structures with your water PDB file.

Your task isn't complete yet. Due to slight differences in residue names and atom types between QligFEP and GROMACS output, we still need to address this. To do so, we utilize the script. 

**fix_pdb_Q.sh**

After all these steps, the only remaining (hopefully) issue to address is changing CYS to CYX if there is a cysteine bridge in your system. We hope this adjustment will ensure acceptance of your input by Q!




