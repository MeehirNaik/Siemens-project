@echo off

setlocal

set http_port=8000
set browser_cmd="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

echo Starting server on port %http_port%
start /min python -m http.server %http_port%

echo Waiting for server to start...
ping -n 1 127.0.0.1 > nul

echo Opening test.html in browser...
%browser_cmd% "http://localhost:%http_port%/test.html"

echo Press any key to stop server and close this window...
pause > nul

echo Stopping server...
taskkill /f /im python.exe > nul

endlocal
