# nextstrain.org/monkeypox

This is the [Nextstrain](https://nextstrain.org) build for monkeypox virus. Output from this build is visible at [nextstrain.org/monkeypox](https://nextstrain.org/monkeypox).

## Usage

Before running this, data preparation is required. See 'Input data' below.

Copy input data with:
```
mkdir -p data/
cp -v example_data/* data/
```
Add any additional sequences and metadata in separate fasta or metadata-tsv files to `data`, respectively.

Run pipeline with:
```
nextstrain build --docker --image=nextstrain/base:branch-nextalign-v2 --cpus 1 .
```

Adjust the number of CPUs to what your machine has available you want to perform alignment and tree building a bit faster.

View results with:
```
nextstrain view auspice/
```

## Configuration

Configuration takes place in `config/config.yml` by default.
The analysis pipeline is contained in `workflow/snakemake_rule/core.smk`.
This can be read top-to-bottom, each rule specifies its file inputs and output and pulls its parameters from `config`.
There is little redirection and each rule should be able to be reasoned with on its own.

## Input data

### GenBank data

Run `python preprocessing.py`
- This script downloads appropriate metadata and fasta sequence.
- Processes the metadata and fasta sequence in preparation for the `augur parse` command below.

Note: Metadata is downloaded/prepped in this order:
1. Strain name
2. GenBank accession
3. Country
4. Date
5. Host

This prepares the file `insdc_cleaned_sequence.fasta`. Parse this file into sequences and metadata using:
```
augur parse \
 --sequences data/insdc_cleaned_sequence.fasta \
 --fields strain accession date country host \
 --output-sequences example_data/sequences.fasta \
 --output-metadata example_data/metadata.tsv
```
Now you are ready to follow instructions in 'Usage'.

### Data use

We gratefully acknowledge the authors, originating and submitting laboratories of the genetic
sequences and metadata for sharing their work. Please note that although data generators have
generously shared data in an open fashion, that does not mean there should be free license to
publish on this data. Data generators should be cited where possible and collaborations should be
sought in some circumstances. Please try to avoid scooping someone else's work. Reach out if
uncertain.

## Installation

Follow the [standard installation instructions](https://docs.nextstrain.org/en/latest/install.html) for Nextstrain's suite of software tools.
Please choose the installation method for your operating system which uses Docker, as currently a pre-release version of Nextalign is required which we've baked into the `--image` argument to `nextstrain build` above.

## Requirements

- Python 3+ (https://www.python.org/downloads/)
- Nextstrain (https://docs.nextstrain.org/en/latest/install.html)
- Install packages using `pip install -r requirements.txt`
