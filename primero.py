import requests
import rumps

headers = { 
		'Accept':'application/json',
		'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRiYWYwMTYyLTNiYTMtNGUwYy1iYjUzLTU4NzY5MGRiZDA4YiIsImlhdCI6MTYyODE3OTI1OSwic3ViIjoiZGV2ZWxvcGVyLzIwNDViNWM5LTVmNmItMGExMi01OGM3LTZhNTdkYTEzMmIzYyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4Ljc5LjkzLjE4MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ._6ns5QySk6rt0zYt1IJQTZ6rFmJws1PAGMJr2rWuctstqxu_outDcSciif3p7ePSuXzJjGonkQTNHiZdZcnQjg'
		}

#-------------------------------------Debug Mode------------------------------------------------------------
#rumps.debug_mode(True)
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------APP---------------------------------------------------------------


class AwesomeStatusBarTrophiesBar(rumps.App):
	def __init__(self):

		super(AwesomeStatusBarTrophiesBar, self).__init__("Bs App")
		self.quit_button=None

		self.userInfoJson="a"
		self.tag=""#Tag

		#--------------Normal Menu-------------------------------------------------------------
		#No poner el mismo nombre a las variableque a las palabras clave de los diccionarios porque da error
		
		
		self.quitButton=rumps.MenuItem("Quit")
		self.userTag=rumps.MenuItem("Tag: Uknown")
		self.username=rumps.MenuItem("Name: Unkown")
		self.userTrophies=rumps.MenuItem("Trophies: Uknown")
		self.club=rumps.MenuItem("Club: Uknown")
		
		


		#------------Sub Menu-------------------------------------------------------------------
		
		#self.menu=[
		#rumps.MenuItem("Brawlers:",dimensions=(18,18)),[rumps.MenuItem("Uno"),rumps.MenuItem("dos")
		#(self.brawlers2,(self.lista))
		




#-------------------------------------------------------------------------------------------------
#|											QUIT BUTTON 										 |
#-------------------------------------------------------------------------------------------------		
		
	@rumps.clicked("Quit")
	def quitButtonF(self, _):
		rumps.quit_application()


#-------------------------------------------------------------------------------------------------
#|											SHOW THE ITEMS										 |
#-------------------------------------------------------------------------------------------------
	@rumps.timer(5)
	def rename(self, _):
		
		uResponse = requests.get("https://api.brawlstars.com/v1/players/%23"+self.tag, headers=headers)
		userJson = uResponse.json()
		self.userInfoJson=userJson

		name=str(userJson["name"])
		trophies1=str(userJson["trophies"])
		clubName=str(userJson["club"].get("name"))
		
		
		self.title=name+":"+trophies1
		self.username.title="Name: "+name
		self.userTrophies.title="Trophies: "+trophies1
		
		if userJson["club"].get("name")==None:
			self.club.title="You don't have club"
		else:
			self.club.title="Club: "+clubName
		#-----------------Brawlers----------------
		
			

#---------------------------------------------------------------------------------------------------
#|                          GET USER TAG  AND CREATE THE MENU ITEMS                                |
#---------------------------------------------------------------------------------------------------
	

	@rumps.clicked("Tag Config")
	def preferences(self, _):
		getTag=rumps.Window(title="Config",message="Put your brawl stars TAG",dimensions=(110,25)).run()
		getTag=getTag.text
		getTag=getTag.upper()
		self.userTag.title=str("Tag: #"+getTag)
		getTag=getTag.replace("#","") 
		getTag=getTag.replace(" ","")
		getTag=getTag.lower()
		self.tag=str(getTag)

		self.menu.add(self.userTag)
		self.menu.add(self.username)
		self.menu.add(self.userTrophies)
		self.menu.add(self.club)
		print("1")
		print(str(self.userInfoJson["brawlers"]))
		lista=[]
		for i in self.userInfoJson["brawlers"]:
			lista.append(i["name"])

		print(lista[:])

		self.menu=[
		("Your brawlers",(lista[:]))
		]

		
	

	
		
	










	
#---------Refrescar y poner los brawlers que tienes-----------


	"""@rumps.clicked("Refresh") 
	def brawlersRefresh(self, _):
		lista=[]
		for i in self.userInfoJson["brawlers"]:
			lista.append(i["name"])
			
		self.menu=[
		("Your brawlers",(lista[:]))
		]
		

"""



if __name__=="__main__":
	AwesomeStatusBarTrophiesBar().run()
