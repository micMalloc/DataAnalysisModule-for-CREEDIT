import json
from queue import Queue
from Log.Logger import Logger
from Job.Job import JobFactory


class Launcher:

    def __init__(self, path=None):
        if path is not None:
            self.meta_data = self.load_meta_data(path)
            self.job_que = self.make_job_queue()
        else:
            self.meta_data = None
        
        self.logger = Logger.get_instance()
        print(self.meta_data)

    def load_meta_data(self, PATH):
        with open(PATH) as jsonFile:
            return json.load(jsonFile)
            
    def make_job_queue(self):
        que = Queue()
        que.put(JobFactory.create_job())

        return que
    
    def get_job(self):
        pass

    def start(self):

        while True:
            if self.job_que.empty():
                print("queue is empty")
                break

            job = self.job_que.get(False)

            try:
                job.do_job()
            except Exception:
                # TODO define do job exception for handling issue
                # TODO Logger may be used in this section
                # Send Mail to authorized users
                self.logger.error("Do Not Complete Job")
                self.logger.send_email()
                pass


if __name__ == "__main__":
    batch_laungcher = Launcher("/Users/heesu.lee/DataAnalysisModule-for-CREEDIT/Batch/meta.json")
    batch_laungcher.start()
    pass
