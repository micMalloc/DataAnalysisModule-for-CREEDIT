

class trun():
    def __init__(self):
        pass
    def trunStatistics(self,s):
       s.execute('''TRUNCATE TABLE statistics''')
       s.commit()
