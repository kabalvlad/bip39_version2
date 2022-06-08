from lxml import html
import requests
import time
import os


#запись полученых адрессов
def Re1(hash):
    try:
        urlAdress = "https://etherscan.io/tx/" + hash
        test = requests.get(urlAdress, headers=headers, timeout=30)
        byte_string = test.content
        source_code = html.fromstring(byte_string)
        adr1 = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div/div[6]/div[2]/a[1]'
        tree1 = source_code.xpath(adr1)
        try:
            V1 = str(tree1[0].text_content())
            with open("ETHadr.txt", "a", encoding="utf-8") as f:
                f.write(V1 + '\n')
                print(V1)
        except IndexError:
            test = requests.post(url=urlAdress, headers={'Connection': 'close'})
            V1 = 0
        test = requests.post(url=urlAdress, headers={'Connection': 'close'})
    except requests.exceptions.RequestException:
        print('Er')

def Re2(hash):
    try:
        urlAdress = "https://etherscan.io/tx/" + hash
        test = requests.get(urlAdress, headers=headers, timeout=30)
        byte_string = test.content
        source_code = html.fromstring(byte_string)
        adr2 = '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div/div[7]/div[2]/a[2]'
        tree2 = source_code.xpath(adr2)
        try:
            V2 = str(tree2[0].text_content())
            with open("ETHadr.txt", "a", encoding="utf-8") as f:
                f.write(V2 + '\n')
                print(V2)
        except IndexError:
            test = requests.post(url=urlAdress, headers={'Connection': 'close'})
            V2 = 0
        test = requests.post(url=urlAdress, headers={'Connection': 'close'})
    except requests.exceptions.RequestException:
        print('Er')



def ReADD(hash):
    try:
        urlAdress = "https://blockscan.com/tx/" + hash
        test = requests.get(urlAdress, headers=headers, timeout=40)
        print('связь в методе', test)
        print('номер транзакции \n', hash)
        byte_string = test.content
        source_code = html.fromstring(byte_string)
        adr1 = '/html/body/main/div/div/div[2]/div/div[3]/div/div[3]/div[2]/div/div/a'
        tree1 = source_code.xpath(adr1)
        try:
            V1 = str(tree1[0].text_content())
            with open("ETHadr.txt", "a", encoding="utf-8") as f:
                f.write(V1 + '\n')
                print(V1)
        except IndexError:
            print('Attention')
            Re1(hash)
        adr2 = '/html/body/main/div/div/div[2]/div/div[3]/div/div[4]/div[2]/div/div/a'
        tree2 = source_code.xpath(adr2)
        try:
            V2 = str(tree2[0].text_content())
            with open("ETHadr.txt", "a", encoding="utf-8") as f:
                f.write(V2 + '\n')
                print(V2)
        except IndexError:
            print('Attention')
            Re2(hash)
    except requests.exceptions.RequestException:
        print('Er')

#проверка на повтор
ref = '0xcde95507ea6929021bd3eab1881a627b2e870631'
#счетчик
counts = 0
#заголовок и адресс ссылки


#Начало поиска)
while True:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
    urlHash = "https://etherscan.io/txs"
    #Чистка командной строки
    if counts % 3 == 0:
        os.system('cls')
    # стартовый время и коментарии
    start_time = time.time()
    print('Scan Number ETH [' + str(counts) + '] ')

    try:
        test = requests.get(urlHash, headers=headers,timeout=40) #вход в страницу
        #проверка на повтор
        byte_string = test.content
        source_code = html.fromstring(byte_string)
        hashB = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[1]/td[2]/span/a'
        treetxid = source_code.xpath(hashB)
        print('связь', test)
        try:
            hashAdr = str(treetxid[0].text_content())
        except IndexError:
            hashAdr = ref
        if ref == hashAdr:
            print('sovpalo')
            test = requests.post(url=urlHash, headers={'Connection': 'close'})
        # конец проверки
        else:
            #проеврка адресов
            ref = hashAdr
            thash1 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[2]/td[2]/span/a'
            thash2 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[3]/td[2]/span/a'
            thash3 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[4]/td[2]/span/a'
            thash4 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[5]/td[2]/span/a'
            thash5 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[6]/td[2]/span/a'
            thash6 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[7]/td[2]/span/a'
            thash7 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[8]/td[2]/span/a'
            thash8 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[9]/td[2]/span/a'
            thash9 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[10]/td[2]/span/a'
            thash10 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[11]/td[2]/span/a'
            thash11 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[12]/td[2]/span/a'
            thash12 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[13]/td[2]/span/a'
            thash13 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[14]/td[2]/span/a'
            thash14 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[15]/td[2]/span/a'
            thash15 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[16]/td[2]/span/a'
            thash16 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[17]/td[2]/span/a'
            thash17 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[18]/td[2]/span/a'
            thash18 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[19]/td[2]/span/a'
            thash19 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[20]/td[2]/span/a'
            thash20 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[21]/td[2]/span/a'
            thash21 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[22]/td[2]/span/a'
            thash22 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[23]/td[2]/span/a'
            thash23 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[24]/td[2]/span/a'
            thash24 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[25]/td[2]/span/a'
            thash25 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[26]/td[2]/span/a'
            thash26 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[27]/td[2]/span/a'
            thash27 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[28]/td[2]/span/a'
            thash28 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[29]/td[2]/span/a'
            thash29 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[30]/td[2]/span/a'
            thash30 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[31]/td[2]/span/a'
            thash31 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[32]/td[2]/span/a'
            thash32 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[33]/td[2]/span/a'
            thash33 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[34]/td[2]/span/a'
            thash34 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[35]/td[2]/span/a'
            thash35 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[36]/td[2]/span/a'
            thash36 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[37]/td[2]/span/a'
            thash37 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[38]/td[2]/span/a'
            thash38 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[39]/td[2]/span/a'
            thash39 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[40]/td[2]/span/a'
            thash40 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[41]/td[2]/span/a'
            thash41 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[42]/td[2]/span/a'
            thash42 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[43]/td[2]/span/a'
            thash43 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[44]/td[2]/span/a'
            thash44 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[45]/td[2]/span/a'
            thash45 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[46]/td[2]/span/a'
            thash46 = '/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr[47]/td[2]/span/a'

            try:
                treetxid1 = source_code.xpath(thash1)
                hashAdr1 = str(treetxid1[0].text_content())
            except IndexError:
                print('err1')
            try:
                treetxid2 = source_code.xpath(thash2)
                hashAdr2 = str(treetxid2[0].text_content())
            except IndexError:
                print('err2')
            try:
                treetxid3 = source_code.xpath(thash3)
                hashAdr3 = str(treetxid3[0].text_content())
            except IndexError:
                print('err3')
            try:
                treetxid4 = source_code.xpath(thash4)
                hashAdr4 = str(treetxid4[0].text_content())
            except IndexError:
                print('err4')
            try:
                treetxid5 = source_code.xpath(thash5)
                hashAdr5 = str(treetxid5[0].text_content())
            except IndexError:
                print('err5')
            try:
                treetxid6 = source_code.xpath(thash6)
                hashAdr6 = str(treetxid6[0].text_content())
            except IndexError:
                print('err6')
            try:
                treetxid7 = source_code.xpath(thash7)
                hashAdr7 = str(treetxid7[0].text_content())
            except IndexError:
                print('err7')
            try:
                treetxid8 = source_code.xpath(thash8)
                hashAdr8 = str(treetxid8[0].text_content())
            except IndexError:
                print('err8')
            try:
                treetxid9 = source_code.xpath(thash9)
                hashAdr9 = str(treetxid9[0].text_content())
            except IndexError:
                print('err9')
            try:
                treetxid10 = source_code.xpath(thash10)
                hashAdr10 = str(treetxid10[0].text_content())
            except IndexError:
                print('err10')
            try:
                treetxid11 = source_code.xpath(thash11)
                hashAdr11 = str(treetxid11[0].text_content())
            except IndexError:
                print('err11')
            try:
                treetxid12 = source_code.xpath(thash12)
                hashAdr12 = str(treetxid12[0].text_content())
            except IndexError:
                print('err12')
            try:
                treetxid13 = source_code.xpath(thash13)
                hashAdr13 = str(treetxid13[0].text_content())
            except IndexError:
                print('err13')
            try:
                treetxid14 = source_code.xpath(thash14)
                hashAdr14 = str(treetxid14[0].text_content())
            except IndexError:
                print('err14')
            try:
                treetxid15 = source_code.xpath(thash15)
                hashAdr15 = str(treetxid15[0].text_content())
            except IndexError:
                print('err15')
            try:
                treetxid16 = source_code.xpath(thash16)
                hashAdr16 = str(treetxid16[0].text_content())
            except IndexError:
                print('err16')
            try:
                treetxid17 = source_code.xpath(thash17)
                hashAdr17 = str(treetxid17[0].text_content())
            except IndexError:
                print('err17')
            try:
                treetxid18 = source_code.xpath(thash18)
                hashAdr18 = str(treetxid18[0].text_content())
            except IndexError:
                print('err18')
            try:
                treetxid19 = source_code.xpath(thash19)
                hashAdr19 = str(treetxid19[0].text_content())
            except IndexError:
                print('err19')
            try:
                treetxid20 = source_code.xpath(thash20)
                hashAdr20 = str(treetxid20[0].text_content())
            except IndexError:
                print('err20')
            try:
                treetxid21 = source_code.xpath(thash21)
                hashAdr21 = str(treetxid21[0].text_content())
            except IndexError:
                print('err21')
            try:
                treetxid22 = source_code.xpath(thash22)
                hashAdr22 = str(treetxid22[0].text_content())
            except IndexError:
                print('err22')
            try:
                treetxid23 = source_code.xpath(thash23)
                hashAdr23 = str(treetxid23[0].text_content())
            except IndexError:
                print('err23')
            try:
                treetxid24 = source_code.xpath(thash24)
                hashAdr24 = str(treetxid24[0].text_content())
            except IndexError:
                print('err24')
            try:
                treetxid25 = source_code.xpath(thash25)
                hashAdr25 = str(treetxid25[0].text_content())
            except IndexError:
                print('err25')
            try:
                treetxid26 = source_code.xpath(thash26)
                hashAdr26 = str(treetxid26[0].text_content())
            except IndexError:
                print('err26')
            try:
                treetxid27 = source_code.xpath(thash27)
                hashAdr27 = str(treetxid27[0].text_content())
            except IndexError:
                print('err27')
            try:
                treetxid28 = source_code.xpath(thash28)
                hashAdr28 = str(treetxid28[0].text_content())
            except IndexError:
                print('err28')
            try:
                treetxid29 = source_code.xpath(thash29)
                hashAdr29 = str(treetxid29[0].text_content())
            except IndexError:
                print('err29')
            try:
                treetxid30 = source_code.xpath(thash30)
                hashAdr30 = str(treetxid30[0].text_content())
            except IndexError:
                print('err30')
            try:
                treetxid31 = source_code.xpath(thash31)
                hashAdr31 = str(treetxid31[0].text_content())
            except IndexError:
                print('err31')
            try:
                treetxid32 = source_code.xpath(thash32)
                hashAdr32 = str(treetxid32[0].text_content())
            except IndexError:
                print('err32')
            try:
                treetxid33 = source_code.xpath(thash33)
                hashAdr33 = str(treetxid33[0].text_content())
            except IndexError:
                print('err33')
            try:
                treetxid34 = source_code.xpath(thash34)
                hashAdr34 = str(treetxid34[0].text_content())
            except IndexError:
                print('err34')
            try:
                treetxid35 = source_code.xpath(thash35)
                hashAdr35 = str(treetxid35[0].text_content())
            except IndexError:
                print('err35')
            try:
                treetxid36 = source_code.xpath(thash36)
                hashAdr36 = str(treetxid36[0].text_content())
            except IndexError:
                print('err36')
            try:
                treetxid37 = source_code.xpath(thash37)
                hashAdr37 = str(treetxid37[0].text_content())
            except IndexError:
                print('err37')
            try:
                treetxid38 = source_code.xpath(thash38)
                hashAdr38 = str(treetxid38[0].text_content())
            except IndexError:
                print('err38')
            try:
                treetxid39 = source_code.xpath(thash39)
                hashAdr39 = str(treetxid39[0].text_content())
            except IndexError:
                print('err39')
            try:
                treetxid40 = source_code.xpath(thash40)
                hashAdr40 = str(treetxid40[0].text_content())
            except IndexError:
                print('err40')
            try:
                treetxid41 = source_code.xpath(thash41)
                hashAdr41 = str(treetxid41[0].text_content())
            except IndexError:
                print('err41')
            try:
                treetxid42 = source_code.xpath(thash42)
                hashAdr42 = str(treetxid42[0].text_content())
            except IndexError:
                print('err42')
            try:
                treetxid43 = source_code.xpath(thash43)
                hashAdr43 = str(treetxid43[0].text_content())
            except IndexError:
                print('err43')
            try:
                treetxid44 = source_code.xpath(thash44)
                hashAdr44 = str(treetxid44[0].text_content())
            except IndexError:
                print('err44')
            try:
                treetxid45 = source_code.xpath(thash45)
                hashAdr45 = str(treetxid45[0].text_content())
            except IndexError:
                print('err45')
            try:
                treetxid46 = source_code.xpath(thash46)
                hashAdr46 = str(treetxid46[0].text_content())
            except IndexError:
                print('err46')

            ReADD(hashAdr1)
            ReADD(hashAdr2)
            ReADD(hashAdr3)
            ReADD(hashAdr4)
            ReADD(hashAdr5)
            ReADD(hashAdr6)
            ReADD(hashAdr7)
            ReADD(hashAdr8)
            ReADD(hashAdr9)
            ReADD(hashAdr10)
            ReADD(hashAdr11)
            ReADD(hashAdr12)
            ReADD(hashAdr13)
            ReADD(hashAdr14)
            ReADD(hashAdr15)
            ReADD(hashAdr16)
            ReADD(hashAdr17)
            ReADD(hashAdr18)
            ReADD(hashAdr19)
            ReADD(hashAdr20)
            ReADD(hashAdr21)
            ReADD(hashAdr22)
            ReADD(hashAdr23)
            ReADD(hashAdr24)
            ReADD(hashAdr25)
            ReADD(hashAdr26)
            ReADD(hashAdr27)
            ReADD(hashAdr28)
            ReADD(hashAdr29)
            ReADD(hashAdr30)
            ReADD(hashAdr31)
            ReADD(hashAdr32)
            ReADD(hashAdr33)
            ReADD(hashAdr34)
            ReADD(hashAdr35)
            ReADD(hashAdr36)
            ReADD(hashAdr37)
            ReADD(hashAdr38)
            ReADD(hashAdr39)
            ReADD(hashAdr40)
            ReADD(hashAdr41)
            ReADD(hashAdr42)
            ReADD(hashAdr43)
            ReADD(hashAdr44)
            ReADD(hashAdr45)
            ReADD(hashAdr46)

            test = requests.post(url=urlHash, headers={'Connection':'close'}) #конец запроса
    except requests.exceptions.RequestException:
        print(test, ' нет связи до старта цикла')
        test = requests.post(url=urlHash, headers={'Connection': 'close'})
    counts += 1
    end_time = time.time()
    print(f"------END----- It took {end_time - start_time:.2f} seconds to compute")

