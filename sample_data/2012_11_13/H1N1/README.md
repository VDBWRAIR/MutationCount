Other files
============
mexico_ref_split is a directory containing the reference used split up into all the genes

mutations__HA.mut
=================

Generated mutations__HA.mut via:

``#> ../../mutalign.py --subject mexico_ref_split/mexico_ref__HA.fna --query 75_pdm_H1N1HA.fasta > mutations__HA.mut``

mutations__HA.mut.csv
=====================

Generated mutations__HA.mut.csv via:

``#> grep -v '^Q:' mutations__HA.mut | awk -F':' '{printf( "%s\t%s\n", $1, $3 )}' | sort -k 2 > mutations__HA.mut.csv``
