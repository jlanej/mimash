import os
import urllib.request
from pathlib import Path


# Download mitochondrial genome vcf from the 1000 Genomes Project
# using the 1000 Genomes FTP site at http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chrMT.phase3_callmom-v0_4.20130502.genotypes.vcf.gz
# and the corresponding index file at http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chrMT.phase3_callmom-v0_4.20130502.genotypes.vcf.gz.tbi
# and saves them to the data/1000G directory
# if the files already exist, it does not download them again
# returns the path to the vcf file


def download_1000G_mito_vcf(root_dir):
    # create the 1000G directory if it does not exist
    Path(root_dir).mkdir(parents=True, exist_ok=True)

    vcf_file = os.path.join(root_dir, 'ALL.chrMT.phase3_callmom-v0_4.20130502.genotypes.vcf.gz')
    index_file = os.path.join(root_dir, 'ALL.chrMT.phase3_callmom-v0_4.20130502.genotypes.vcf.gz.tbi')
    filesToDownload = [vcf_file, index_file]

    # download the vcf and index files if they do not exist
    for file in filesToDownload:
        if not os.path.exists(file):
            print('Downloading ' + file)
            urllib.request.urlretrieve(
                'http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/' + os.path.basename(file), file)
        else:
            print('File ' + file + ' already exists')
