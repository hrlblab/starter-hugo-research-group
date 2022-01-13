import os

os.system('hugo')
os.system('cd public')
os.system('git config core.autocrlf true')
os.system('git add .')
os.system('git commit -m "update"')
os.system('git push origin master')
os.system('cd ..')
