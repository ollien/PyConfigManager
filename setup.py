import distutils.core

setupArgs = {
	"name": "PyConfigManager",
	"version": "1.0",
	"description": "A JSON config manager for your JSON configs",
	"author": "Nick Krichevsky",
	"author_email": "nick@ollien.com",
	"packages": ["configmanager"]
}

distutils.core.setup(**setupArgs)
