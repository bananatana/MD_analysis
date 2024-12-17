# MD_analysis
Scripts for analysing MD simulations. 
You can discover Jupyter notebooks here that carry out specific analyses on Gromacs Molecular Dynamics Trajectories.

**mdtraj_rmsf_triplicates.ipynb**

This script performs RMSD analysis for both the ligand and protein, as well as RMSF analysis for the protein, across triplicate trajectories. It also computes the average RMSD and RMSF for each trajectory frame, generating plots that display the data alongside standard deviation information.

**pca_conformations.ipynb**

The script performs Principal Component Analysis (PCA) using CA-CA distances from an MD trajectory and subsequently applies K-Means clustering. 
Within the script, the Elbow method is performed to determine number of clusters.
Following the visualization of the results, it preserves a representative PDB structure for each cluster within desired PCA combination. The representative structure is determined as the actual structure that is geometrically closest (RMSD) to the average structure within the cluster.

**mdtraj_rmsf_ligand_per_atom.ipynb**

The script computes the RMSF of heavy ligand atoms, both for each individual MD replica and collectively across multiple replicas, including the standard deviation. The results are presented as histograms, with an option to display functional groups in distinct colors.

**water_bridge_TT.ipynb**

The script computes the number of "water-bridged" hydrogen bonds for the specified residues. The results are stored in a pandas DataFrame for further analysis and exported to a CSV file, with one replicate listed below the other. Additionally, the script calculates the average occupancy across three replicates for the selected residues.
