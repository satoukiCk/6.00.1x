class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        self.vals.append(e)
    def remove(self):
        try:
            e = self.vals[0]
            self.vals.remove(e)
            return e
        except:
            raise ValueError("ValueError")