for i in {2..2}
do
    for j in {1..1}
    do
	rm topol*
	leftG=$(perl -sE 'say "G" x "$times"' -- -times=${i})
	rightG=$(perl -sE 'say "G" x "$times"' -- -times=${j})
	echo $leftG
	seq=${leftG}$1${rightG}
	echo $seq
	seqlower=$(echo "$1" | tr '[:upper:]' '[:lower:]')
	echo $seqlower
	leftshift=$(echo $i+2 | bc)
	rightshift=$(echo $j+2 | bc)
	mkdir -p C${seq}s
	echo GC${seq}CG $leftshift $rightshift
	echo -e "1\n 1\n" | ./run2.sh seq GC${seq}CG seq_mut prot.pdb prot_mut.pdb GC${seq}CG.pdb C${seq} $seqlower $leftshift $rightshift
	mv C${seq}_min.gro topol.top posre.itp C${seq}s
	
    done
done
