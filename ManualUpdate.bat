@ECHO OFF
cd Python
.\env\Scripts\python.exe UpdateConfigFile.py
cd ..
mkdir tally
cd Python
.\env\Scripts\python.exe CreateInoFile.py