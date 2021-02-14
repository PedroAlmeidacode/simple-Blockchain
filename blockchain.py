# module 1 - Create a Blockchain


import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - building a blockchain

class Blockchain:
        
    # inicialize the blockchain
    def __init__(self):
        self.chain = []
        # creates the genesis block
        self.create_block(proof = 1, previous_hash = '0' )


    # used after minning a block and founded the proof
    # or in the first block creation
    def create_block(self, proof, previous_hash):
        
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 }
        
        # adds to the chain 
        self.chain.append(block)
        return block
    
    