import os
import time
import hashlib
import binascii
import ecdsa
import smtplib
import mmap
screen_print_after_keys = 5000

################################################################
def loadadrs():
    btc_list = set()
    with open("Bitcoin_addresses.txt", mode="r", encoding="utf8") as fp:
        with mmap.mmap(fp.fileno(), length=0, access=mmap.ACCESS_READ) as mobj:
            btc_list.update(mobj.read().splitlines())
    #print(len(btc_list))
    fp.close()
    print("Загрузка завершена")
    return btc_list

################################################################
def generate_private_key():
    return binascii.hexlify(os.urandom(32)).decode('utf-8')

################################################################
def private_key_to_public_key(private_key):
    sign = ecdsa.SigningKey.from_string(binascii.unhexlify(private_key), curve = ecdsa.SECP256k1)
    return ('04' + binascii.hexlify(sign.verifying_key.to_string()).decode('utf-8'))


################################################################
def public_key_to_address(public_key):
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    count = 0; val = 0
    var = hashlib.new('ripemd160')
    var.update(hashlib.sha256(binascii.unhexlify(public_key.encode())).digest())
    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(('00' + var.hexdigest()).encode())).digest()).hexdigest()
    address = '00' + var.hexdigest() + doublehash[0:8]
    for char in address:
        if (char != '0'):
            break
        count += 1
    count = count // 2
    n = int(address, 16)
    output = []
    while (n > 0):
        n, remainder = divmod (n, 58)
        output.append(alphabet[remainder])
    while (val < count):
        output.append(alphabet[0])
        val += 1
    return ''.join(output[::-1])



################################################################
def check_address(addr, btc_list, private_key, public_key):
    str_object = addr.encode("utf-8")
    if str_object in btc_list:
        print ('Win')
        f = open("Win.txt", "a")
        f.writelines('Private Key: '+ private_key + " PubKey: " + public_key + " Address: " + addr + "\n")
        f.close()
        to_addr = "kabalvlad@tut.by"
        subject = "Найдена мнемоника BTC old"
        text = {private_key + ' Address: ' + addr+ '\n'}
        try:
            send_email(to_addr, subject, text)
        except:
            print('er')      
   
    return

################################################################
def send_email(to_addr, subject, text, encode='utf-8'):
    """
    Отправка электронного письма (email)

    """
    server = "smtp.yandex.ru"
    port = 587
    from_addr = "NikolaiKrovavi1@yandex.by"
    passwd = "gdbfxdkpufqndkci"
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {to_addr}",
           f"Subject: {subject}", mime, charset, "", str(text)))
    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(from_addr, passwd)

        # пробуем послать письмо
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        print('Err...')
        raise err
    finally:
        smtp.quit()

###############################################################################
# ==============================================================================
def generate_mnem_address_pairs():
    btc_list = loadadrs()
    print('[+] Loaded ' + str(len(btc_list)))
    st = time.time()
    print('Starting thread: ')
    k = 1
    while True:
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        address = public_key_to_address(public_key)
        #address = '111111111111111111168xDACCG'
        if k % screen_print_after_keys == 0:
            print("Address " + address + '\n  {:0.2f} Keys/s    :: Total Key Searched: {}'.format(k/(time.time() - st), k) + " Private Key: " + private_key, end='\n')

        k += 1
        check_address(address, btc_list, private_key, public_key)



###############################################################################
if __name__ == '__main__':
    print('[+] Starting.........Wait.....')
    print('[+] Load base address BTC..... 3 - 5 min')
    generate_mnem_address_pairs()
