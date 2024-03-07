# MacroHapDBB
  $${\color{blue}MacroHapDB \space is \space The \space DataBase \space of \space Macrohap \space Alleles}$$

An Macrohap Allele consists of an alleic sequence at variant sites only of forensic CODIS STRs, SNPs and InDels. VarAlleleDB deposits alleles,cross-validated information and their frequency count in human populations. The current version includes two sets of humman samples, each with three databases at population, supperpopulation and global scale, from the 1000 genome project. The coordinate position is based on HG38.

Dataset I: 289 validated individuals; 11,560 alleles. 

Dataset II: 2504 unrelated individuals; 100,160 alleles. 

Both have 26 populations (FIN,CDX,IBS,MXL,CHB,CHS,CEU,JPT,ESN,KHV,TSI,CLM,YRI,GBR,PEL,STU,BEB,GIH,PJL,MSL,ITU,GWD,LWK,ASW,PUR,ACB), 5 supperpopulations (EAS, EUR, AFR,SAS, AMR).

# Installation
The VarAlleleDB can be directly run and viewed in any computer after downloading. No additional installation is required once an internet browser, e.g. Chrome, IE, Edge, firefox etc., is there. Users can use either method to install the database in a computer.

## Method 1: 
Download the files from github using the following command:

`git clone https://github.com/XuewenWangUGA/VarAlleleDB`

Double click the viewer `VarAlleleDB_viewer.html` in the downloaded folder to run the database.

## Method 2: 
Download the database compressed files from the github page and uncompress it. 

Then, double click the viewer `VarAlleleDB_viewer.html` in the downloaded folder to run the database.

# Usage

Step 1. choose a database file: .global, pop, superPop

Step 2. select a marker name from drop-down list

Step 3. the alleles for selected marker will be shown up in a Tab separated text.


# Meaning of the columns 
The displayed alleles for each marker will have five columns, e.g., 

    CSF1PO	EAS	C,C,T,G,C,A,G,C,C,G,A,T,T,C,G,T,A,C,T,T,T,G,C,T,A,G,A,C,C,G,C,C,G,G,G,G,C,T,C,G,G,G,G,G;T,T,G;ATCTATCTATCTATCTATCTATCTATCTATCTATCTATCT	136	T=A=S

Meaning of each column:
1. column 1 is the marker/locus name, e.g., CSF1PO
2. column 2 is the population name, e.g., EAS
3. column 3 is the variant allele. SNPs, InDels and STRs separated by ";"
4. column 4 is the frequency count of this allele in the given population EAS
5. column 5 is the validated consistency information.T=A=S represents a consistency between three mathods.

Each variant is separated by ",". The position of each variant is provided in our Github depository https://github.com/XuewenWangUGA/VarSeqStitcher/tree/main/testData .


# Example
Here is an example for load the supper-population database.

Step 1. open the database file "stitched.MH.allele_count.1KG2504.supPop.consisTag.txt"

Step 2. click to choose the marker "CSF1PO" or any other marker name from the drop-down list

the variant allele will be displayed for the selected marker as shown in Fig1.

 ![Displaying of CSF1PO variant alleles](DBdisaply.PNG) Fig1.


# Support

Contact: Xuewen.Wang at UNTHSC.edu, August.Woerner at UNTHSC.edu




