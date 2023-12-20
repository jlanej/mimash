import os

import download_1000g

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cwd = os.getcwd()
    # set the data directory
    data_dir = os.path.join(cwd, 'data')

    # set the 1000G directory
    thousandG_dir = os.path.join(data_dir, '1000G')
    download_1000g.download_1000G_mito_vcf(thousandG_dir)
