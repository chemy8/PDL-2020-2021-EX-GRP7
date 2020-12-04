# PDL-GRP7
# Wikipedia Matrix : The Truth
![Quick illustration of the project](img/readme.png) <br>

The aim of this PDL project is to extract tables in CSV format from Wikipedia pages. Those pages can be analyzed in two different ways:
By searching for the corresponding Wikitext code
By exploiting the HTML rendering of the Wikipedia page 

Both approaches would be compared and tested (in order to have the same CSV output).

### But why extract tables in Wikipedia?

Wikipedia tables are difficult to exploit by statistical tools, visualization or any tool able to exploit tables (e.g., Excel, OpenOffice, RStudio, Jupyter). These tables are written in a syntax (Wikitext) difficult to analyze and not necessarily designed for the specification of tables. In addition, there is a strong heterogeneity in the way tables are written, further complicating Wikipedia's tabular data processing. Same can be said for HTML format. 

### Why CSV (Comma separated values) ?
It is very simple and above all supported by many tools.

This project is about implementing a solution and specify a ground truth ("ground truth") and thus evaluate different extractors by confronting them to the ground truth. Also, it must be able to extract several tables on the same Wikipedia page.


Last but not least, this project will propose a set of tools able to analyze the results of the extractors and thus specify a set of expected results (which will then be used during the automatic test phase). Among these tools, one of them will allows to visualize a matrix (resulting from an automatic extractor), possibly to correct the matrix, and then to export it in CSV format.

Finally, a most global suite of tests will demonstrate the quality of our tool.

### Final result
There will be three concrete results:
Extractors of much better quality (with source code, documentation, test suite, continuous integration, etc.)
A suite of tools to be able to more easily specify a ground truth and thus help the evaluation of extractors
A dataset reusable by anyone wanting to test an array extractor

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See "Parsing wikitables" to start the parsing on a live system.

After cloning the project into your computer, either you open it on your IDE 

### Prerequisites

An IDE .

```
Pycharm - https://www.jetbrains.com/fr-fr/pycharm/
```


### Installing

How to install it ?


You can find more details in [INSTALL.md](https://github.com/chemy8/PDL-2020-2021-EX-GRP7/blob/main/INSTALL.md).

 ## How to run project?
In this project you have two parts:
the extractor python , his run is explain in install.md
and the comparator of extractor 
 ## Fonctionement and run of comparator_interface.py
![Project architecture](img/Inkedcomp2_LI.jpg)

-fonctionement of comparator_interface.py
It is a web interface to compare csv files from 3 extractors (java:html and wikitext and python:html) obtained from URL Wikipedia
there are 7 parts on this interface:
1) URL WIKIPEDIA: you have to enter the Url to be extracted
2) CHOOSING AN EXTRACTOR: you have to choose from a drop-down list one of the 3 extractors you want to use
3)DATA TABLE:
in order to make it easier for the user to understand the CSV file is displayed in the form of an editable table.
4) RECORD CHANGES
here after modifying your table you can save the changes in the CSV file.
5) VISUALIZE THE DIFFERENCE
you will be able to see the major differences between the 3 extractors 
6)CHOICE OF THE CSV TO BE DISPLAYED IN THE TABLE
in case you have several tables, the first table is displayed by default and you can choose here the CSV of the table you want to display
7) SAFE OF GROUND TRUTH
in this part you can save your modified CSV in the folder correctCSV 


-run of comparator_interface.py
For run this part 

## Folders' structure

Folders:
- the root contains some files, as :
  
  1. INSTALL.md containing the install guide
  2. DESIGN.md cointaining projects' scope and its UML Model.
  3. README.md containing utils informations about project.
.
  

- the /src folder contains four folders :
  1. Donnee.py containing the implementation class of our extractor.
  2. Url containing url for test.
  3. wikiExtractMain is main class.
  4.Comparator_interface.py the comparator interface

## Running the tests


## Parsing wikitables

For extracting from both HTML  you need to go:

On PyCharm : Double click on the green play button on your right for run wikiExtractMain.py .

Put Url you want extract.
```

```
## Supported and unsupported features (actual state)



##Future function


## Built With

* [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/) - The IDE used
git config --global user.email johndoe@example.com

## Authors

* **Lassana MAKADJI** - *Whole project* - [Lassana_Makadji](https://github.com/makadjilassana)
* **Rahima KONE** - *Whole project* - [Rahima_Koné](https://github.com/chemy8)
* **Mariem ROUISSI** - *Whole project* - [Mariem_Rouissi](https://github.com/Mrouissi)
* **Rebecca EHUA** - *Whole project* - [Rebecca_Ehua](https://github.com/CodeusedeReve)

##Project Context

This module takes place at the University of Rennes 1, ISTIC, in Master 1 (MIAGE). 
The objective of PDL is to carry out a software project with open technologies and data. 
There are many challenges to overcome, requiring skills in project management, modeling, and programming.
This scenario should make it possible to better understand and apprehend the difficulty of developing software in an extremely concrete context. 
Software development technics and tools (git, github, etc.) well known to the industry will be used. 
Technological choices will also have to be made.

## License

This project haven't licence.

