# nextstrain.org/monkeypox

This is the [Nextstrain](https://nextstrain.org) build for monkeypox virus. Output from this build is visible at [nextstrain.org/monkeypox](https://nextstrain.org/monkeypox).

## Usage

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

From ENA Advanced Search, download appropriate metadata and fasta. Bare in mind retrieval of fields below, and ensure that the query includes country and collection date information by default.

Download Genome FASTA, select custom format, and choose the following fields in this order:
1. Strain name
2. GenBank accession
3. Country
4. Date
5. Host

This downloads the file `*.fasta`. Parse this file into sequences and metadata using:
```
augur parse \
 --sequences data/XXXXX.fasta \
 --fields strain accession date country host \
 --output-sequences data/sequences.fasta \
 --output-metadata data/metadata.tsv
```


### Outbreak data

- [Monkeypox/PT0001/2022](https://virological.org/t/first-draft-genome-sequence-of-monkeypox-virus-associated-with-the-suspected-multi-country-outbreak-may-2022-confirmed-case-in-portugal/799)
- [ITM_MPX_1_Belgium](https://virological.org/t/belgian-case-of-monkeypox-virus-linked-to-outbreak-in-portugal/801)
- [MPXV_USA_2022_MA001](https://www.ncbi.nlm.nih.gov/nuccore/ON563414)

has been saved to `example_data/outbreak.fasta`.

### Data preparation

**Option 1:**

Collect data as described above and store in one or more `data/*.fasta` and `data/*.tsv` file(s).

**Option 2:**

Move the provided metadata and sequences to `data/`:
```
cp example_data/metadata.tsv data/metadata.tsv
cat example_data/sequences.fasta example_data/outbreak.fasta > data/sequences.fasta
```

**Option 3:**

Download data using [LAPIS](https://mpox-lapis.gen-spectrum.org/docs)
```
snakemake --cores 1 -f download_via_lapis
```

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
