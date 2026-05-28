#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fraud Detection Website - Complete Launcher
自動解決所有問題
"""

import subprocess
import sys
import os
import webbrowser
import time
import platform

def clear_screen():
    """清空螢幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """打印標題"""
    print("\n" + "="*70)
    print("           🛡️  詐騙偵測網站 - 一鍵啟動")
    print("="*70 + "\n")

def check_python():
    """檢查 Python 版本"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 版本太舊（需要 3.7 以上）")
        print(f"   目前版本: {version.major}.{version.minor}")
        return False
    print(f"✅ Python 版本: {version.major}.{version.minor}.{version.micro}")
    return True

def check_requirements_file():
    """檢查 requirements.txt 是否存在"""
    if not os.path.exists('requirements.txt'):
        print("❌ 找不到 requirements.txt 檔案")
        print(f"   目前位置: {os.getcwd()}")
        return False
    print("✅ 找到 requirements.txt")
    return True

def install_dependencies():
    """安裝依賴套件"""
    print("\n⏳ 正在安裝依賴套件...")
    print("   (Flask, pandas, scikit-learn)")
    print("   這可能需要 2-3 分鐘...\n")
    
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("✅ 依賴套件安裝完成！\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 安裝失敗: {e}")
        return False

def check_app_file():
    """檢查 app.py 是否存在"""
    if not os.path.exists('app.py'):
        print("❌ 找不到 app.py 檔案")
        return False
    print("✅ 找到 app.py")
    return True

def start_website():
    """啟動網站"""
    print("="*70)
    print("                    🚀 啟動中...")
    print("="*70)
    print("\n📍 網站地址: http://localhost:5000")
    print("📍 網站地址: http://127.0.0.1:5000")
    print("\n💡 提示: 按 CTRL+C 可以停止網站\n")
    print("⏳ 5 秒後自動打開瀏覽器...\n")
    
    time.sleep(5)
    
    try:
        webbrowser.open('http://localhost:5000')
    except Exception as e:
        print(f"⚠️  無法自動打開瀏覽器: {e}")
        print("   請手動打開: http://localhost:5000\n")
    
    try:
        subprocess.call([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n\n✅ 網站已停止。再見！")
        sys.exit(0)

def main():
    """主程式"""
    clear_screen()
    print_header()
    
    # 檢查清單
    print("📋 檢查清單:\n")
    
    if not check_python():
        input("\n按 Enter 結束...")
        sys.exit(1)
    
    if not check_requirements_file():
        input("\n按 Enter 結束...")
        sys.exit(1)
    
    if not check_app_file():
        input("\n按 Enter 結束...")
        sys.exit(1)
    
    # 安裝依賴
    if not install_dependencies():
        input("\n❌ 安裝失敗，按 Enter 結束...")
        sys.exit(1)
    
    # 啟動網站
    start_website()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        input("\n按 Enter 結束...")
        sys.exit(1)
