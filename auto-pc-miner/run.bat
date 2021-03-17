if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
    setlocal
    cd /d %~dp0
    python3 %~dp0/src/app.py
    pause
exit