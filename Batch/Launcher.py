from Job import *
import json
from queue import Queue


class Launcher:

    def __init__(self, PATH=None):
        if PATH is not None:
            self.metaData = self.loadMetaData(PATH)
            self.jobQue = self.makeJobQueue()
        else:
            self.metaData = None
        
        print(self.metaData)

    def loadMetaData(self, PATH):
        with open(PATH) as jsonFile:
            return json.load(jsonFile)
            
    def makeJobQueue(self):
        que = Queue()
        return que
    
    def getJob(self):
        pass

    def start(self):

        while True:
            if self.jobQue.empty():
                print("queue is empty")
                break

            job = self.jobQue.get(False)

            try:
                job.doJob()
            except Exception:
                # Send Mail to authorized users
                pass


if __name__ == "__main__":
    batch_laungcher = Launcher("/Users/heesu.lee/DataAnalysisModule-for-CREEDIT/Batch/meta.json")
    batch_laungcher.start()
    pass