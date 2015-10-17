# PyConfigManager

A quick way to manage your JSON Configs. 

If we have a folder structure of 
```
config/
  config.json
  web/
    server.json
  db/
    connection.json
```
we can easily manage it! All you need to do is install pyconfigmanager using 

```
python setup.py install
```
and add this code to your project.

```py
import configmanager
configs = configmanager.ConfigManager()
#Say we want to access config/config.json. 
rootConfig = configs["config"]
#It's as simple as that! What if we want to access config/web/server.json? Simple! 
serverConfig = configs["web/server"]
#This can go as many directories deep as you want, of course.
```

That's all you need to get a config system all setup for your project!
