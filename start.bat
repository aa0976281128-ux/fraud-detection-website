@echo off
chcp 65001 >nul
echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║     🛡️  金融詐騙偵測系統 - 啟動程式              ║
echo ╚════════════════════════════════════════════════════════╝
echo.
echo ⏳ 正在安裝必要的套件，請稍候...
echo.

python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ 安裝失敗！
    echo 請確認已安裝 Python
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ 套件安裝完成！
echo.
echo 🚀 正在啟動網站...
echo.
echo 📍 網站地址: http://localhost:5000
echo.
echo ⏹️  按 CTRL+C 可以停止程式
echo.

python app.py

pause
