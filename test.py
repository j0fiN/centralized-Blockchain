"""
@author: JOFIN F ARCHBALD
@version: 1.0
"""
from flask import *
from BlockChain import Blockchain
import time

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/')
def home():
    return f"""<h3>Welcome to a Blockchain Network<h3>
                <a href={url_for('blockchain_display')}>Print Blockchain</a>
            """


@app.route("/bc/mine", methods=["POST"])
def mine_a_transaction():
    tran = request.get_json()
    if not tran["author"] or not tran["content"]:
        return "Invalid transaction", 400
    tran["timestamp"] = time.time()
    blockchain.unconfirmed_transactions.append(tran)
    blockchain.mine()
    return jsonify(tran), 200


@app.route("/bc", methods=["GET"])
def blockchain_display():
    chain = list()
    for block in blockchain.chain:
        chain.append(block.__dict__)
    result = dict()
    result['chain_length'] = len(chain)
    result['chain'] = chain
    return f"""<h3>{result}<h3>
        <a href={url_for('home')}>Home</a>
"""


if __name__ == "__main__":
    app.run(debug=True)
