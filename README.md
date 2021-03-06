# Backbone linkage of cyclic peptides
Backbone cyclization of peptides head-to-tail. 
Used in the glycindel scaffolding method of "Hsueh et al." (Optimizing epitope conformational ensembles using alpha-synuclein cyclic peptide ``glycindel'' scaffolds: A method for generating oligomer-selective antibodies for Parkinson's disease)

## pre-requisites
* GROMACS
* Scwrl4

## Before you run
In scripts folder:
* Change the [Path to Scwrl4 executable] in run2.sh to your installed path.
* If you installed GROAMCS with version 5 or greater, please prepend the gromacs-related command with gmx (ex. grompp, pdb2gmx, editconf, mdrun)
* Change the prot.pdb to be the PDB structure that contains your sequence of interest
* Change the text in seq file to be the sequence in lower case of prot.pdb
* At the top of systematically_run.sh, change the range of i and j according to the number of Glycines you want to append on the left (i) and right side (j) of the peptide

## Command
```
./systematically_run.sh <peptide SEQUENCE>
 ```
  
After the command is run, there are 3 file outputs:
* The gromacs topology file (.top), 
* The gro structure (.gro), 
* The position restraint file (.itp) 
These will be deposited in a new folder named C<G (repeat i times)>\<SEQUENCE\><G (repeat j times)>s (for example: CGGKTKEGs)

## Example
The example folder shows the content after running 
 ```
./systematically_run.sh KTKE
 ```
In this example, the prot.pdb contains the alphasynuclein structure (chain A of the PDB entry 2N0A), and the seq file contains the corresponding sequence (KTKE). The variables i and j in systematically_run.sh file are 2 and 1, respectively, so the sequence after glycindel process is CGGKTKEG. The files for GROMACS MD simulation are deposited in a folder named "CGGKTKEGs".
