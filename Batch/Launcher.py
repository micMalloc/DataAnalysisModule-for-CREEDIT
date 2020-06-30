from Job.Job import Job
import json

class Launcher:

    def __init__(self, PATH=None):
        if PATH is not None:
            self.metaData = self.loadMetaData(PATH)
            self.jobList = self.makeJobQueue()
        else:
            self.metaData = None
        
        print(self.metaData)

    def loadMetaData(self, PATH):
        with open(PATH) as jsonFile:
            return json.load(jsonFile)
            
    def makeJobQueue(self):
        pass
    
    def start(self):
        pass


if __name__ == "__main__":
    Launcher("/Users/heesu.lee/DataAnalysisModule-for-CREEDIT/Batch/meta.json")
    pass