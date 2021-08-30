import requests
import rumps
import pickle
from modulos.utility import*

headers = { 
		"Accept":"application/json",
		"authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhjMWI5NGY1LWUxYTUtNDgxNC04OTQ3LTY1YzI2ZTI4ZmI1ZCIsImlhdCI6MTYzMDI2NjU0Mywic3ViIjoiZGV2ZWxvcGVyLzIwNDViNWM5LTVmNmItMGExMi01OGM3LTZhNTdkYTEzMmIzYyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4Ljc5LjkyLjE4OSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.bhf1rePUagOJnD8tK82NMAaasPv8AD8hP1L-EPz9ZlmCsSlNzkJEYw1epWEXyIq6Ygg2GVOAdjg0skoCvobG-g"
		}


#La IP no es la correcta respecto a la key de la api por eso no se puede conectar al server (error 403)

#TODO:




#-------------------------------------Debug Mode------------------------------------------------------------
#rumps.debug_mode(True)
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------APP---------------------------------------------------------------


class AwesomeStatusBarTrophiesBar(rumps.App,TagUtility):
	def __init__(self):
		super(AwesomeStatusBarTrophiesBar, self).__init__("Bs App")

		self.quit_button=None
		#No poner el mismo nombre a las variableque a las palabras clave de los diccionarios porque da error
		#---Menu Items-----
		self.quitButton=rumps.MenuItem("Quit")
		self.userTag=rumps.MenuItem("Tag: Uknown")
		self.username=rumps.MenuItem("Name: Unkown")
		self.userTrophies=rumps.MenuItem("Trophies: Uknown")
		self.club=rumps.MenuItem("Club: Uknown")
	
	#-----------------------------------------------------------------------------------
	
	apiInfo="a"
	tag=" "#Tag
	@rumps.timer(3000)
	def searchExternalInfo(self, _): #search the tag in external file
		
		tag=str(self.load())
		
		if tag!=" ":
			self.createMenuItems()
			self.userTag.title=str("Tag: #"+self.upperTag(tag)) 
		else:
			pass
	

   #-------------------------------------------------------------------------------------------------
   #|									QUIT BUTTON 						       				    |
   #-------------------------------------------------------------------------------------------------		
		
	@rumps.clicked("Quit")
	def quitButtonF(self, _):
		rumps.quit_application()

	
	#-------------------------------------------------------------------------------------------------
	#|						        	CONNECT WITH THE BS API                                      |
	#-------------------------------------------------------------------------------------------------
	
	@rumps.timer(5)
	def urlRefresh(self, _):
		if self.load()!=" ":
			uResponse = requests.get("https://api.brawlstars.com/v1/players/%23"+self.load(), headers=headers)
			#uResponse = requests.get("https://api.brawlstars.com/v1/players/%23uqlyoour", headers=headers)
		else:
			uResponse = requests.get("https://api.brawlstars.com/v1/players/%23"+self.load(), headers=headers)

		userJson = uResponse.json()
		
		
		self.apiInfo=userJson

   #---------------------------------------------------------------------------------------------------
   #|                          			CREATE THE MENU ITEMS 			       		 	              |
   #--------------------------------------------------------------------------------------------------- 

	def createMenuItems(self):
		self.menu.add(self.userTag)
		self.menu.add(self.username)
		self.menu.add(self.userTrophies)
		self.menu.add(self.club)
		brawlers123=rumps.MenuItem("Brawlers")
		brawlers123.set_callback(lambda _:self.showBrawlers())
		self.menu.add(brawlers123)



   #---------------------------------------------------------------------------------------------------
   #|                          			SAVE USER TAG  					       		 	              |
   #---------------------------------------------------------------------------------------------------

	@rumps.clicked("Tag Config")
	def preferences(self, _):
		getTag=rumps.Window(title="Config",message="Put your brawl stars TAG",dimensions=(110,25)).run()
		getTag=getTag.text

		self.userTag.title=str("Tag: #"+self.upperTag(getTag)) #Mostrar tag menu
		tag=self.lowerTag(getTag) #guardar tag en la variable tag

		

		self.createTagFile(getTag) 
		self.createMenuItems() 
	

	#-------------------------------------------------------------------------------------------------
	#|											SHOW THE ITEMS										 |
	#-------------------------------------------------------------------------------------------------
	@rumps.timer(5)
	def rename(self, _):
		

		name=str(self.apiInfo["name"])
		trophies1=str(self.apiInfo["trophies"])
		clubName=str(self.apiInfo["club"].get("name"))
		
		
		self.title=name+":"+trophies1
		self.username.title="Name: "+name
		self.userTrophies.title="Trophies: "+trophies1
		
		if self.apiInfo["club"].get("name")==None:
			self.club.title="You don't have club"
		else:
			self.club.title="Club: "+clubName
		#-----------------Brawlers----------------
		"""lista=[]
		for i in self.apiInfo["brawlers"]:
			lista.append(i["name"])
		
		
		brawlr=rumps.MenuItem("Your brawlers")

		self.menu=[
		(brawlr,(lista[:]))
		]"""

	def showBrawlers(self):
		rumps.alert(message='something', ok='YES!', cancel='NO!')


if __name__=="__main__":
	AwesomeStatusBarTrophiesBar().run()
