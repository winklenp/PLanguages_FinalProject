covidspread.exe

set size=0
for /f %%i in ("start_form.txt") do set size=%%~zi
if %size% gtr 0 python main.py

