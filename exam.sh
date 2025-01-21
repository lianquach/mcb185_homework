# Determine if there are more genes on the + or - strand in the C. elegans genome 
gunzip -c ~/Code/MCB185/data/C.elegans.gff.gz | cut -f7 | grep -c "+"
gunzip -c ~/Code/MCB185/data/C.elegans.gff.gz | cut -f7 | grep -c "-"

# Determine if the E.coli proteome has more proteins described as helicase or transposase
gunzip -c ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz | grep -c "helicase"
gunzip -c ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz | grep -c "transposase"
