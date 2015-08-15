import json
import os
import os.path

class ConfigManager():
	def __init__(self, configPath = "configs/"):
		if os.path.isdir(configPath):
			self.configPath = configPath
		else:
			raise IOError("Config Path does not eixst")
		self.configs = {}
		self.getConfigs()

	#Recursive function to get all files. Sub is the relative path from the root config dir.	
	def getConfigs(self, path = None, sub = ""):
		if path == None:
			path = self.configPath
		files = os.listdir(path)	
		for item in files:
			if os.path.isdir(os.path.join(path, item)):
				self.getConfigs(path = os.path.join(path, item), sub = os.path.join(sub, item))
			else:
				f = open(os.path.join(path, item), "r")
				parsed = self.parseConfig(f.read())
				f.close()
				if parsed != None:
					name = item.replace(".json", "")
					finalPath = os.path.join(sub, name)
					self.configs[finalPath] = parsed
		
	def parseConfig(self, config):
		try:
			return json.loads(config)
		except ValueError:
			return None
