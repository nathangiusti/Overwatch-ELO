This project serves two purposes:

1. To direct development of PowerPy
2. I think it's fun to do combine math and sports

OWParser.py reads in a copy paste of the match results and posts them to a google sheet. 

ELO Calculator.py reads the google sheet with match results and does ELO calculations. 

These pages are read by OWL ELO.pbix

For export to PDF, DuplicateAndSetSlicer.py duplicates the team pages while updating the slicer in order to programatically create all additional tabs.
The output to this process can be seen in OW ELO.pdf