from lxml import html
import requests
import time
import os


def ReADD(hash):
    try:
        urlAdress = "https://www.blockchain.com/ru/eth/tx/" + hash
        test = requests.get(urlAdress, timeout=5)
        byte_string = test.content
        source_code = html.fromstring(byte_string)
        adr1 = '/html/body/div[1]/div[3]/div[2]/div/div/div[3]/div/div/div[2]/div/div[3]/div[2]/div/a'
        adr2 = '/html/body/div[1]/div[3]/div[2]/div/div/div[3]/div/div/div[2]/div/div[4]/div[2]/div/div/a'
        tree1 = source_code.xpath(adr1)
        tree2 = source_code.xpath(adr2)
        try:
            V1 = str(tree1[0].text_content())
            with open("ETHadr.txt", "a", encoding="utf-8") as f:
                f.write(V1 + '\n')
                print(V1)
        except IndexError:
            V1 = 0
        try:
            V2 = str(tree2[0].text_content())
            with open("ETHadr.txt", "a", encoding="utf-8") as f:
                f.write(V2 + '\n')
                print(V2)
        except IndexError:
            V2 = 0

    except requests.exceptions.RequestException:
        print('Er')


ref = '0x92657fc9bba9c0057bfa65fea40000542f0cc301'
counts = 0

while True:
    start_time = time.time()
    if counts % 3 == 0:
        os.system('cls')
    print('Scan Number [' + str(counts) + '] ')
    try:
        urlHash = "https://www.blockchain.com/eth/unconfirmed-transactions"
        test = requests.get(urlHash, timeout=5)
        byte_string = test.content
        source_code = html.fromstring(byte_string)
        hash1 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/a'
        hash2 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[1]/div[2]/a'
        hash3 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[8]/div[1]/div[2]/a'
        hash4 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[1]/div[2]/a'
        hash5 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]/a'
        hash6 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[6]/div[1]/div[2]/a'
        hash7 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[7]/div[1]/div[2]/a'
        hash8 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[9]/div[1]/div[2]/a'
        hash9 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[13]/div[1]/div[2]/a'
        hash10 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[10]/div[1]/div[2]/a'
        hash11 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[11]/div[1]/div[2]/a'
        hash12 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[12]/div[1]/div[2]/a'
        hash13 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[14]/div[1]/div[2]/a'
        hash14 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[15]/div[1]/div[2]/a'
        hash15 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[16]/div[1]/div[2]/a'
        hash16 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[17]/div[1]/div[2]/a'
        hash17 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[18]/div[1]/div[2]/a'
        hash18 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[19]/div[1]/div[2]/a'
        hash19 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[20]/div[1]/div[2]/a'
        hash20 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[21]/div[1]/div[2]/a'
        hash122 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[22]/div[1]/div[2]/a'
        hash222 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[23]/div[1]/div[2]/a'
        hash322 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[24]/div[1]/div[2]/a'
        hash422 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[25]/div[1]/div[2]/a'
        hash522 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[26]/div[1]/div[2]/a'
        hash622 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[27]/div[1]/div[2]/a'
        hash722 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[28]/div[1]/div[2]/a'
        hash822 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[29]/div[1]/div[2]/a'
        hash922 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[30]/div[1]/div[2]/a'
        hash1022 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[31]/div[1]/div[2]/a'
        hash1122 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[32]/div[1]/div[2]/a'
        hash1222 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[33]/div[1]/div[2]/a'
        hash1322 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[34]/div[1]/div[2]/a'
        hash1422 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[35]/div[1]/div[2]/a'
        hash1522 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[36]/div[1]/div[2]/a'
        hash1622 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[37]/div[1]/div[2]/a'
        hash1722 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[38]/div[1]/div[2]/a'
        hash1822 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[39]/div[1]/div[2]/a'
        hash1922 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[40]/div[1]/div[2]/a'
        hash2022 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[41]/div[1]/div[2]/a'
        tree1 = source_code.xpath(hash1)
        tree2 = source_code.xpath(hash2)
        tree3 = source_code.xpath(hash3)
        tree4 = source_code.xpath(hash4)
        tree5 = source_code.xpath(hash5)
        tree6 = source_code.xpath(hash6)
        tree7 = source_code.xpath(hash7)
        tree8 = source_code.xpath(hash8)
        tree9 = source_code.xpath(hash9)
        tree10 = source_code.xpath(hash10)
        tree11 = source_code.xpath(hash11)
        tree12 = source_code.xpath(hash12)
        tree13 = source_code.xpath(hash13)
        tree14 = source_code.xpath(hash14)
        tree15 = source_code.xpath(hash15)
        tree16 = source_code.xpath(hash16)
        tree17 = source_code.xpath(hash17)
        tree18 = source_code.xpath(hash18)
        tree19 = source_code.xpath(hash19)
        tree20 = source_code.xpath(hash20)
        tree122 = source_code.xpath(hash122)
        tree222 = source_code.xpath(hash222)
        tree322 = source_code.xpath(hash322)
        tree422 = source_code.xpath(hash422)
        tree522 = source_code.xpath(hash522)
        tree622 = source_code.xpath(hash622)
        tree722 = source_code.xpath(hash722)
        tree822 = source_code.xpath(hash822)
        tree922 = source_code.xpath(hash922)
        tree1022 = source_code.xpath(hash1022)
        tree1122 = source_code.xpath(hash1122)
        tree1222 = source_code.xpath(hash1222)
        tree1322 = source_code.xpath(hash1322)
        tree1422 = source_code.xpath(hash1422)
        tree1522 = source_code.xpath(hash1522)
        tree1622 = source_code.xpath(hash1622)
        tree1722 = source_code.xpath(hash1722)
        tree1822 = source_code.xpath(hash1822)
        tree1922 = source_code.xpath(hash1922)
        tree2022 = source_code.xpath(hash2022)
        V1 = str(tree1[0].text_content())
        V2 = str(tree2[0].text_content())
        V3 = str(tree3[0].text_content())
        V4 = str(tree4[0].text_content())
        V5 = str(tree5[0].text_content())
        V6 = str(tree6[0].text_content())
        V7 = str(tree7[0].text_content())
        V8 = str(tree8[0].text_content())
        V9 = str(tree9[0].text_content())
        V10 = str(tree10[0].text_content())
        V11 = str(tree11[0].text_content())
        V12 = str(tree12[0].text_content())
        V13 = str(tree13[0].text_content())
        V14 = str(tree14[0].text_content())
        V15 = str(tree15[0].text_content())
        V16 = str(tree16[0].text_content())
        V17 = str(tree17[0].text_content())
        V18 = str(tree18[0].text_content())
        V19 = str(tree19[0].text_content())
        V20 = str(tree20[0].text_content())
        V122 = str(tree122[0].text_content())
        V222 = str(tree222[0].text_content())
        V322 = str(tree322[0].text_content())
        V422 = str(tree422[0].text_content())
        V522 = str(tree522[0].text_content())
        V622 = str(tree622[0].text_content())
        V722 = str(tree722[0].text_content())
        V822 = str(tree822[0].text_content())
        V922 = str(tree922[0].text_content())
        V1022 = str(tree1022[0].text_content())
        V1122 = str(tree1122[0].text_content())
        V1222 = str(tree1222[0].text_content())
        V1322 = str(tree1322[0].text_content())
        V1422 = str(tree1422[0].text_content())
        V1522 = str(tree1522[0].text_content())
        V1622= str(tree1622[0].text_content())
        V1722 = str(tree1722[0].text_content())
        V1822 = str(tree1822[0].text_content())
        V1922 = str(tree1922[0].text_content())
        V2022 = str(tree2022[0].text_content())
        if ref == V1:
            print('sovpalo')
            test = requests.post(url=urlHash, headers={'Connection': 'close'})
        else:
            ref = V1
            ReADD(V1)
            ReADD(V2)
            ReADD(V3)
            ReADD(V4)
            ReADD(V5)
            ReADD(V6)
            ReADD(V7)
            ReADD(V8)
            ReADD(V9)
            ReADD(V10)
            ReADD(V11)
            ReADD(V12)
            ReADD(V13)
            ReADD(V14)
            ReADD(V15)
            ReADD(V16)
            ReADD(V17)
            ReADD(V18)
            ReADD(V19)
            ReADD(V20)
            ReADD(V122)
            ReADD(V222)
            ReADD(V322)
            ReADD(V422)
            ReADD(V522)
            ReADD(V622)
            ReADD(V722)
            ReADD(V822)
            ReADD(V922)
            ReADD(V1022)
            ReADD(V1122)
            ReADD(V1222)
            ReADD(V1322)
            ReADD(V1422)
            ReADD(V1522)
            ReADD(V1622)
            ReADD(V1722)
            ReADD(V1822)
            ReADD(V1922)
            ReADD(V2022)
            test = requests.post(url=urlHash, headers={'Connection':'close'})
    except (IndexError, requests.exceptions.RequestException):
        test = requests.post(url=urlHash, headers={'Connection':'close'})
    counts += 1
    end_time = time.time()
    print(test)
    print(f"It took {end_time - start_time:.2f} seconds to compute")

