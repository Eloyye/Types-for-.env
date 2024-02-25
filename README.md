# Type Safety for env.process using *Typescript* and *File Watchers*

# Aim of this program
This program aims to provide static types for keys in .env files so that they can
be used in intellisense in your favorite IDE.

# Requirements
1. python 3.8

# How to use using any Jetbrains IDE:
1. clone this repo
2. go to settings > "file watchers" > add 
3. In program field:
```
path/to/python/executable
```
4. In arguments field: 
```
absolute/path/to/main.py .env
``` 
5. Uncheck "Auto-save edited files..." 
6. Create .env file in project directory
