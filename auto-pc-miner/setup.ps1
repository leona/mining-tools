[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe" -OutFile "c:/temp/python-3.9.0.exe"
C:/temp/python-3.9.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
$current_path=Split-Path -parent $PSCommandPath
cmd /c python3 -m pip install -r $current_path/requirements.txt
cmd /c pause