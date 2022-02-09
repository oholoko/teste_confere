import os
import paramiko

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

header = {
	'regiter_type':{'id':0,'format':'num'},
	'client_code':{'id':1,'format':'num'},
	'hour':{'id':2,'format':'hour'},
	'date':{'id':3,'format':'date'},
	'version':{'id':4,'format':'string'},
	'uniqueid':{'id':5,'format':'string'}
}

sales = {
	'type':{'id':0,'format':'num'},
	'sale_id':{'id':1,'format':'num'},
	'cl_external_id':{'id':2,'format':'num'},
	'cl_code':{'id':3,'format':'num'},
	'stabilishment_id':{'id':4,'format':'num'},
	'sale_date':{'id':5,'format':'date'},
	'brute_value':{'id':6,'format':'money'},
	'transaction_type':{'id':7,'format':'table1'},
	'flag_code':{'id':8,'format':'table2'},
	'aq_code':{'id':9,'format':'table3'},
	'comp_num':{'id':10,'format':'string'},
	'auth_code':{'id':11,'format':'num'},
	'PDV':{'id':12,'format':'string'},
	'parc_total':{'id':13,'format':'num'},
	'desc':{'id':14,'format':'string'},
	'hour':{'id':15,'format':'hour'},
	'card_num':{'id':16,'format':'text'}
}

table1 = {'1':'Depósito em conta',
	'2':'Débito Online',
	'3':'Benefício',
	'4':'Boleto Bancário',
	'5':'Cheque Pré',
	'6':'Cheque',
	'7':'Crédito Parcelado',
	'8':'Crédito à Vista',
	'9':'Débito',
	'10':'Dinheiro',
	'11':'Outros',
	'12':'Repasse de Terceiro',
	'13':'Transferência entre Contas'}

table2 = {
	'1':'Master',
	'2':'Visa',
	'3':'Amex',
	'4':'Diners',
	'5':'Jcb',
	'6':'Discover',
	'7':'Elo',
	'8':'Aura',
	'9':'Hipercard',
	'10':'Cabal',
	'11':'Sorocred',
	'12':'Cup',
	'13':'Credsystem',
	'14':'Sicredi',
	'15':'VR',
	'16':'Ticket',
	'17':'Alelo',
	'18':'Avista',
	'19':'Bancred Card',
	'20':'Banestes',
	'21':'Bib Club',
	'22':'Big Card',
	'23':'Calcard',
	'24':'Cooper',
	'25':'Good Card',
	'26':'Greencard',
	'27':'Hiper',
	'28':'Mais!',
	'29':'Maxx Card',
	'30':'Minas Cred',
	'31':'Novocard',
	'33':'Outro',
	'34':'Plan',
	'35':'Policard',
	'36':'Praticard',
	'37':'Sodexo',
	'38':'Softnext',
	'39':'Syspro Card',
	'40':'Unik',
	'41':'Union Pay',
	'42':'Vb',
	'43':'Verde Card',
	'44':'Verocheque',
	'45':'Visa Vale',
	'46':'Brasilcard',
	'47':'Fortbrasil',
	'48':'Grandcard',
	'49':'Personalcard',
	'50':'Valecard',
	'51':'Credz',
	'52':'Agiplan',
	'53':'Esplanada',
	'54':'ConectCar',
	'55':'Sem Parar',
	'57':'Banescard',
	'58':'PagSeguro',
	'59':'Dacasa',
	'60':'Porto Seguro',
	'61':'Ticket - Ref.',
	'62':'Ticket - Alim.',
	'63':'Vr - Ref.',
	'64':'Vr - Alim.',
	'65':'Sodexo - Ref.',
	'66':'Sodexo - Alim.',
	'67':'Alelo Ref.',
	'68':'Alelo Alim.',
	'69':'Alelo Auto',
	'81':'Bandeira não identificada',
	'70':'Vr - Auto',
	'71':'Vr - Cultura',
	'72':'Vr - Cartão da mamãe',
	'73':'Sodexo - Premium Pass',
	'74':'Sodexo - Gift Pass',
	'75':'Sodexo - Mobility Pass Carro',
	'79':'Sodexo - Cultura Pass',
	'82':'Ourocard',
	'84':'BanriCard',
	'83':'Banricompras',
	'93':'Nutricash',
	'85':'Senff',
	'89':'Greencard - Alim.',
	'90':'Greencard - Ref.',
	'91':'Alelo Cult.',
	'92':'Alelo multi.',
	'94':'Banco do Brasil',
	'95':'Mercado Pago',
	'98':'Solucard',
	'99':'VSCard',
	'100':'Construcard',
	'96':'Flex Car Visa Vale',
	'97':'Tricard',
	'101':'Bradesco',
	'103':'Ticket Cultura'}

table3 = {'2':'Rede',
	'56':'Sicredi',
	'57':'Pago',
	'58':'Vero',
	'59':'SafraPay',
	'60':'Tribanco',
	'61':'Adyen',
	'62':'Unicred',
	'195':'Pop Credicard',
	'196':'Senff',
	'64':'Nutricash',
	'200':'Adquirente indefinido',
	'197':'MercadoPago',
	'201':'Tricard',
	'202':'Unica',
	'204':'Mercado Livre',
	'1':'Cielo',
	'3':'Amex',
	'4':'Getnet',
	'5':'Aura',
	'6':'Ticket',
	'7':'Sodexo',
	'8':'Elavon',
	'9':'Bin',
	'10':'Stone',
	'23':'PagSeguro',
	'24':'Alelo',
	'25':'Hipercard',
	'26':'Banricompras',
	'27':'GoodCard',
	'28':'PlanVale',
	'29':'GlobalPayments',
	'32':'DMCard',
	'33':'VeroCheque',
	'34':'VR',
	'35':'PoliCard',
	'36':'ValeCard',
	'38':'LiberCard',
	'39':'GreenCard',
	'40':'Discover',
	'41':'JCB',
	'42':'DaCasa',
	'43':'Porto Seguro',
	'45':'Adiq',
	'205':'Nao Implementado',
	'206':'Coopercard',
	'208':'Sorocred',
	'210':'InfinitePay',
	'209':'FortBrasil'}



def serialize_data(line):
	if line_type[line[0]] == 'Header':
		return {'tipo'}
	if line_type[line[0]] == 'Vendas':


class confere_data:
	def __init__(self,
		Host='sftp.confere.com.br',
		User='desafio',
		Port=22,
		Password='N2JiYTcwMGYzNTFiYjZmMTE3YjJlYmNk',
		Home='/confere-data/sftp-users/desafio'):
		client=paramiko.SSHClient()

		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		client.connect(Host,Port, username=User, password=Password)

		self.client = client
		self.update_files()
		self.__serializedata__()

	def files(self):
		ftp = self.client.open_sftp()
		file_list = ftp.listdir()
		ftp.close()
		return file_list

	def update_files(self):
		ftp = self.client.open_sftp()
		files_updated = []

		for each in self.files():
			ex_cur_time = ftp.stat(each).st_mtime
			lc_cur_time = os.stat('downloads/'+each).st_mtime
			if ex_cur_time != lc_cur_time:
				ftp.get(each,'downloads/'+each)
				os.utime('downloads/'+each,(ex_cur_time,ex_cur_time))
				files_updated.append(each)

		ftp.close()
		return files_updated

	def update_file(self,filename):
		ftp = self.client.open_sftp()
		ftp.get(filename,'downloads/'+filename)
		os.utime('downloads/'+filename,(ex_cur_time,ex_cur_time))
		ftp.close()
		return 'File updated'

	def __serializedata__(self):
		for each in os.listdir('downloads/'):
			with open('downloads/'+each) as file:
				

confere_data()