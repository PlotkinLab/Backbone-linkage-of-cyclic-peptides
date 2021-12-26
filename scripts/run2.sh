#!/bin/bash
name=${6%.*}
echo $name
Scwrl4='[Path to Scwrl4 executable]'

python mut_seq_part1.py $1 $2 $3 $4 $5 $6 $8 $9 ${10}
${Scwrl4} -i $4 -o $5 -s $3
python mut_seq_part2.py $1 $2 $3 $4 $5 $6 $8 $9 ${10}
editconf -f $6 -resnr 10 -o ${name}_1.pdb
pdb2gmx -f ${name}_1.pdb -o $7.gro -ignh -missing
python edit_topol.py topol.top topol1.top $2
python shift_topol.py topol1.top $7.gro posre.itp $2
editconf -f $7.gro -o $7_box.gro -d 1.2 -bt cubic
grompp -f min.mdp -c $7_box.gro -p topol1.top -o $7_min.tpr
mdrun -deffnm $7_min
python edit_topol1.py topol1.top topol.top
