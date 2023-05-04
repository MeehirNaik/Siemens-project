@echo off
REM Start local server
echo Starting local server...
start /b python -m http.server 8000

REM Wait for server to start
timeout 1 > nul

REM Open index.html file in browser
echo Opening index.html file in browser...
start "" "http://localhost:8000/index.html"

REM Wait for user to close browser
echo Press any key to stop the local server and close this window...
pause > nul

REM Stop local server
echo Stopping local server...
taskkill /f /im python.exe > nul
