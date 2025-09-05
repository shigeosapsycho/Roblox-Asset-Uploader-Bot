import requests
import time
import sys
import os
os.system("color 0b")

print ("   ")
print ("   ")
print ("   ")
print ("############################################################################")
print ("#Googledmusics sexy version                                                #")
print ("#This is a Special bot for googledmusic                                    #")
print ("#If u don't know how this work pm me                                       #")
print ("#Discord link https://discord.gg/k9Qsxt                                    #")
print ("#don't leak this or u stupid lol                                           #")
print ("############################################################################")
print ("   ")
print ("   ")

class RobloxBot:
	
	def __init__(self, group_id):
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
		self.session = requests.session()
		self.session.headers.update(self.headers)
		self.group_id = group_id
		if requests.get('https://pastebin.com/raw/xxzsCPH2').text != 'If you are looking at this you are a skid from visilex':
			sys.exit('Unable to connect')

	def login(self, username, password):
		print('playing music')
		payload = {'username': username, 'password': password}
		self.session.post('https://www.roblox.com/newlogin', data=payload)
		print('played music')

	def get_shirts(self, starting_page=66, category='12', wait=10):
		page_num = starting_page
		while page_num < 999999:
			params = {'CatalogContext': 66, 'Subcategory': category, 'SortAggregation': '5', 'LegendExpanded': 'true', 'Category': '3', 'PageNumber': page_num}
			try:
				r = self.session.get('https://www.roblox.com/catalog/json', params=params)
				r.raise_for_status()
			except requests.exceptions.HTTPError:
				print('Status Error: {}'.format(r.status_code))
				time.sleep(30)
				continue
			for asset in r.json():
				while True:
					try:
						self.__download(asset['AssetId'])
						break
					except:
						print('Found an error. Retrying.')
						continue
				time.sleep(wait)
			page_num += 1

	def __download(self, assetId):
		data = self.session.get('https://api.roblox.com/Marketplace/ProductInfo', params={'assetId': assetId}).json()
		name, description, price, asset_type = data['Name'], data['Description'], data['PriceInRobux'], data['AssetTypeId']
		count = 0
		while count < 10:
			assetId -= 1
			try:
				r = self.session.get('https://api.roblox.com/Marketplace/ProductInfo', params={'assetId': assetId})
				count += 1
				r.raise_for_status()
				if r.json()['Name'] == name:
					break
			except (requests.exceptions.HTTPError, ValueError):
				return
		else:
			print('Could not find template for: {}'.format(assetId))
			return
		file = self.session.get('https://www.roblox.com/asset/', params={'id': assetId})
		self.__upload(name, description, price, file, asset_type, assetId)

	def __upload(self, name, description, price, file, asset_type, assetId):
		r = self.session.get('https://www.roblox.com/build/upload')
		token = r.text.split('name=__RequestVerificationToken type=hidden value=')[-1].split('>')[0]
		data = {'file': ('template.png', file.content, 'image/png')}
		payload = {'__RequestVerificationToken': token, 'assetTypeId': asset_type, 'isOggUploadEnabled': 'True', 'isTgaUploadEnabled': 'True', 'groupId': self.group_id, 'onVerificationPage': 'False', 'name': name}
		r = self.session.post('https://www.roblox.com/build/upload', files=data, data=payload)
		asset_id = r.text.split('uploadedId=')[-1].split('" />')[0]
		assets = {'id': asset_id}
		r = self.session.get('https://www.roblox.com/my/item.aspx', params=assets)
		view_state = r.text.split('id="__VIEWSTATE" value="')[-1].split('" />')[0]
		view_gen = r.text.split('id="__VIEWSTATEGENERATOR" value="')[-1].split('" />')[0]
		validation = r.text.split('id="__EVENTVALIDATION" value="')[-1].split('" />')[0]
		payload = {'__EVENTTARGET': 'ctl00$cphRoblox$SubmitButtonBottom', '__EVENTARGUMENT': '', '__VIEWSTATE': view_state, '__VIEWSTATEGENERATOR': view_gen, '__EVENTVALIDATION': validation, 'ctl00$cphRoblox$NameTextBox': name, 'ctl00$cphRoblox$DescriptionTextBox': description, 'ctl00$cphRoblox$SellThisItemCheckBox': 'on', 'ctl00$cphRoblox$SellForRobux': 'on', 'ctl00$cphRoblox$RobuxPrice': price, 'ctl00$cphRoblox$EnableCommentsCheckBox': 'on', 'GenreButtons2': '1', 'ctl00$cphRoblox$actualGenreSelection': '1'}
		self.session.post('https://www.roblox.com/my/item.aspx', params=assets, data=payload)
		print('Successfull'.format(assetId))

if __name__ == '__main__':
	bot = RobloxBot(group_id='3815292')
	bot.login(username='GoogledMusicYT', password='googledishot')
	bot.get_shirts(starting_page=1, category='14', wait=3)
