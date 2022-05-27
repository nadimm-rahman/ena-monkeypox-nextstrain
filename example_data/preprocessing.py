#!/usr/bin/env python

import re
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


sequence_meta = pd.read_csv('ena_metadata_results.tsv', sep="\t")           # Download the metadata first - NOTE: Upcoming change to automatically read metadata
sequence_file = 'ena_sequence.fasta'          # Download the fasta sequences first - NOTE: Upcoming change to automatically download fasta sequences
format = 'fasta'

records = []
# Read each record from the fasta file
for record in SeqIO.parse(sequence_file, format):
    result = re.search('\|(.*)\|', record.id)
    id = result.group(1)            # Obtain only the sequence ID to cross-check with metadata
    seq = record.seq            # Sequence

    # Sequence headers require alteration, specifically injection of metadata fields
    print('*' * 50)
    print(id)
    print('*' * 50)
    accession_info = sequence_meta.loc[sequence_meta['accession'] == id]
    country = accession_info.iloc[0]['country']
    collection_date = accession_info.iloc[0]['collection_date']
    host = accession_info.iloc[0]['host']

    # Obtain an appropriate value for strain
    if accession_info['strain'].isnull().values.any():
        if accession_info['isolate'].isnull().values.any():
            strain = id         # If no strain or isolate, use the accession ID
        else:
            strain = accession_info.iloc[0]['isolate']          # Try isolate column second
    else:
        strain = accession_info.iloc[0]['strain']           # Try strain column first

    # Create the record to store fasta
    new_record = SeqRecord(
        Seq(seq),
        id=str(strain) + "|" + str(id) + "|" + str(collection_date) + "|" + str(country) + "|" + str(host)
    )
    records.append(new_record)
SeqIO.write(records, "example.fasta", "fasta")      # Write all sequence records to a fasta file, ready for augur command