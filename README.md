# MD_analysis
Scripts for analysing MD simulations. 
You can discover Jupyter notebooks here that carry out specific analyses on Gromacs Molecular Dynamics Trajectories.

**mdtraj_rmsf_triplicates.ipynb**
This script performs RMSD analysis for both the ligand and protein, as well as RMSF analysis for the protein, across triplicate trajectories. It also computes the average RMSD and RMSF for each trajectory frame, generating plots that display the data alongside standard deviation information.

**pca_conformations.ipynb**
The script performs Principal Component Analysis (PCA) using CA-CA distances from an MD trajectory and subsequently applies K-Means clustering. Following the visualization of the results, it preserves a representative PDB structure for each cluster within every PCA combination. The representative structure is determined as the actual structure that is geometrically closest to the average structure within the cluster.