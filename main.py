

# DON'T FORGET TO PUT YOUR DISCORD TOKEN BEFORE YOU RUN THE FILE

import discord
import requests
import json
from discord.ext import commands
from bs4 import BeautifulSoup as SOUP
import re
from keep_alive import keep_alive

BOT_PREFIX = ("?", "!")
# client = commands.Bot(command_prefix="!")
client = discord.Client()
client= commands.Bot(command_prefix="!")
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def bitcoin_exxchange():
	response = requests.get ("https://api.coindesk.com/v1/bpi/currentprice.json")
	data = response.json()
	bitcoin_price = float(data["bpi"]["USD"]["rate"].replace(",", ""))  # Bitcoin price in USD
	bitcoin_price = "$" + str(bitcoin_price)
	return bitcoin_price



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
	
	if message.author == client.user:
		return
	
	if message.content.startswith('$hello'): #if the message is $hello
		await message.channel.send("Hello!")	#return Hello!

	if message.content.startswith('$inspire'):
		hold = get_quote()
		await message.channel.send(hold)
	

	if message.content.startswith('$meme'):
		content = requests.get("https://meme-api.herokuapp.com/gimme").text
		data = json.loads(content,)
		meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
		await message.channel.send(embed=meme)
	
	if message.content.startswith('$instruction'):
		f = open('instructions.txt', 'r')
		await message.channel.send(f.read())


	if message.content.startswith('$dadjokes'):
		url = "https://icanhazdadjoke.com/"

		payload={}
		headers = {
		'Accept': 'application/json'
		}

		response = requests.request("GET", url, headers=headers, data=payload)
		response1 = json.loads(response.text)
		await message.channel.send(response1["joke"])

	

	if message.content.startswith('$family'):  
		count = 0
		urlhere = "http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Family Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1

	if message.content.startswith('$drama'):  
		#drama =  sad
		count = 0
		urlhere = "http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Drama Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1

	if message.content.startswith('$musical'):  
		count = 0
		urlhere = "http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Musical Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1
		
	
	if message.content.startswith('$thriller'):  

		#anger = $family_movies
		count = 0
		urlhere = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Thriller Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1

	if message.content.startswith('$sports'):  
		count = 0
		urlhere = "http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Sports Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1
	
	if message.content.startswith('$horror'):  
		count = 0
		urlhere = "https://www.imdb.com/search/title/?genres=horror&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Horror Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1
	
	if message.content.startswith('$action'):  
		count = 0
		urlhere = "https://www.imdb.com/search/title/?genres=action&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Action Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1

	if message.content.startswith('$adventure'):  
		count = 0
		urlhere = "https://www.imdb.com/search/title/?genres=adventure&title_type=feature&sort=moviemeter"
		payload={}
		headers = {
		'Accept': 'application/json'
		}
		response = requests.request("GET", urlhere, headers=headers, data=payload)
		data = response.text
		soup = SOUP(data, "lxml")
		title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

		for i in title:
			tmp = str(i).split('>')
			if count == 0:
				await message.channel.send("The Top 10 Adventure Movies are:")

			if(len(tmp) == 3):
				await message.channel.send(tmp[1][:-3])

			if(count > 25):
				break
			count += 1

	if message.content.startswith('$bitcoin'):
		safe = bitcoin_exxchange()
		await message.channel.send(safe)

keep_alive()
client.run("") #PUT YOUR TOKEN HERE (Guide to get the token is in the READ.ME file)
# client.run(os.getenv('TOKEN'))


