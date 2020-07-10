class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.operation = []
        self.step = []
        self.l_undo = []

    def add(self, num: int):
        self.value += num
        self.operation.append(['sum', num])
        self.step.append(['sum', num])
        return self.value

    def subtract(self, num: int):
        self.value -= num
        self.operation.append(['sub', num])
        self.step.append(['sub', num])
        return self.value

    def undo(self):
        if(len(self.step) == 0):
            return str(self.value)
        self.lastop = self.operation.pop()
        if (self.lastop[0] =='sum'):
            self.value -= self.lastop[1]
        else:
            self.value += self.lastop[1]
        self.l_undo.append('undo')
        return self.value

    def redo(self):
        if(len(self.step) == 0):
            return str(self.value)
        if (self.lastop[0] =='sum'):
            self.value += self.lastop[1]
        else:
            self.value -= self.lastop[1]
        self.l_undo.pop()
        return self.value

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()
        return self.value    

    def bulk_redo(self, steps: int):
        if(self.l_undo.count('undo') < steps):
            steps = self.l_undo.count('undo')
        
        for i in range(steps):
            self.redo()
        return self.value
