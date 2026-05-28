@echo off
chcp 65001 >nul
cls

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║     🛡️  金融詐騙偵測系統 - 啟動程式              ║
echo ╚════════════════════════════════════════════════════════╝
echo.
echo ⏳ 正在安裝必要的套件，請稍候...
echo 這可能需要 2-3 分鐘...
echo.

python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ 安裝失敗！
    echo.
    echo 可能的原因：
    echo 1. 沒有安裝 Python
    echo 2. Python 不在系統路徑中
    echo.
    echo 請試著：
    echo - 重新安裝 Python (記得勾選 Add Python to PATH)
    echo - 或聯絡技術人員
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ 套件安裝完成！
echo.
echo 🚀 正在啟動網站...
echo.
echo ════════════════════════════════════════════════════════
echo 📍 網站地址: http://localhost:5000
echo ════════════════════════════════════════════════════════
echo.
echo ⏹️  按 CTRL+C 可以停止程式
echo.
echo 稍候 5 秒鐘自動打開瀏覽器...
echo.

timeout /t 5

REM 嘗試自動打開瀏覽器
start http://localhost:5000

REM 啟動 Flask 應用
python app.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ 啟動失敗！
    echo.
    pause
    exit /b 1
)
