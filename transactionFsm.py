from account import Account

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)
        
    def set_start(self, name):
        self.startState = name.upper()

    def run(self):
        account = Account()
        try:
            handler = self.handlers[self.startState]    
        except:
            raise Exception("must call .set_start() before .run()")
        if not self.endStates:
            raise  Exception("at least one state must be an end_state")
    
        while True:
            if  handler == self.handlers[self.startState]:
                cargo = input('Input your debit or credit transaction (ex = Debit:100) :')
            (newState, cargo, account) = handler(cargo, account)
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break 
            else:
                handler = self.handlers[newState.upper()]

