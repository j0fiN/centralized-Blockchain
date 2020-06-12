"""
@author: JOFIN F ARCHBALD
@version: 1.0
"""
import time
import json
from hashlib import sha256


class Block:

    def __init__(self, index, transaction, timestamp, previous_hash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = None
        self.nonce = None

    def compute_hash(self):
        js = json.dumps(self.__dict__)
        return sha256(js.encode()).hexdigest()


class Blockchain:
    difficulty = 0

    def __init__(self):
        self.chain = list()
        self.unconfirmed_transactions = list()
        self.create_genesis_block()

    def create_genesis_block(self):
        block = Block(index=0,
                      transaction=[],
                      timestamp=time.time(),
                      previous_hash=0)
        block.hash = block.compute_hash()
        self.chain.append(block)

    @property
    def get_last_block(self):
        return self.chain[-1]

    @staticmethod
    def proof_of_work(block):
        block.nonce = 0
        h = block.compute_hash()
        while not h.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
        return h

    def add_block(self, block, proof):
        last_hash = self.get_last_block.hash
        if block.previous_hash != last_hash:
            return False
        if not self.validate_proof(block=block, proof=proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    @staticmethod
    def validate_proof(block, proof):
        return (proof.startswith('0' * Blockchain.difficulty) and
                proof == block.compute_hash())

    def add_new_transactions(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False
        last = self.get_last_block
        block = Block(index=last.index + 1,
                      transaction=self.unconfirmed_transactions,
                      timestamp=time.time(),
                      previous_hash=last.hash)
        proof = self.proof_of_work(block)
        self.add_block(block, proof)
        self.unconfirmed_transactions = []
        return block.index

    def __repr__(self):
        for i, block in enumerate(self.chain):
            if i == 0:
                print('GEN BLOCK')
            else:
                print(f'BLOCK {i + 1}')
        return ""
