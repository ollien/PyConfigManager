import json
import os
import os.path

class ConfigManager():
	_cache = {}
	def __init__(self, configPath = "configs/"):
		if os.path.isdir(configPath):
			self.configPath = configPath
		else:
			raise IOError("Config Path does not eixst")
		self._configs = {}
		self._syncCache()
		self.getConfigs()

	def __getitem__(self, key):
		try:
			return self._configs[key]
		except KeyError:
			self.syncCache()
			return self._configs[key]

	#Recursive function to get all files. Sub is the relative path from the root config dir.	
	def getConfigs(self, path = None, sub = "", overrideCache = False):
		if path == None:
			path = self.configPath
		files = os.listdir(path)	
		for item in files:
			#Ignore hidden files.
			if item[0] == ".":
				continue

			#Remove the .json handle from the name
			name = item.replace(".json", "")
			finalPath = os.path.join(sub, name)

			#If it's a directory, run this function again within that directory
			if os.path.isdir(os.path.join(path, item)):
				self.getConfigs(path = os.path.join(path, item), sub = os.path.join(sub, item))
			#If we already have something from the cache, skip it.
			elif overrideCache or name not in self._configs:
				#Read in the file
				f = open(os.path.join(path, item), "r")
				#Check if it's JSON. If it is, it will be parsed.
				parsed = self.parseConfig(f.read())
				f.close()
				if parsed != None:
					self.addConfig(finalPath, parsed)

	#Returns parsed JSON if config is valid JSON, otherwise, return Noen	
	def parseConfig(self, config):
		try:
			return json.loads(config)
		except ValueError:
			return None
	
	def addConfig(self, name, contents):
		self._configs[name] = contents
		ConfigManager._cache[name] = contents
	
	def _syncCache(self):
		unmatchedKeys = [key for key in ConfigManager._cache.keys() if key not in self._configs]
		for key in unmatchedKeys:
			self._configs[key] = ConfigManager._cache[key]
