#!/usr/bin/env bash

export METADATA_FILE=$1

# Download fasta sequences from a list of sequence accessions (skip first line)
{
  read
    while IFS=, read -r accession country collection_date host strain isolate
    do
      wget https://www.ebi.ac.uk/ena/browser/api/fasta/${accession}?download=true >> insdc_sequences.fasta
    done
} < ${METADATA_FILE}
