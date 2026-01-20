# Blockchain Testnet

An implementation of a blockchain in Python. This project demonstrates core blockchain concepts including a ledger (state), transaction validation, block creation, and Proof of Work (mining) using SHA-256 hashing. The project plans to allow users to connect to this service over the internet and engage in transactions.

## Features

* **Transaction Validation:** Checks if the sender has enough funds and if both users exist before processing a transaction.
* **JSON Serialization:** Converts custom Python objects into JSON strings for hashing.
* **Proof of Work (Mining):** Implements a difficulty target (finding a hash starting with `0000`) using a nonce.
* **Interactive CLI:** Allows dynamic input of users, transactions, and blocks.
* **Online Decentralized Access**: Allows users to engage with this service over the internet


### File Structure
This project requires two files in the same folder. 

1. **`blockhain.py`**: The code containing the mining and blockchain logic (the code you provided).
2. **`transaction.py`**: A file containing the Transaction class.
