from Bio import Entrez
import random


def main():
    Entrez.email = "lexbosch@live.nl"  # Always tell NCBI who you are
    random_amount_of_data = list(set([str(random.randrange(12000000, 32000000)) for x in range(0, 100000)]))
    handle = Entrez.efetch(db="pubmed", id=random_amount_of_data, rettype="medline", retmode="xml")
    reed_data = Entrez.read(handle)

    new_file = open("bestandsnaam.txt", "w")
    lelijke_counter = 0

    for paper in reed_data["PubmedArticle"]:
        try:
            maybe_abstract = (paper["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][0])
            if maybe_abstract:
                if not ">" in maybe_abstract:
                    new_file.write(maybe_abstract + "\n")
        except Exception:
            lelijke_counter -= -1
            print(lelijke_counter)
    new_file.close()

main()
