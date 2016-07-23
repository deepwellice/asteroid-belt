@echo off

SET OUTPUTTXT=%1
SET OUTPUTCLR=%2

SET OUTPUTTXT=%OUTPUTTXT:"=%

for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do ( set "DEL=%%a")
<nul set /p ".=%DEL%" > "%OUTPUTTXT%"
findstr /v /a:%OUTPUTCLR% /R "^$" "%OUTPUTTXT%" nul
if "%OUTPUTTXT%" NEQ "" if EXIST "%OUTPUTTXT%" del "%OUTPUTTXT%"
