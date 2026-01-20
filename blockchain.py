##the security -- mining
#the hash
import hashlib
import json
from transaction import Transaction
#message = "Hello world!"
#hash_object = hashlib.sha256(message.encode())
#print(hash_object.hexdigest())
#transaction
##three important things in a transation - sender, recipient, amount
#transaction_string = json.dumps(transaction, sort_keys= True)                         
#hash_object = hashlib.sha256(transaction_string.encode())
#print(hash_object.hexdigest())
#the block
#block2json = json.dumps(block2, sort_keys=True)
#block2json_object = hashlib.sha256(block2json.encode())

# #proof of work
def mine_block(block):
    blockjson = json.dumps(block, default=lambda o: o.__dict__, sort_keys=True)
    blockjson_object = hashlib.sha256(blockjson.encode())
    while blockjson_object.hexdigest()[0:4] != "0000":
        block["nonce"] +=  1
        blockjson = json.dumps(block, default=lambda o: o.__dict__, sort_keys=True)
        blockjson_object = hashlib.sha256(blockjson.encode())
    return block["nonce"]


##logic -- acount balance state
def is_valid(transaction: Transaction, state):
    if transaction.sender not in state or transaction.receiver not in state:
        return False
    if state[transaction.sender] < transaction.amount:
        return False
    return True

def process_transaction(transaction: Transaction, state):
    if is_valid(transaction, state) == True:
        state[transaction.sender] = state[transaction.sender] - transaction.amount 
        state[transaction.receiver] = state[transaction.receiver] + transaction.amount

    return state


state = {"Alice": 50, "Bob":50, "Charlie":50} #the ledger
# block1_transaction = {"Sender":"Alice", "Recipient":"Bob", "Amount":5}
block1_transaction=[]

for i in range(10):
    
    sender = input("Enter name of sender: ")
    receiver=input("Enter Receiver name: ")
    amount = int(input("Enter amount: "))
    newtrans = Transaction(sender,receiver,amount)
    print(f"Sender: {newtrans.sender}")
    block1_transaction.append(newtrans)
    for t in block1_transaction:
        state = process_transaction(t,state)
    c=input("Do u want more trans? (Y,n)")
    if not (c=='y' or c=='Y'):
        break


block2_transaction = []
for i in range(10):
    sender = input("Enter name of sender: ")
    receiver=input("Enter Receiver name: ")
    amount = int(input("Enter amount: "))
    newtrans = Transaction(sender,receiver,amount)
    print(f"Sender: {newtrans.sender}")
    block2_transaction.append(newtrans)
    for t in block2_transaction:
        state = process_transaction(t,state)
    c=input("Do u want more trans? (Y,n)")
    if not (c=='y' or c=='Y'):
        break


block = {"transactions": block1_transaction, "previous_hash": "0", "nonce": 0}
prevhash = mine_block(block)
block2 = {"transactions": block2_transaction, "previous_hash": prevhash, "nonce": 0}
mine_block(block2)

blockchain = [block]
blockchain.append(block2)

print("Final Blockchain:", blockchain)
print("Final State:", state)
