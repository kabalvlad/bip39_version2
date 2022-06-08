from hdwallet import BIP49HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.utils import generate_mnemonic
from hdwallet.cryptocurrencies import EthereumMainnet as symbolETH

filename ='eth1.txt' #btc address list to look for database file needed
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1        
with open(filename) as file:
    add = file.read().split()
add = set(add)

def save_data():
    with open("win ETH.txt", "a") as f:
        f.write(f"""\n Mnemonic_words :  {MNEMONIC}
        Privatekey : {target_wallet['privatekeyETH']}
        Derivation Path ETH :  {target_wallet['pathETH']} 
        Public Address ETH:                                            
        {target_wallet['ETHp2pkh']}  
        """)



def data_all():
    data.append({
        'ETHp2pkh': bip44_ETH.p2pkh_address(),
        #'15S3PCw1g6UW7zPMD5i3B44gH1nPLg9YUy': '1FHxjiN379MB6rgPtWGYx1QW9j8gHw5R5P', #test

        'privatekeyETH': bip44_ETH.private_key(),

        'pathETH': bip44_ETH.path(),

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
    bip44_ETH: BIP44HDWallet = BIP44HDWallet(
        cryptocurrency=symbolETH, account=0, change=False, address=0
    )
    bip44_ETH.from_mnemonic(
        mnemonic=MNEMONIC, language=LANGUAGE
    )

    data_all()
    for target_wallet in data:
        ETHadr = target_wallet['ETHp2pkh']



        if ETHadr in add:
            print('\nMatch Found')
            save_data()
    else:
        if display == 1:
            print('ETH scan [' + str(count) + '] ------------------------')
            print('Total Checked [' + str(total) + '] ')
            print('mnemonic_words  : ' + MNEMONIC)
            for target_wallet in data:
                print(target_wallet['pathETH'], '  : ETH  Address : ', target_wallet['ETHp2pkh'])
                #save_data()


        if display == 2:
            print('ETH Scan Number [' + str(count) + '] ------', 'Total Checked [' + str(total) + '] ', end='\r')