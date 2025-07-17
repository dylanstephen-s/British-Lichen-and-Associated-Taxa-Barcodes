# British-Lichen-and-Associated-Taxa-Barcodes

This reference database provides barcodes for the mtSSU, ITS, 18S and 28S for British Lichens and Associated Taxa (Lichenicolous, non-lichenized taxa, and chemical races). This data is compiled from multiple reference databases (UNITE, GenBank, BOLD, GlobalFungi, and Martin7) in CSV format to be used directly in R or converted to FASTA files for command line scripting. Data was geographically limited to only include specimens collected from within Europe. The associated paper is located at the following link.


![Appendix Figure Pipeline](https://github.com/user-attachments/assets/5b30e0df-1f04-44f3-9ea8-605b7cf1374b)

Pipeline from data retrieval to coalescing and species name changing if necessary. Each color of the arrows to databases indicates method of retrieval, red indicates programmatic access, purple is webscraping, and yellow is through UI interface. After European filter, species name changes are indicated by the following numbers: 1) a single historic name changes to a single new name, which would mean a replacement of the older name, 2) one historic name found in the database has split and become two or more new names, it is unreliable to assign to one of these new names, so this record is removed, 3) A historic name has split resulting in the retention of the historic name, but also a new name as well as the species that was once classified under the historic name; in this case, the species will retain the historic name in the split. 4) Multiple species lump into a new currently/historically accepted name


File Descriptions:
Input Data:
BLS species counts by VC Sept 2024.xlsx - British Lichen Society Surveys by vice-county (VC) completed by September 2024. 
SUPERDICT_28-08-2023(superdict).csv - Conservation evaluations for each taxa from Woods & Coppins, 2012.
taxonomy_british_lichen_final.csv - Taxonomy of British lichen, collated from multiple databases (GBIF, ITIS, COL and Consortium of Lichen Herbaria Taxonomy Explorer)

Priority Lists:
conservation_priority_list.csv - taxa to prioritize for sequencing due to conservation concern.
family_priority_list.csv - taxa to prioritize for sequencing due to their correspondent family lacking previous sequence data for British lichens.
most_abundant_priority_list.csv - taxa to prioritize for sequencing due to their high frequency of capture on BLS surveys. 
lichen_species_missing_markers.csv - all LAT that are missing sequences for each barcode, count of how many sequences there are for each barcode.

Sequence Data (metadata and sequence data stored in one csv for each barcode):
mtssu_seq_meta.csv
nuclsu_seq_meta.csv
nucssu_seq_meta.csv
its_seq_meta.csv - Full ITS region

Scripts:
global_fungi_downloader.py - Python script to webscrape sequence data from the GlobalFungi database.

