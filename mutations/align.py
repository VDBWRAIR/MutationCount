from Bio.Blast.Applications import NcbiblastnCommandline as blast
from Bio.Blast import NCBIXML
from Bio import SeqIO, pairwise2
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from StringIO import StringIO
from subprocess import Popen, PIPE, STDOUT
import sys

blastn_path = '/home/EIDRUdata/programs/blast+/bin/blastn'

def run_blast( seq, subject_fasta ):
    cline = blast( cmd=blastn_path, subject=subject_fasta, gapopen=5, gapextend=2, reward=1, penalty=-2, outfmt=5 )#, out='blastoutput.xml' ) #outfmt="6 qseqid sseqid evalue slen mismatch" )#, out='wrair2368t_pb2.xml' )
    p = Popen( str(cline).split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT )
    stdeo, stdin = p.communicate( input=seq.format( 'fasta' ) )

    return parse_blast( seq, stdeo )

def parse_blast( seq, output ):
    blast_output = StringIO( output )

    blast_records = NCBIXML.read( blast_output )

    try:
        alignment = blast_records.alignments[0]
    except:
        return (output, -1)

    hsp = alignment.hsps[0]

    mutations = get_muts( hsp.query, hsp.sbjct )

    return (mutations,1)

def pairwise_align( seq1, seq2 ):
    alignments = pairwise2.align.globalms( seq1, seq2, 1, -2, -5, -2 )
    count = 1
    get_muts( alignments[0][0], alignments[0][1] )

def tcoffee_align( seq1, seq2 ):
    seqs = StringIO()
    seqs.write( seq1.format( 'fasta' ) )
    seqs.write( seq2.format( 'fasta' ) )
    cmd = "t_coffee -in stdin -output fasta -outfile stdout -quiet" % tcoffee_path
    p = Popen( cmd.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT )
    stdeo, stdin = p.communicate( input = seqs.getvalue() )
    s = StringIO( stdeo )

    try:
        p = SeqIO.parse( s, 'fasta' )
        ref = p.next()
        s = p.next()
    except Exception:
        return (stdeo, -1)

    mutations = get_muts( ref.seq, s.seq )

    return (mutations,1)

def get_muts( sub_align, query_align ):
    mutations = []
    count = 1
    for q,s in zip( query_align, sub_align ):
        if q != s:
            mutations.append( "Q: %s S: %s Pos: %s" % (q, s, count) )
        count += 1
    return mutations

def count_seqs( file_name ):
    total_seq = 0
    fh = open( file_name )
    for l in fh:
        if l[0] == '>':
            total_seq += 1
    fh.close()

    return total_seq
