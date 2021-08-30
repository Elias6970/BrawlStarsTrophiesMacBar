import pickle

class TagUtility():

	def upperTag(self,tag):
		tag=tag.replace("#","") 
		tag=tag.replace(" ","")
		tag=tag.upper()
		return tag

	def lowerTag(self,tag):
		tag=tag.replace("#","") 
		tag=tag.replace(" ","")
		tag=tag.lower()
		return tag

	def load(self):
		try:
			userTagFile=open("modulos/.extraInfo","rb")
			p=pickle.load(userTagFile)
			userTagFile.close()
			del(userTagFile)
		except:
			p=" "
		finally:
			return p

	def createTagFile(self,getTag):
		userTagFile=open("modulos/.extraInfo","wb")
		pickle.dump(getTag,userTagFile)
		userTagFile.close()
		del(userTagFile)
		

class showBrawlers():
	def showBrawlersName():
		pass