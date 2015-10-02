Other files
============
H3N2_BrisbaneRefGenbank__HA.fna was copied from a previous project and had been split up into separate genes

mutations__HA.mut
=================

Generated mutations__HA.mut via:

``#> ../../mutalign.py --subject H3N2_BrisbaneRefGenbank/H3N2_BrisbaneRefGenbank__HA.fna --query 125_H3N2_HA.fasta > mutations__HA.mut``

mutations__HA.mut.csv
=====================

Generated mutations__HA.mut.csv via:

``#> grep -v '^Q:' mutations__HA.mut | awk -F':' '{printf( "%s\t%s\n", $1, $3 )}' | sort -k 2 > mutations__HA.mut.csv``
