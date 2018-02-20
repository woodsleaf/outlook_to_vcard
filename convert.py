# -*- coding: utf-8 -*-
# python 3.x

import csv
import sys

# convert a "comma separated values" file to vcf contact cards. I used this to
# convert a list of student
# names and phone numbers into a vcf and save the trouble of adding one by one
# through phone

# USAGE:
# CSV_to_Vcards.py CSV_filename


def adrtostr(adrlist):
    at = ''
    for k in adrlist:
        at += str(k.strip().replace('\n', '\\n')) + ';'
    # print(at)
    return at # Сборка адреса


def convert(somefile):
    # assuming file format : lastname,firstname,phonenumber,mail
    n, org = {}, {}
    with open(somefile, 'r') as source:
        # reader now holds the whole data like ['lastname', 'firstname',
        # 'phonenumber', 'mail']
        reader = csv.reader(source, delimiter=';', quotechar='"')  # csv.DictReader
        allvcf = open(str(somefile + '.vcf'), 'w')  # allvcf = open('ALL.vcf', 'w')
        next(reader)
        i = 0
        for row in reader:
            categories = row[56]  # if row[56] is not None else ''
            n.update({1: row[3]})  # 'Фамилия':'N.1',
            n.update({2: row[1]})  # 'Имя':'N.2',
            n.update({3: row[2]})  # 'Отество':'N.3',
            n.update({4: row[0]})  # 'Обращение':'N4',
            n.update({5: row[4]})  # 'Суффикс':'N.5',
            fnvalue = n[1] + ' ' + n[2] + ' ' + n[3] + ' ' + n[4] + ' ' + n[5]

            # nickname
            bday = row[51].replace('0.0.00', '')  # 'Деньрождения':'BDAY',
            title = row[7]  # 'Должность':'TITLE',
            # role
            org.update({1: row[5]})  # 'Организация':'ORG.1',
            org.update({2: row[6]})  # 'Отдел':'ORG.2',
            email = [row[82], row[85], row[88]]  # 'Адресэлпоты':'EMAIL;TYPE=internet',
            note = row[53].replace('\n', '\\n')
            
            # 'Улицарабадрес':'ADR;TYPE=work.2',
            # 'Улица2рабадрес':'ADR;TYPE=work.2',
            # 'Улица3рабадрес':'ADR;TYPE=work.2',
            # 'Городрабадрес':'ADR;TYPE=work.3',
            # 'Областьрабадрес':'ADR;TYPE=work.4',
            # 'Индексрабадрес':'ADR;TYPE=work.5',
            # 'Странарабадрес':'ADR;TYPE=work.6',
            atwork = ['',
                      '',
                      str(row[8]) + ' ' + str(row[9]) + ' ' + str(row[10]),
                      row[11],
                      row[12],
                      row[13],
                      row[14]
                      ]
            # 'Потовыйкоддом':'ADR;TYPE=home.1',
            # 'Улицадомадрес':'ADR;TYPE=home.2',
            # 'Улица2домадрес':'ADR;TYPE=home.2',
            # 'Улица3домадрес':'ADR;TYPE=home.2',
            # 'Городдомадрес':'ADR;TYPE=home.3',
            # 'Областьдомадрес':'ADR;TYPE=home.4',
            # 'Индексдомадрес':'ADR;TYPE=home.5',
            # 'Странадомадрес':'ADR;TYPE=home.6',
            athome = ['',
                      row[20],
                      str(row[15]) + ' ' + str(row[16]) + ' ' + str(row[17]),
                      row[18],
                      row[19],
                      '',
                      row[21]
                      ]
            # 'Улицадругойадрес':'ADR;TYPE=postal.2',
            # 'Улица2другойадрес':'ADR;TYPE=postal.2',
            # 'Улица3другойадрес':'ADR;TYPE=postal.2',
            # 'Городдругойадрес':'ADR;TYPE=postal.3',
            # 'Областьдругойадрес':'ADR;TYPE=postal.4',
            # 'Индексдругойадрес':'ADR;TYPE=postal.5',
            # 'Странадругойадрес':'ADR;TYPE=postal.6',
            atpostal = ['',
                        '',
                        str(row[22]) + ' ' + str(row[23]) + ' ' + str(row[24]),
                        row[25],
                        row[26],
                        row[27],
                        row[28]
                        ]
            atw = adrtostr(atwork)
            ath = adrtostr(athome)
            atp = adrtostr(atpostal)

            tcell = row[41]  # 'Телефонпереносной':'TEL;TYPE=cell',
            tpager = [row[29],row[43]]  # 'Телефонпомощника', 'Пейджер':'TEL;TYPE=pager',
            tmobile = row[45]  # 'Радиотелефон':'TEL;TYPE=pcs',
            twork = [row[31],row[32], row[35]]  # 'Рабоийтелефон','Телефонраб2':'TEL;TYPE=work',
            # tworkmain = row[35]  # 'Основнойтелефонорганизации':'TEL;TYPE=work',
            tworkfax = row[30]  # 'Рабоийфакс':'TEL;TYPE=work;TYPE=fax',
            tcallback = row[33]  # 'Обратныйвызов':'TEL;TYPE=X-EVOLUTION-CALLBACK',
            tcar = row[34]  # 'Телефонвмашине':'TEL;TYPE=car',
            thome = [row[37], row[38]]  # 'Домашнийтелефон', 'Телефондом2':'TEL;TYPE=home',
            thfax = row[36]  # 'Домашнийфакс':'TEL;TYPE=home;TYPE=fax',
            tisdn = row[39]  # 'ISDN':'TEL;TYPE=isdn',
            tofax = row[41]  # 'Другойфакс':'TEL;TYPE=fax',
            tother = row[42]  # 'Другойтелефон':'TEL',
            tmain = row[44]  # 'Основнойтелефон':'TEL',
            teletype =row[46]  # ' Телетайптелефонститрами':'TEL;TYPE=msg',
            telex = row[47]  # 'Телекс':'TEL;TYPE=msg',
            
            url = row[49]  # 'Вебстраница':'URL',
            godovshina = row[50].replace('0.0.00', '')  # 'Годовщина':'X-ANNIVERSARY',
            helpername = row[54]  # 'Имяпомощника':'X-ASSISTANT',
            keyword = row[57].replace('\n', '\\n')  # 'Клюевыеслова':'NOTE',
            supruga = row[77]  # 'Супруга':'X-SPOUSE',

            '''
            outlook = {
              'Важность':'',
              'Дети':'',
              'Инициалы':'',
              
              'Кодорганизации':'',
              'Линыйкод':'',
              'Отложено':'',
              'Пол':'',
              'Пользователь1':'',
              'Пользователь2':'',
              'Пользователь3':'',
              'Пользователь4':'',
              'Пометка':'',
              'Потовыйящикдомадрес':'',
              'Потовыйящикдругойадрес':'',
              'Потовыйящикрабадрес':'',
              'Профессия':'',
              'Расположение':'',
              'Расположениекомнаты':'',
              'Расстояние':'',
              'Расположениекомнаты':'',
              'Расстояние':'',
              'Руководитель':'',
              'СведенияодоступностивИнтернете':'',
              'Серверкаталогов':'',
              
              'Сет':'',
              'Сета':'',
              'Хобби':'',
              '_астное':'',
              'Типэлпоты':'',
              'Краткоеимяэлпоты':'',
              'Тип2элпоты':'',
              'Краткое2имяэлпоты':'',
              'Тип3элпоты':'',
              'Краткое3имяэлпоты':'',
              'Язык':''}
            '''

            # write in individual vcf
            # vcf = open(row[1] + ' ' + row[0] + ".vcf", 'w')
            # vcf.write( 'BEGIN:VCARD' + '\n')
            # vcf.write( 'VERSION:2.1' + '\n')
            # vcf.write( 'N:' + row[0] + ';' + row[1] + '\n')
            # vcf.write( 'FN:' + row[1]
            #    + ' ' + row[0] + '\n')  # rembemer that lastname first
            # vcf.write( 'ORG:' + 'ATI' + '\n')
            # vcf.write( 'TEL;CELL:' + row[2] + '\n')
            # vcf.write( 'EMAIL:' + row[3] + '\n')
            # vcf.write( 'END:VCARD' + '\n')
            # vcf.write( '\n')
            # vcf.close()

            # write in the "ALL.vcf" file.
            allvcf.write('BEGIN:VCARD' + '\n')
            allvcf.write('VERSION:3.0' + '\n')
            allvcf.write('N:' + str(n[1]) + ';' +
                         str(n[2]) + ';' +
                         str(n[3]) + ';' +
                         str(n[4]) + ';' +
                         str(n[5]) + '\n')
            allvcf.write('FN:' + fnvalue + '\n')  # remember that lastname first

            if categories:
                allvcf.write('CATEGORIES:' + categories + '\n')
            # allvcf.write('NICKNAME:' + nickname + '\n')
            if bday:
                allvcf.write('BDAY:' + str(bday) + '\n')
            if title:
                allvcf.write('TITLE:' + title + '\n')
            if org[1] or org[2]:
                allvcf.write('ORG:' + org[1] + '' + org[2] + '\n')
            if len(ath) > 7:
                allvcf.write('ADR;TYPE=HOME:' + ath + '\n')
            if len(atw) > 7:
                allvcf.write('ADR;TYPE=WORK:' + atw + '\n')
            if len(atp) > 7:
                allvcf.write('ADR;TYPE=POSTAL:' + atp + '\n')
            
            if tcell:
                allvcf.write('TEL;CELL:' + tcell + '\n')
            for each in tpager:
              if each:
                  allvcf.write('TEL;TYPE=pager:' + each + '\n')
            if tmobile:
                allvcf.write('TEL;TYPE=pcs:' + tmobile + '\n')
            for each in twork:
              if each:
                  allvcf.write('TEL;TYPE=work:' + each + '\n')
            if tworkfax:
                allvcf.write('TEL;TYPE=work;TYPE=fax:' + tworkfax + '\n')
            if tcallback:
                allvcf.write('TEL;TYPE=X-EVOLUTION-CALLBACK:' + tcallback + '\n')
            if tcar:
                allvcf.write('TEL;TYPE=car:' + tcar + '\n')
            for each in thome:
                if each:
                    allvcf.write('TEL;TYPE=home:' + each + '\n')
            if thfax:
                allvcf.write('TEL;TYPE=home;TYPE=fax:' + thfax + '\n')
            if tisdn:
                allvcf.write('TEL;TYPE=isdn:' + tisdn + '\n')
            if tofax:
                allvcf.write('TEL;TYPE=fax:' + tofax + '\n')
            if tother:
                allvcf.write('TEL:' + tother + '\n')
            if tmain:
                allvcf.write('TEL:' + tmain + '\n')
            if teletype:
                allvcf.write('TEL;TYPE=msg:' + teletype + '\n')
            if telex:
                allvcf.write('TEL;TYPE=msg:' + telex + '\n')
                
            if godovshina:
                allvcf.write('X-ANNIVERSARY:' + godovshina + '\n')
            if helpername:
                allvcf.write('X-ASSISTANT:' + helpername + '\n')

            if url:
                allvcf.write('URL:' + url + '\n')
            for each in email:
              if each:
                  allvcf.write('EMAIL:' + each + '\n')
            if note or keyword:
                allvcf.write('NOTE:' + note + ' ' + keyword + '\n')
            if supruga:
                allvcf.write('X-SPOUSE:' + supruga + '\n')

            allvcf.write('END:VCARD' + '\n')
            allvcf.write('\n')

            i += 1  # counts

        allvcf.close()
        print(str(i) + " vcf cards generated")


def main(args):
    if len(args) != 2:
        #convert('own.csv')
        print("Usage:")
        print(args[0] + " filename")
        return

    convert(args[1])


if __name__ == '__main__':
main(sys.argv)
