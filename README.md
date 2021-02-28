# packard
 Packard's Morphological Analysis Codes module for the Sword engine.

 This is based on : http://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxmorph/*Morph-Coding */


https://wiki.crosswire.org/TEI_Dictionaries
```
1) generate a list of morphcode from the LXX's osis file.
./bin/extractCode.py /home/melmoth/dev/LXX/lxx.osis.xml > code.txt

2) if you want to get a list of invalid code and the verse they occurs in:
./bin/findInvalidCode.py /home/melmoth/dev/LXX/lxx.osis.xml > invalid.txt

3) build  the xml:
./bin/buildTei.py code.txt  > packard.tei.xml

4) validate the xml
 wget http://www.crosswire.org/OSIS/teiP5osis.2.5.0.xsd
 xmllint --noout --schema teiP5osis.2.5.0.xsd  packard.tei.xml

5) build the module:
rm -rf packard 
mkdir packard 
/usr/local/sword/bin/tei2mod  packard packard.tei.xml -z 

```
