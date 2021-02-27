# packard
 Packard's Morphological Analysis Codes module for the Sword engine.

 This is based on : http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/*Morph-Coding */


1) generate a list of morphcode:
./bin/extractCode.py /home/melmoth/dev/LXX/lxx.osis.xml > code.txt

2) if you want to get a list of invalid code:
./bin/findInvalidCode.py /home/melmoth/dev/LXX/lxx.osis.xml > invalid.txt

3) get description for all code:
./bin/allentry.py  code.txt > list.txt

