##the security -- mining
#the hash
import hashlib
import json
#message = "Hello Gemini!"
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
    blockjson = json.dumps(block, sort_keys=True)
    blockjson_object = hashlib.sha256(blockjson.encode())
    while blockjson_object.hexdigest()[0:4] != "0000":
        block["nonce"] +=  1
        blockjson = json.dumps(block, sort_keys=True)
        blockjson_object = hashlib.sha256(blockjson.encode())
    return block["nonce"]


##logic -- acount balance state
def is_valid(transaction, state):
    if transaction['Sender'] not in state or transaction['Recipient'] not in state:
        return False
    if state[transaction['Sender']] < transaction['Amount']:
        return False
    return True

def process_transaction(transaction, state):
    if is_valid(transaction, state) == True:
        state[transaction["Sender"]] = state[transaction['Sender']] - transaction["Amount"] 
        state[transaction["Recipient"]] = state[transaction['Recipient']] + transaction["Amount"]

    return state


state = {"Alice": 50, "Bob":50} #the ledger
block1_transaction = {"Sender":"Alice", "Recipient":"Bob", "Amount":5}

block2_transactions = [{"Sender":"Bob", "Recipient":"Alice", "Amount":2}]
for transaction in block2_transactions:
    state = process_transaction(transaction, state)

block = {"transactions": [block1_transaction], "previous_hash": "0", "nonce": 0}
mine_block(block)
block2 = {"transactions": block2_transactions, "previous_hash": "0000c622041716a4d0e72d844e10a7021cb0bff7cca5daac90bcc6da1e5e01f1", "nonce": 0}
mine_block(block2)

blockchain = [block]
blockchain.append(block2)

print("Final Blockchain:", blockchain)
print("Final State:", state)
