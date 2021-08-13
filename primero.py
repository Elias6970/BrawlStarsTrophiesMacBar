import requests
import rumps

headers = { 
		'Accept':'application/json',
		'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRiYWYwMTYyLTNiYTMtNGUwYy1iYjUzLTU4NzY5MGRiZDA4YiIsImlhdCI6MTYyODE3OTI1OSwic3ViIjoiZGV2ZWxvcGVyLzIwNDViNWM5LTVmNmItMGExMi01OGM3LTZhNTdkYTEzMmIzYyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4Ljc5LjkzLjE4MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ._6ns5QySk6rt0zYt1IJQTZ6rFmJws1PAGMJr2rWuctstqxu_outDcSciif3p7ePSuXzJjGonkQTNHiZdZcnQjg'
		}

class AwesomeStatusBarTrophiesBar(rumps.App):
	def __init__(self):
		super(AwesomeStatusBarTrophiesBar, self).__init__("Elias6970")
		self.menu=["Querying API..."]
		self.menu=["J"]

	@rumps.timer(10)
	def trophies(self, _):
		uResponse = requests.get("https://api.brawlstars.com/v1/players/%23uqly00ur", headers=headers)
		userJson = uResponse.json()
		print(userJson["trophies"])
		self.title="Elias6970: "+str(uResponse.json()["trophies"])

if __name__=="__main__":
	AwesomeStatusBarTrophiesBar().run()