@echo off
cls
echo Starting Fraud Detection Website...
echo Please wait...
echo.

python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Installation failed!
    echo Please make sure Python is installed.
    pause
    exit /b 1
)

echo Installation complete!
echo.
echo Starting website...
echo Website URL: http://localhost:5000
echo.
echo Press CTRL+C to stop
echo.

timeout /t 3

start http://localhost:5000

python app.py

pause
