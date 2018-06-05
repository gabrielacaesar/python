import pandas as pd
import numpy as np
import os
import urllib
import zipfile
import glob
import codecs

from tempfile import mkdtemp
TEMP_PATH = "./temp"

if not os.path.exists(TEMP_PATH):
    os.makedirs(TEMP_PATH)

FILENAME_PREFIX = 'filiados_{}_{}.zip'
TSE_PARTYMEMBERS_STATE_URL = 'http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/'
TODAY = pd.datetime.today().date()
OUTPUT_FILENAME = TODAY.isoformat() + '-tse-partymembers.xz'
OUTPUT_DATASET_PATH = os.path.join('data', OUTPUT_FILENAME)
# the array with parties has considered all mentioned on TSE's website until 21/07/2017
party_list = ["DEM", "NOVO", "PEN", "PC_DO_B", "PCB", "PCO", "PDT", "PHS", "PMDB", "PMB", "PMN", "PP",
              "PPL", "PPS", "PR", "PRB", "PROS", "PRP", "PRTB", "PSB", "PSC", "PSD", "PSDB", "PSDC", "PSL",
              "PSOL", "PSTU", "PT", "PT_DO_B", "PTB", "PTC", "PTN", "PV", "REDE", "SD"]
state_list = ["RS", "SC", "PR", "RJ", "SP", "ES", "MG", "GO", "DF", "TO", "MS", "MT", "AM", "AC",
              "RO", "RR", "PA", "AP", "MA", "AL", "PI", "RN", "PE", "CE", "SE", "BA", "PB"]

#party_list = ["DEM", "NOVO"]
#state_list = ["RS"]

# Download files
for party in party_list:
    for state in state_list:
        filename = FILENAME_PREFIX.format(party.lower(), state.lower())
        file_url = TSE_PARTYMEMBERS_STATE_URL + filename
        print(file_url)
        output_file = os.path.join(TEMP_PATH, filename)
        print(output_file)
        urllib.request.urlretrieve(file_url, output_file)

# Unzip downloaded files
for party in party_list:
    for state in state_list:
        filename = FILENAME_PREFIX.format(party.lower(), state.lower())
        file_path = os.path.join(TEMP_PATH, filename)
        print(file_path)
        zip_ref = zipfile.ZipFile(file_path, 'r')
        zip_ref.extractall(TEMP_PATH)
        zip_ref.close()

csv_pattern = os.path.join(TEMP_PATH, "aplic/sead/lista_filiados/uf/filiados_*.csv")
csv_files = glob.glob(csv_pattern)

f = codecs.open("./filiados2018.csv", "w", "iso8859-1")

f2 = codecs.open(csv_files[0], "r", "iso8859-1")
f.write(f2.readlines()[0])
f2.close()

for csv_path in csv_files:
	csv_file = codecs.open(csv_path, "r", "iso8859-1")
	data = csv_file.readlines()[1:]
	f.write("".join(data))
	csv_file.close()

f.close()

