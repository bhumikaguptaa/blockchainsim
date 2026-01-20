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

state = {} #the ledger
users = int(input("How many users are there?: "))
usernames = input("List the names in a comma separated manner:")
namelist = usernames.split(",")
if users != len(namelist):
    print("username count doesnt match provided usernames")
    exit(0)

print("Default starting amount is $100")
for name in namelist:
    state[name] = 100
print(state)

blockchain=[]
prevhash=0
for i in range(10): # This loop determines the number of blocks
    
    blockn_transaction=[]

    for i in range(10):#This loop is num transactions
        
        sender = input("Enter name of sender: ")
        receiver=input("Enter Receiver name: ")
        amount = int(input("Enter amount: "))
        newtrans = Transaction(sender,receiver,amount)
        print(f"Sender: {newtrans.sender}")
        blockn_transaction.append(newtrans)
        for t in blockn_transaction:
            state = process_transaction(t,state)
        c=input("Do u want more trans? (Y,n)")
        if not (c=='y' or c=='Y'):
            break
    blockn = {"transactions":blockn_transaction, "previous_hash":prevhash, "nonce":0}
    prevhash=mine_block(blockn)
    blockchain.append(blockn)
    c=input("Do you want more blocks?: (Y,n) ")
    if not (c=='y' or c=='Y'):
            break



print("Final Blockchain:")
count=1
for block in blockchain:
    print("Block number",count)
    count+=1
    trans=block["transactions"]
    print("Transactions:")
    for t in trans:
        print(t)
    print(f"prev_nonce: {block["previous_hash"]}")
    print(f"Current nonce: {block['nonce']}")
    print("="*20)

print("Final State:", state)
