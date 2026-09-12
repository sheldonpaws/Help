#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Запуск всех скриптов диагностики диска
"""
import subprocess
import sys
import os

def run_script(script_name):
    """Запускает указанный скрипт."""
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if not os.path.exists(script_path):
        print(f"❌ Скрипт не найден: {script_path}")
        return False
    
    print(f"\n{'='*70}")
    print(f"▶ ЗАПУСК: {script_name}")
    print('='*70)
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=False,
            encoding='utf-8',
            errors='replace'
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Ошибка запуска: {e}")
        return False

def main():
    scripts = [
        "system_files_size.py",
        "disk_usage_root.py",
        "user_folder_analysis.py",
        "temp_files_check.py",
        "restore_points_check.py",
    ]
    
    print("=" * 70)
    print("КОМПЛЕКСНАЯ ДИАГНОСТИКА ДИСКА C:")
    print("=" * 70)
    print("\nРекомендуется запуск от имени администратора для полного доступа.\n")
    
    results = {}
    for script in scripts:
        results[script] = run_script(script)
    
    print("\n" + "=" * 70)
    print("ИТОГИ ДИАГНОСТИКИ")
    print("=" * 70)
    
    for script, success in results.items():
        status = "✓ Успешно" if success else "❌ Ошибка"
        print(f"{script:<35} {status}")
    
    print("=" * 70)
    print("\n💡 Рекомендации:")
    print("1. Если pagefile.sys или hiberfil.sys занимают много места —")
    print("   можно настроить их размер в параметрах системы.")
    print("2. Временные файлы можно безопасно очистить.")
    print("3. OneDrive можно отключить, если не используется.")

if __name__ == "__main__":
    # Проверка прав администратора
    import ctypes
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            print("⚠ ВНИМАНИЕ: Скрипт запущен НЕ от имени администратора.")
            print("   Некоторые данные могут быть недоступны.\n")
    except:
        pass
    
    main()
