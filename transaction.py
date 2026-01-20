class Transaction:
    def __init__(self,send,rec,amt):
        self.sender=send
        self.receiver=rec
        self.amount=amt
    def __repr__(self):
        return "{"+f"Sender: {self.sender}, Receiver:{self.receiver}, Amount:{self.amount}" + "}"