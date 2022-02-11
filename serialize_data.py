import os
from datetime import datetime
import paramiko
import json
import sqlite3

if not os.path.exists('downloads'):
    os.makedirs('downloads')

if not os.path.exists('result'):
    os.makedirs('result')

if not os.path.exists('log'):
    os.makedirs('log')


line_type = {
    '0': 'Header',
    '1': 'Vendas',
    '2': 'Detalhes das vendas',
    '3': 'Lote Financeiro',
    '4': 'Vendas Pagas',
    '5': 'Ajustes',
    '6': 'Antecipações',
    '9': 'Trailer'
}

table1 = {'1': 'Depósito em conta',
          '2': 'Débito Online',
          '3': 'Benefício',
          '4': 'Boleto Bancário',
          '5': 'Cheque Pré',
          '6': 'Cheque',
          '7': 'Crédito Parcelado',
          '8': 'Crédito à Vista',
          '9': 'Débito',
          '10': 'Dinheiro',
          '11': 'Outros',
          '12': 'Repasse de Terceiro',
          '13': 'Transferência entre Contas'}

table2 = {
    '1': 'Master',
    '2': 'Visa',
    '3': 'Amex',
    '4': 'Diners',
    '5': 'Jcb',
    '6': 'Discover',
    '7': 'Elo',
    '8': 'Aura',
    '9': 'Hipercard',
    '10': 'Cabal',
    '11': 'Sorocred',
    '12': 'Cup',
    '13': 'Credsystem',
    '14': 'Sicredi',
    '15': 'VR',
    '16': 'Ticket',
    '17': 'Alelo',
    '18': 'Avista',
    '19': 'Bancred Card',
    '20': 'Banestes',
    '21': 'Bib Club',
    '22': 'Big Card',
    '23': 'Calcard',
    '24': 'Cooper',
    '25': 'Good Card',
    '26': 'Greencard',
    '27': 'Hiper',
    '28': 'Mais!',
    '29': 'Maxx Card',
    '30': 'Minas Cred',
    '31': 'Novocard',
    '33': 'Outro',
    '34': 'Plan',
    '35': 'Policard',
    '36': 'Praticard',
    '37': 'Sodexo',
    '38': 'Softnext',
    '39': 'Syspro Card',
    '40': 'Unik',
    '41': 'Union Pay',
    '42': 'Vb',
    '43': 'Verde Card',
    '44': 'Verocheque',
    '45': 'Visa Vale',
    '46': 'Brasilcard',
    '47': 'Fortbrasil',
    '48': 'Grandcard',
    '49': 'Personalcard',
    '50': 'Valecard',
    '51': 'Credz',
    '52': 'Agiplan',
    '53': 'Esplanada',
    '54': 'ConectCar',
    '55': 'Sem Parar',
    '57': 'Banescard',
    '58': 'PagSeguro',
    '59': 'Dacasa',
    '60': 'Porto Seguro',
    '61': 'Ticket - Ref.',
    '62': 'Ticket - Alim.',
    '63': 'Vr - Ref.',
    '64': 'Vr - Alim.',
    '65': 'Sodexo - Ref.',
    '66': 'Sodexo - Alim.',
    '67': 'Alelo Ref.',
    '68': 'Alelo Alim.',
    '69': 'Alelo Auto',
    '81': 'Bandeira não identificada',
    '70': 'Vr - Auto',
    '71': 'Vr - Cultura',
    '72': 'Vr - Cartão da mamãe',
    '73': 'Sodexo - Premium Pass',
    '74': 'Sodexo - Gift Pass',
    '75': 'Sodexo - Mobility Pass Carro',
    '79': 'Sodexo - Cultura Pass',
    '82': 'Ourocard',
    '84': 'BanriCard',
    '83': 'Banricompras',
    '93': 'Nutricash',
    '85': 'Senff',
    '89': 'Greencard - Alim.',
    '90': 'Greencard - Ref.',
    '91': 'Alelo Cult.',
    '92': 'Alelo multi.',
    '94': 'Banco do Brasil',
    '95': 'Mercado Pago',
    '98': 'Solucard',
    '99': 'VSCard',
    '100': 'Construcard',
    '96': 'Flex Car Visa Vale',
    '97': 'Tricard',
    '101': 'Bradesco',
    '103': 'Ticket Cultura'}

table3 = {
    '2': 'Rede',
    '56': 'Sicredi',
    '57': 'Pago',
    '58': 'Vero',
    '59': 'SafraPay',
    '60': 'Tribanco',
    '61': 'Adyen',
    '62': 'Unicred',
    '195': 'Pop Credicard',
    '196': 'Senff',
    '64': 'Nutricash',
    '200': 'Adquirente indefinido',
    '197': 'MercadoPago',
    '201': 'Tricard',
    '202': 'Unica',
    '204': 'Mercado Livre',
    '1': 'Cielo',
    '3': 'Amex',
    '4': 'Getnet',
    '5': 'Aura',
    '6': 'Ticket',
    '7': 'Sodexo',
    '8': 'Elavon',
    '9': 'Bin',
    '10': 'Stone',
    '23': 'PagSeguro',
    '24': 'Alelo',
    '25': 'Hipercard',
    '26': 'Banricompras',
    '27': 'GoodCard',
    '28': 'PlanVale',
    '29': 'GlobalPayments',
    '32': 'DMCard',
    '33': 'VeroCheque',
    '34': 'VR',
    '35': 'PoliCard',
    '36': 'ValeCard',
    '38': 'LiberCard',
    '39': 'GreenCard',
    '40': 'Discover',
    '41': 'JCB',
    '42': 'DaCasa',
    '43': 'Porto Seguro',
    '45': 'Adiq',
    '205': 'Nao Implementado',
    '206': 'Coopercard',
    '208': 'Sorocred',
    '210': 'InfinitePay',
    '209': 'FortBrasil'}



def serialize_data(line, line_num):
    line = line.strip('\n').split(';')
    try:
        if line_type[line[0]] == 'Header':
            data = {
                'type': line[0],
                'client_code': line[1],
                'hour': line[2],
                'date': datetime.strptime(line[3], '%Y%M%d'),
                'version': line[4],
                'uniqueid': line[5]
            }
            
        if line_type[line[0]] == 'Vendas':
            data = {
                'type': line[0],
                'sale_id': line[1],
                'cl_external_id': line[2],
                'cl_code': line[3],
                'stabilishment_id': line[4],
                'sale_date': datetime.strptime(line[5], '%Y%M%d'),
                'brute_value': float(line[6])/100,
                'transaction_type': table1[line[7]],
                'flag_code': table2[line[8]],
                'aq_code': table3[line[9]],
                'comp_num': line[10],
                'auth_code': line[11],
                'PDV': line[12],
                'parc_total': line[13],
                'desc': line[14],
                'hour': line[15],
                'card_num': line[16]
            }
        if line_type[line[0]] == 'Trailer':
            data = {
                'type': 9
            }
        return data
    except:
        return {'type': 'Erro', 'line_num': line_num}


class confere_data:
    def __init__(self,
        Host='sftp.confere.com.br',
        User='desafio',
        Port=22,
        Password='N2JiYTcwMGYzNTFiYjZmMTE3YjJlYmNk',
        Home='/confere-data/sftp-users/desafio',
        elog=False,
        log=False):
        client=paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if elog:
            print('Connecting to SFTP_SERVER')

        client.connect(Host, Port,  username=User,  password=Password)

        if elog:
            print('Connected to SFTP_SERVER')

        con = sqlite3.connect('data.db')
        cur = con.cursor() 
        cur.execute('''CREATE TABLE if not exists headers
                       (type int, client_code int, 
                       hour time, trans_date date, 
                       version text,uniqueid  text PRIMARY KEY)''')
        cur.execute('''DELETE FROM headers''')

        cur.execute('''CREATE TABLE if not exists transactions
                       (type int,sale_id int,
                        cl_external_id text, cl_code int,
                        stabilishment_id int,
                        sale_date date,
                        brute_value float,
                        transaction_type text,
                        flag_code text,
                        aq_code text,
                        comp_num int,
                        auth_code int,
                        PDV text,
                        parc_total int,
                        desc text,
                        hour time,
                        card_num text)''')
        cur.execute('''DELETE FROM transactions''')
        con.commit()
        self.cur = cur
        self.log = log
        self.elog = elog
        self.client = client
        self.update_files()
        self.__serializedata__()
        con.commit()
        con.close()

    def files(self):
        ftp = self.client.open_sftp()
        if self.elog:
            print('List of files in the server:')
        file_list = ftp.listdir()
        if self.elog:
            print(file_list)
        ftp.close()
        return file_list

    def update_files(self):
        ftp = self.client.open_sftp()
        files_updated = []

        if self.elog:
            print('\nDownloading files and updating them')

        for each in self.files():
            if each in os.listdir('downloads'):
                ex_cur_time = ftp.stat(each).st_mtime
                lc_cur_time = os.stat('downloads/'+each).st_mtime
            else:
                ex_cur_time = ftp.stat(each).st_mtime
                lc_cur_time = 0
            if ex_cur_time != lc_cur_time:
                if self.elog:
                    print('{} is being downloaded'.format(each))
                ftp.get(each, 'downloads/'+each)
                os.utime('downloads/'+each, (ex_cur_time, ex_cur_time))
                files_updated.append(each)
            else:
                if self.elog:
                    print('{} is already matching modified time with the server.'.format(each))

        ftp.close()
        return files_updated

    def __serializedata__(self):
        self.data = {}
        if self.elog:
            print('Processing csv files.')
        for file in os.listdir('downloads/'):
            data = []
            with open('downloads/'+file) as lines:
                i = 0
                for line in lines:
                    i+=1
                    dt = serialize_data(line, i)
                    data.append(dt)
                    if self.elog and data[-1]['type'] == 'Erro':
                        print('{} file line number {} has not been able to be processed'.format(file, i))
                    elif dt['type'] == '0':
                        self.cur.execute('''INSERT INTO headers VALUES  ("{}","{}","{}","{}","{}","{}");'''.format(dt['type'],dt['client_code'],
                dt['hour'],dt['date'],dt['version'],dt['uniqueid']))
                    elif dt['type'] == '1':
                        self.cur.execute('''INSERT INTO transactions VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''.format(
                dt['type'],dt['sale_id'],dt['cl_external_id'],dt['cl_code'],dt['stabilishment_id'],
                dt['sale_date'],dt['brute_value'],dt['transaction_type'],dt['flag_code'],dt['aq_code'],
                dt['comp_num'],dt['auth_code'],dt['PDV'],dt['parc_total'],dt['desc'],dt['hour'],dt['card_num']))

            self.data[file] = data
        if self.elog:
            print('All csvs processed')


    def to_file(self, name, file_name, file_type='w'):
        file = open('result/'+name, file_type)
        file.write(json.dumps(self.data[file_name],  indent=4,  sort_keys=True,  default=str))

    def all_files(self, filename='teste', multiple=True):
        if multiple:
            for each in self.data:
                self.to_file(each.replace('.csv', '.json'), each)
        else:
            for each in self.data:
                self.to_file(filename, each, file_type='a')

    def to_stdout(self):
        print(json.dumps(self.data,  indent=4,  sort_keys=True,  default=str))