@echo off
rem This file was generated by Fluent.  To kill Fluent and all its
rem related processes, run this script.  If Fluent exits normally
rem this file will be removed automatically.

set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v212\fluent\\ntbin\\win64\\winkill.exe "

echo Killing node process 9556...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 9556) else ( CASL5CD952DBRR %KILL_CMD% 9556)
echo Killing node process 8528...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 8528) else ( CASL5CD952DBRR %KILL_CMD% 8528)
echo Killing node process 10408...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 10408) else ( CASL5CD952DBRR %KILL_CMD% 10408)
echo Killing node process 14752...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 14752) else ( CASL5CD952DBRR %KILL_CMD% 14752)
echo Killing node process 11184...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 11184) else ( CASL5CD952DBRR %KILL_CMD% 11184)
echo Killing node process 8960...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 8960) else ( CASL5CD952DBRR %KILL_CMD% 8960)
echo Killing node process 13340...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 13340) else ( CASL5CD952DBRR %KILL_CMD% 13340)
echo Killing node process 16476...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 16476) else ( CASL5CD952DBRR %KILL_CMD% 16476)
echo Killing host process...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 16308) else ( CASL5CD952DBRR %KILL_CMD% 16308)
echo Killing cortex process...
if /i "%LOCALHOST%"=="CASL5CD952DBRR" (%KILL_CMD% 2320) else ( CASL5CD952DBRR %KILL_CMD% 2320)
del /q "C:\Users\SammaV\Documents\GitHub\Fluent_No_GUI\\cleanup-fluent-CASL5CD952DBRR-2320.bat"