# nexusCollectionParser
Simple python script to generate a list of download links from a nexus collection json file


# Usage
Start by [installing python](https://www.python.org/downloads/). 

Then clone the repository, or download the source as zip and extract it somewhere

Then open a script where you downloaded the source code and type
```powershell
python -m pip install -r requirements.txt
```
Then execute the script:
```
python ./nexusCollectionParser.py ./collection.json
```
The script will generate a list of links in Output.txt


#How to get the collection.json file of the colelction
TODO. I had to add the collection to nexus, then navigate to C:\Users\MYUSER\AppData\Roaming\Vortex\GAME\mods and find the name of the collection among the folder to retrieve the file, which is not super efficient. I'll search for an easier way later.