# VarAlleleDB
 VarAlleleDB is $${\color{blue}The \space DataBase \space \space of \space Variant \space Alleles}$$

A Variant Allele consists of an alleic sequence at variant sites only of forensic CODIS STRs, SNPs and InDels. VarAlleleDB deposits alleles,cross-validated information and their frequency count in human populations. The current version includes two sets of humman samples, each with three databases at population, supperpopulation and global scale, from the 1000 genome project.

Dataset I: 289 validated individuals; 11,560 alleles. 

Dataset II: 2504 individuals; 100,160 alleles. 

Both have 26 populations (FIN,CDX,IBS,MXL,CHB,CHS,CEU,JPT,ESN,KHV,TSI,CLM,YRI,GBR,PEL,STU,BEB,GIH,PJL,MSL,ITU,GWD,LWK,ASW,PUR,ACB), 5 supperpopulations (EAS, EUR, AFR,SAS, AMR).

# Installation
The VarAlleleDB can be directly run and viewed in any computer after downloading. No additional installation is required once an internet browser, e.g. Chrome, IE, Edge, firefox etc., is there. 
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

Contact: Xuewen.Wang at UNTHSC.edu, August.Woerner at UNTHSC.edu

# Example
Here is an example for load the supper-population database.

Step 1. open the database file "stitched.MH.allele_count.1KG2504.supPop.consisTag.txt"

Step 2. click to choose the marker "CSF1PO" or any other marker name from the drop-down list

the variant allele will be displayed for the selected marker as shown in Fig1.

 ![Displaying of CSF1PO variant alleles](DBdisaply.PNG) Fig1.





