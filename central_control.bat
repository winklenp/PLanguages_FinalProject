Covid_Spread.exe

set size=0
:while
for /f %%i in ("quit.txt") do set size=$$~zi
    if %size%==0
        (
        set size=0

        for /f %%i in ("start_form.txt") do set size=%%~zi
        if %size% gtr 0 python main.py

        echo "" > start_form.txt

        set size=0

        for /f %%i in ("start_prolog.txt") do set size=%%~zi
        if %size% gtr 0 prolog.p1

        echo "" > start_prolog.txt

        set size=0

        for /f %%i in ("start_haskell.txt") do set size=%%~zi
        if %size% gtr 0 haskell.h1

        echo "" > start_haskell.txt

        set size=0
        goto:while
        )
    else goto:eof


