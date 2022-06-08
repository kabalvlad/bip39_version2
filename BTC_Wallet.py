from hdwallet import BIP49HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.utils import generate_mnemonic
from hdwallet.cryptocurrencies import BitcoinMainnet as symbolBTC

filename ='btc1.txt' #btc address list to look for database file needed
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1        
with open(filename) as file:
    add = file.read().split()
add = set(add)

def save_data():
    with open("win BTC.txt", "a") as f:
        f.write(f"""\n Mnemonic_words :  {MNEMONIC}
        Privatekey : {target_wallet['privatekeyBTC']}
        Derivation Path BTC :  {target_wallet['pathBTC']} 
        Public Address BTC:                                            
        {target_wallet['BTCp2pkh']} 
        {target_wallet['BTCp2sh']} 
        {target_wallet['BTCp2wsh']} 
        {target_wallet['BTCp2wpkh']} 
        {target_wallet['BTCp2wpkh_p2sh']} 
        {target_wallet['BTCp2wsh_p2sh']} 
        """)



def data_all():
    data.append({
        'BTCp2pkh': bip44_BTC.p2pkh_address(),
        'BTCp2sh': bip44_BTC.p2sh_address(),
        'BTCp2wsh': bip44_BTC.p2wsh_address(),
        'BTCp2wpkh': bip44_BTC.p2wpkh_address(),
        'BTCp2wpkh_p2sh': bip44_BTC.p2wpkh_in_p2sh_address(),
        'BTCp2wsh_p2sh': bip44_BTC.p2wsh_in_p2sh_address(),
        #'15S3PCw1g6UW7zPMD5i3B44gH1nPLg9YUy': '1FHxjiN379MB6rgPtWGYx1QW9j8gHw5R5P', #test

        'privatekeyBTC': bip44_BTC.private_key(),

        'pathBTC': bip44_BTC.path(),

    })

data = []
count=0
total= 0
LANGUAGE = "english"
s1 = 128
divs = 1
display = int(input('1=Full Display (Slower) 2=Slient Mode (Faster) : '))

while True:
    data=[]
    count += 1
    total += divs
    MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=s1)

    # BTC
    bip44_BTC: BIP44HDWallet = BIP44HDWallet(
        cryptocurrency=symbolBTC, account=0, change=False, address=0
    )
    bip44_BTC.from_mnemonic(
        mnemonic=MNEMONIC, language=LANGUAGE
    )

    data_all()
    for target_wallet in data:
       #BTCadr = target_wallet['15S3PCw1g6UW7zPMD5i3B44gH1nPLg9YUy'] #test
        BTCadr2 = target_wallet['BTCp2pkh']
        BTCadr3 = target_wallet['BTCp2sh']
        BTCadr4 = target_wallet['BTCp2wsh']
        BTCadr5 = target_wallet['BTCp2wpkh']
        BTCadr6 = target_wallet['BTCp2wpkh_p2sh']
        BTCadr7 = target_wallet['BTCp2wsh_p2sh']


        if BTCadr2 in add or BTCadr3 in add or BTCadr4 in add or BTCadr5 in add or BTCadr6 in add or BTCadr7 in add:
            print('\nMatch Found')
            save_data()
    else:
        if display == 1:
            print('BTC scan [' + str(count) + '] ------------------------')
            print('Total Checked [' + str(total) + '] ')
            print('mnemonic_words  : ' + MNEMONIC)
            for target_wallet in data:
                print(target_wallet['pathBTC'], '  : BTC 2 Address : ', target_wallet['BTCp2pkh'])
                print(target_wallet['pathBTC'], '  : BTC 3 Address : ', target_wallet['BTCp2sh'])
                print(target_wallet['pathBTC'], '  : BTC 4 Address : ', target_wallet['BTCp2wsh'])
                print(target_wallet['pathBTC'], '  : BTC 5 Address : ', target_wallet['BTCp2wpkh'])
                print(target_wallet['pathBTC'], '  : BTC 6 Address : ', target_wallet['BTCp2wpkh_p2sh'])
                print(target_wallet['pathBTC'], '  : BTC 7 Address : ', target_wallet['BTCp2wsh_p2sh'])
                #save_data()


        if display == 2:
            print('BTC Scan Number [' + str(count) + '] ------', 'Total Checked [' + str(total) + '] ', end='\r')