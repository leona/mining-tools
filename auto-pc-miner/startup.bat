SCHTASKS /CREATE /SC ONSTART /TN "MyTasks\AutoMiner task" /TR "%~dp0/run.bat"
pause