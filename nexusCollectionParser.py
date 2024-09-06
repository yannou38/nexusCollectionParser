import json
from pathlib import Path
import sys
import jmespath   

class NexusCollectionParser():    

    def __init__(self, filePath) -> None:
        with open(Path(filePath).absolute(), 'r') as file:
            self.json_data = json.load(file) 

    def getModsDownloadLinks(self) -> str:
        """
        Get mods download links of collection
        """
        #get name of game from collection
        domainName = jmespath.search("info.domainName", self.json_data)
        #get mod id and file id
        IdLists = jmespath.search("mods[*].source.[modId, fileId]", self.json_data)
        #tranqform previous list to links to mods
        links = '\n'.join('https://www.nexusmods.com/{}/mods/{}?tab=files&file_id={}'.format(domainName, IDs[0], IDs[1]) for IDs in IdLists)
        return links

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Missing path to file")
        exit()

    print("Hello! Trying to process the collection")
    #get download links
    links = NexusCollectionParser(sys.argv[1]).getModsDownloadLinks()
    with open("Output.txt", "w") as output:
        output.write(links)
    print("Done ! check Output.txt")
