# gmx-cyclize
cyclize peptides using glycindel scaffolding method

## pre-requite
* GROMACS
* Scwrl4

## Before you run
In scripts folder
* Change the [Path to Scwrl4 executable] in run2.sh to your installed path.
* If you installed GROAMCS with version > 5. Please prepend the gromacs-related command with gmx (ex. grompp, pdb2gmx, editconf, mdrun)
* Change the prot.pdb to be the PDB structure that contains your sequence of interest
* Change the text in seq file to be the sequence in lower case of prot.pdb
* At the top of systematically_run.sh, change the range of i and j according to the number of Glycines you want to append on the left and right side of the peptide

## Command
```
./systematically_run.sh <peptide SEQUENCE>
 ```
  
After the command was run, the gromacs topology file (.top), gro structure (.gro), and position restraint file (.itp) will be deposited in a new folder named C<G (repeat i times)>\<SEQUENCE\><G (repeat j times)>s (ex. CGGKTKEGs)

## Example
The example folder shows the content after running 
 ```
./systematically_run.sh KTKE
 ```
The prot.pdb contains the alphasynuclein structure (chain A of the PDB entry 2N0A), and the seq file contain the corresponding sequence. The variable i and j in systematically_run.sh file are 2 and 1, respectively, so the sequence after glycindel process is CGGKTKEG. The files for GROMACS MD simulation are deposited in CGGKTKEGs.
