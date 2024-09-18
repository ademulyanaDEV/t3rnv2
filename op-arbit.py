from web3 import Web3
from eth_account import Account
import time
import sys
import config

# Detail jaringan
private_key = config.private_key_metamask.strip() 
rpc_url = 'https://sepolia.optimism.io'  # JANGAN DIGANTI
chain_id = 11155420  # JANGAN DIGANTI
contract_address = '0xF221750e52aA080835d2957F2Eed0d5d7dDD8C38'  # JANGAN DIGANTI
my_address = config.alamat_dompet

# Koneksi ke jaringan
web3 = Web3(Web3.HTTPProvider(rpc_url))
if not web3.is_connected():
    raise Exception("Tidak dapat terhubung ke jaringan")

# Buat akun dari private key
account = Account.from_key(private_key)

# Data transaksi untuk bridge (Jangan Diganti)
data = '0x56591d596172627400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000071592a0fb4cbce6c0e1574a225f25f1fad9c2cc200000000000000000000000000000000000000000000000001633e3f03ce5b0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016345785d8a0000'

# Fungsi untuk membuat dan mengirim transaksi
def send_bridge_transaction():
    # Ambil nonce untuk alamat pengirim
    nonce = web3.eth.get_transaction_count(my_address)

    # Estimasi gas
    try:
        gas_estimate = web3.eth.estimate_gas({
            'to': contract_address,
            'from': my_address,
            'data': data,
            'value': web3.to_wei(0.1, 'ether')  # Mengirim 0.01 ETH
        })
        gas_limit = gas_estimate + 20000  # Tambahkan buffer gas
    except Exception as e: 
        print(f"Error estimating gas: {e}")
        return None

    # Buat transaksi
    transaction = {
        'nonce': nonce,
        'to': contract_address,
        'value': web3.to_wei(0.1, 'ether'),  # Mengirim 0.1 ETH # IZIN YA BANG ADE
        'gas': gas_limit,  # Gunakan gas limit yang diestimasi
        'gasPrice': web3.eth.gas_price,
        'chainId': chain_id,
        'data': data
    }

    # Tanda tangani transaksi dengan private key
    try:
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
    except Exception as e:
        print(f"Error signing transaction: {e}")
        return None

    # Kirim transaksi
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)  # Menggunakan raw_transaction
        return web3.to_hex(tx_hash)
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

# Fungsi utama untuk mengirim beberapa transaksi
def send_multiple_transactions(num_transactions):
    successful_txs = 0
    try:
        for _ in range(num_transactions):
            tx_hash = send_bridge_transaction()
            if tx_hash:
                successful_txs += 1
                print(f"Tx Hash: {tx_hash} | Total Tx Sukses: {successful_txs}")
            time.sleep(config.delay_transaksi)  # Delay 30 detik setiap transaksi
    except KeyboardInterrupt:
        print("\nScript dihentikan oleh pengguna.")
    print(f"Total transaksi sukses: {successful_txs}")

# Jumlah transaksi yang ingin dikirim
try:
    num_transactions = int(input("Masukkan jumlah transaksi yang ingin dikirim: "))
    send_multiple_transactions(num_transactions)
except ValueError:
    print("Input tidak valid, pastikan untuk memasukkan angka.")
    sys.exit(1)
