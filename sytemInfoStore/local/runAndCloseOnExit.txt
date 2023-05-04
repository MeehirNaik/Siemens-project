@echo off

REM Start local server
echo Starting local server...
start /b python -m http.server 8000

REM Wait for server to start
timeout 1 > nul

REM Open test.html file in browser
echo Opening test.html file in browser...
start "" "http://localhost:8000/test.html"

REM Wait for user to close browser or command prompt window
echo Press any key to stop the local server and close this window...
set /p dummy=
taskkill /f /im python.exe > nul

