import binascii, hashlib, hmac, struct
from ecdsa.curves import SECP256k1
from eth_utils import to_checksum_address, keccak as eth_utils_keccak
import mnem
import time

BIP39_PBKDF2_ROUNDS = 2048
BIP39_SALT_MODIFIER = "mnemonic"
BIP32_PRIVDEV = 0x80000000
BIP32_CURVE = SECP256k1
BIP32_SEED_MODIFIER = b'Bitcoin seed'
ETH_DERIVATION_PATH = "m/44'/60'/0'/0"

class PublicKey:
    def __init__(self, private_key):
        self.point = int.from_bytes(private_key, byteorder='big') * BIP32_CURVE.generator

    def __bytes__(self):
        xstr = self.point.x().to_bytes(32, byteorder='big')
        parity = self.point.y() & 1
        return (2 + parity).to_bytes(1, byteorder='big') + xstr

    def address(self):
        x = self.point.x()
        y = self.point.y()
        s = x.to_bytes(32, 'big') + y.to_bytes(32, 'big')
        return to_checksum_address(eth_utils_keccak(s)[12:])

def mnemonic_to_bip39seed(mnemonic, passphrase):
    mnemonic = bytes(mnemonic, 'utf8')
    salt = bytes(BIP39_SALT_MODIFIER + passphrase, 'utf8')
    return hashlib.pbkdf2_hmac('sha512', mnemonic, salt, BIP39_PBKDF2_ROUNDS)

def bip39seed_to_bip32masternode(seed):
    k = seed
    h = hmac.new(BIP32_SEED_MODIFIER, seed, hashlib.sha512).digest()
    key, chain_code = h[:32], h[32:]
    return key, chain_code

def derive_bip32childkey(parent_key, parent_chain_code, i):
    assert len(parent_key) == 32
    assert len(parent_chain_code) == 32
    k = parent_chain_code
    if (i & BIP32_PRIVDEV) != 0:
        key = b'\x00' + parent_key
    else:
        key = bytes(PublicKey(parent_key))
    d = key + struct.pack('>L', i)
    while True:
        h = hmac.new(k, d, hashlib.sha512).digest()
        key, chain_code = h[:32], h[32:]
        a = int.from_bytes(key, byteorder='big')
        b = int.from_bytes(parent_key, byteorder='big')
        key = (a + b) % BIP32_CURVE.order
        if a < BIP32_CURVE.order and key != 0:
            key = key.to_bytes(32, byteorder='big')
            break
        d = b'\x01' + h[32:] + struct.pack('>L', i)
    return key, chain_code

def parse_derivation_path(str_derivation_path):
    path = []
    if str_derivation_path[0:2] != 'm/':
        raise ValueError("Can't recognize derivation path. It should look like \"m/44'/60/0'/0\".")
    for i in str_derivation_path.lstrip('m/').split('/'):
        if "'" in i:
            path.append(BIP32_PRIVDEV + int(i[:-1]))
        else:
            path.append(int(i))
    return path

def mnemonic_to_private_key(mnemonic, str_derivation_path, passphrase=""):
    derivation_path = parse_derivation_path(str_derivation_path)
    bip39seed = mnemonic_to_bip39seed(mnemonic, passphrase)
    master_private_key, master_chain_code = bip39seed_to_bip32masternode(bip39seed)
    private_key, chain_code = master_private_key, master_chain_code
    for i in derivation_path:
        private_key, chain_code = derive_bip32childkey(private_key, chain_code, i)
    return private_key


if __name__ == '__main__':
    print('start')
    start_time = time.time()
    for i in range(1000):
        mnemonic = mnem.main()
        #mnemonic = 'help bid unhappy broken attack mail sudden armed renew rely lawsuit elbow'
        private_key = mnemonic_to_private_key(mnemonic,
            str_derivation_path=f'{ETH_DERIVATION_PATH}/0')
        public_key = PublicKey(private_key)
    
    end_time = time.time()
    print(f"------END----- It took {end_time - start_time:.2f} seconds to compute")
    
    print(f'mnemonic: ' + mnemonic)
    print(f'privkey: {binascii.hexlify(private_key).decode("utf-8")}')
    print(f'pubkey:  {binascii.hexlify(bytes(public_key)).decode("utf-8")}')
    print(f'address: {public_key.address()}')
    
    
    #'0x90382a68CB82d26Ed74e9E0c2E66fec4107652e3    '