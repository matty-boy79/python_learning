import platform

x = platform.system()
print(x)  # prints "Windows" or "MacOS" or whatever

y = dir(platform)
print(y)  # lists all defined names belonging to the platform module
