import sys
import getopt
import os
import pandas as pd

'''
to simulate macrohap allele for one individual 
Version: Mar - 18 - 2024
Author: Xuewen Wang
Email: xwang.kib @ gmail.com
'''
__author__="Xuewen Wang"

#parse arguments
xapp=os.path.basename(__file__)
def usage():
    version="1.0.0"
    print(f"Usage: python {xapp} [options]")
    print(f"e.g., python {xapp} -i MHtest2000.txt -m 1 -o MH_inSilicoMan")
    print("Options:")
    print("\t-h, --help: show this help message and exit")
    inputInfo="\n\t\t#database format (tab separated):" \
              "\n\t\tCSF1PO	EAS	C,C,T,G,C,A,G;;ATCTATCTATCTATCTATCTATCTATCTATCTATCTATCT	29	T=A=S" \
              "\n\t\tCSF1PO	EAS	C,C,T,G,C,A,G;;ATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCT	28	T=A=S"
    print("\t-i, --input: a required file of macrohap database" +inputInfo)
    print("\t-m, --mix: integer >=1, the number of individuals in simulated DNA evidenced mixture, default 1")
    outputInfo="\n\t\t#suspect format (tab separated):" \
               "\n\t\tTH01	C,C,T,T,G,T,C,G,G,G,C,C;G;AATGAATGAATGAATGAATGAATGAATG	1" \
               "\n\t\tTH01	C,T,C,T,G,T,G,G,G,G,A,C;G;AATGAATGAATGAATGAATGAATG	1" \
               "\n\t\tTPOX	C,G,A,T,G,C,C,G,C,G,A,C,C,C,G,G,A,G;G;AATGAATGAATGAATGAATGAATGAATGAATG	2" \
               "\n\t\t#Evidence format: similar to suspect format but no the 3rd column"
    print("\t-o, --out, prefix of file name. Results are the tab delimited allele data in evidence and suspect format."+outputInfo)
    print(f"Version: {version}, Mar,18th,2024")
    print("Support: xwang.kib@gmail.com")


def xpar(argv):
    nmix=1 #default to one person
    hapLibrary = "MHtest2000.txt"
    try:
        opts, args = getopt.getopt(argv, "hi:m:o:", ["--help","input", "mix","out"])
    except getopt.GetoptError:
        #print(err)
        usage()
        exit(2)

    if not opts:
        # Print the usage message and exit
        print("Oops: No options provided")
        usage()
        sys.exit(0)

    for opt, valx in opts:
        if opt == '-h':
            usage()
            sys.exit(0)
        elif opt in ("-i", "--input"):
            hapLibrary = valx
        elif opt in ("-m", "--mix"):
            nmix = valx
        elif opt in ("-o", "--out"):
            outMHfile = valx

    print("Input libray file is:\t" + hapLibrary)
    print("Number of simulated DNA contributors:\t", nmix)
    print("prefix of Output files:\t", outMHfile)
    print("")
    return hapLibrary,nmix,outMHfile

if __name__=='__main__':

    # Step 0: parse pars
    hapLibrary="MHtest2000.txt" # Replace with the actual file path
    nmix=1
    outfilePrefix= "MH_inSilicoMan" #prefix of outfiles
    hapLibrary,nmix,outEvidencefile= xpar(sys.argv[1:])

    OutMhEviden=open(outfilePrefix+"MH.tsv","wt")
    OutMhsuspect = open(outfilePrefix+".MHs.tsv", "wt")


    # Step 1: Read the input file into a DataFrame
    df = pd.read_csv(hapLibrary, sep="\t", header=None)

    # Step 2: Sort the DataFrame by the 1st column and then the 4th column
    df.columns = ['ColumnA', 'ColumnB', 'ColumnC', 'ColumnD','ColumnE']
    df.sort_values(by=["ColumnA",  "ColumnD"], ascending=[True, False], inplace=True)

    # Step 3: Calculate the total sum of the 4th column for each unique value in the 1st column
    freq_dict = {}
    for group, data in df.groupby("ColumnA"):
        freq_dict[group] = data["ColumnD"].sum()

    # Step 4: Calculate line frequency for each line: store in new column LineFrequency
    df["LineFrequency"] = df.apply(lambda row: row["ColumnD"] / freq_dict[row["ColumnA"]], axis=1)

    # Step 5: Randomly select lines based on line-frequency
    selected_lines = []
    numbOfAlleles=nmix*2  # the number of alleles for nmix person
    for group, data in df.groupby("ColumnA"):
        #select two rows n=2, based on line weight
        selected_line = data.sample(weights=data["LineFrequency"], n=numbOfAlleles)
        selected_lines.append(selected_line)
        #stored the dataframe with n=2 rows into the list

    #get MH in selected_lines:
    print(f"This is in silico Macrohap alleles maker")
    MHdict={}
    for line_group in selected_lines:
        for index, row in line_group.iterrows():
            #report the in silico MH alleles
            #print(f"{row['ColumnA']}\t{row['ColumnB']}\t{row['ColumnC']}\t{row['ColumnD']} ")
            # CSF1PO    EUR C, C, T, G, C, A, G;;ATCTATCTATCTATCTATCTATCTATCTATCTATCTATCT   9
            # CSF1PO    EUR C, C, T, G, C, A, G;;ATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCT   18

            ############# great moments: results
            #output similuated MH in vidence format, just need: name and allele_seq
            # output the locus name and MH allele, note that the MH may be the same if homologous, to filter duplicate for make mixture
            locus=row['ColumnA']
            MhAllele=row['ColumnC']
            MHoutInfo=locus+"\t"+MhAllele
            #print(f"{MHoutInfo}")
            OutMhEviden.write(MHoutInfo+"\n")
            # TH01	C,C,T,T,G,T,C,G,G,G,C,C;G;AATGAATGAATGAATGAATGAATGAATG
            # TH01	C,T,C,T,G,T,G,G,G,G,A,C;G;AATGAATGAATGAATGAATGAATG
            # TPOX	C,G,A,T,G,C,C,G,C,G,A,C,C,C,G,G,A,G;G;AATGAATGAATGAATGAATGAATGAATGAATG

            # prepare suspect allele format just need: name, allele_seq, count=1 or 2 for each individual
            #format: OutMhEviden
            count=1
            MhlocusAndAllele = locus + "\t" + MhAllele
            if MhlocusAndAllele in MHdict:
                #update count:  A,C,C,C,C,C,G,T;;ATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCT 1
                count=MHdict[MhlocusAndAllele]+1
            MHdict[MhlocusAndAllele]=count

    ############# great moments: results
    #output the suspect MH alleles
    for sl in MHdict:
        MHoutInfoSuspect=sl+"\t"+str(MHdict[sl])
        #print(f"{MHoutInfoSuspect}")
        OutMhsuspect.write(MHoutInfoSuspect+"\n")
        #TH01	C,C,T,T,G,T,C,G,G,G,C,C;G;AATGAATGAATGAATGAATGAATGAATG	1
        #TH01	C,T,C,T,G,T,G,G,G,G,A,C;G;AATGAATGAATGAATGAATGAATG	1
        #TPOX	C,G,A,T,G,C,C,G,C,G,A,C,C,C,G,G,A,G;G;AATGAATGAATGAATGAATGAATGAATGAATG	2


    OutMhEviden.close()
    OutMhsuspect.close()

    print("Results: \nMH allele in evidence format:\t"+ outfilePrefix+".MH.tsv")
    print("MH allele in suspect format:\t" +outfilePrefix+".MHs.tsv")
    print("Done")