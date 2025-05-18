from web3 import Web3
from eth_account import Account
import time
import sys

# Detail jaringan
private_key = ''  # GANTI DENGAN PRIVATE KEY ANDA
rpc_url = 'https://b2n.rpc.caldera.xyz/http'  # JANGAN DIGANTI
chain_id = 334  # JANGAN DIGANTI
contract_address_method = '0xAEC9f9DbE3FC031c780d6AF2A489BD003F83E4a7'  # JANGAN DIGANTI (Method address)
contract_address_token = '0xcbEd09fA8F99dc709C23b5c46F002d9ec010FcDA'  # GANTI DENGAN CONTRACT ADDRESS TOKEN YANG INGIN DITUKAR
my_address = ''  # GANTI DENGAN ADDRESS EVM ANDA

# Koneksi ke jaringan
web3 = Web3(Web3.HTTPProvider(rpc_url))
if not web3.is_connected():
    raise Exception("Tidak dapat terhubung ke jaringan")

# Ubah semua alamat menjadi checksum address
contract_address_method = web3.to_checksum_address(contract_address_method)
contract_address_token = web3.to_checksum_address(contract_address_token)
my_address = web3.to_checksum_address(my_address)

# Buat akun dari private key
account = Account.from_key(private_key)

# Fungsi untuk membuat dan mengirim transaksi

def send_bridge_transaction():
    # Ambil nonce untuk alamat pengirim
    nonce = web3.eth.get_transaction_count(my_address)

    # Estimasi gas fee
    try:
        gas_estimate = web3.eth.estimate_gas({
            'to': contract_address_method,
            'from': my_address,
            'data': data,
            'value': 0  # Token transfer tidak membutuhkan ETH value
        })
    except Exception as e:
        print(f"Error estimating gas: {e}")
        return None

    # Buat transaksi
    transaction = {
        'nonce': nonce,
        'to': contract_address_method,
        'value': 0,  # Tidak ada ETH yang dikirim
        'gas': gas_estimate,  # Gunakan gas fee estimasi
        'gasPrice': web3.to_wei(2, 'gwei'),  # Gas price disetel ke 3 Gwei
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
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        return web3.to_hex(tx_hash)  # Kembalikan tx hash
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

# Ambil input dari user
try:
    max_txs = int(input("Masukkan jumlah transaksi sukses yang ingin dicapai: "))
except ValueError:
    print("Input tidak valid, harus berupa angka.")
    sys.exit(1)

# Jalankan script sampai mencapai jumlah transaksi sukses yang diinginkan
successful_txs = 0

while successful_txs < max_txs:
    tx_hash = send_bridge_transaction()
    if tx_hash:
        successful_txs += 1
        print(f"Tx Hash: {tx_hash} | Total Tx Sukses: {successful_txs}")
    else:
        print("Transaksi gagal, mencoba lagi...")
    time.sleep(2)  # Delay 10 detik setiap transaksi

print(f"Sudah mencapai {max_txs} transaksi sukses. Script berhenti.")
sys.exit(0)