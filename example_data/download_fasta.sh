#!/usr/bin/env bash

export METADATA_FILE=$1

# Download fasta sequences from a list of sequence accessions (skip first line)
echo "> Running download script..."
{
  read
    while IFS=$'\t' read -r accession country collection_date host strain isolate
    do
      curl "https://www.ebi.ac.uk/ena/browser/api/fasta/${accession}?download=true" --output seq/${accession}.fasta
    done
} < ${METADATA_FILE}
echo "> Running download script... [DONE]"

echo "> Combining all sequences to a single fasta file..."
cat seq/* > insdc_sequences.fasta
echo "> Combining all sequences to a single fasta file... [DONE]"