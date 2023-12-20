# parses a vcf file with multiple samples
# creates a consensus sequence for a list of samples in the vcf
# returns the consensus sequence

import vcf
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
