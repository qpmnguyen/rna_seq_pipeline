import os 
code = os.system("prefetch --version")

if code != 0:
    print("sra-tools need to be installed")
    exit()

text = open("accession_SRP033351.txt", "r")
for line in text.readlines():
    accession = line.strip()
    os.system("prefetch " + accession)
    os.system("fasterq-dump " + accession + " --outdir raw_data/")

text.close()


