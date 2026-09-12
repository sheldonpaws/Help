#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка размера системных файлов (pagefile, hiberfil, swapfile)
"""
import os

def format_size(size_bytes):
    """Форматирует размер в человекочитаемый вид."""
    for unit in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} ПБ"

def main():
    system_files = [
        "C:\\pagefile.sys",
        "C:\\hiberfil.sys",
        "C:\\swapfile.sys",
        "C:\\DumpStack.log.tmp"
    ]
    
    print("=" * 60)
    print("РАЗМЕР СИСТЕМНЫХ ФАЙЛОВ")
    print("=" * 60)
    
    print(f"{'Файл':<35} {'Размер':>20} {'Статус':>10}")
    print("-" * 60)
    
    for filepath in system_files:
        if os.path.exists(filepath):
            try:
                size = os.path.getsize(filepath)
                status = "✓ Существует"
                print(f"{os.path.basename(filepath):<35} {format_size(size):>20} {status:>10}")
            except (PermissionError, OSError) as e:
                print(f"{os.path.basename(filepath):<35} {'Недоступен':>20} {'Ошибка':>10}")
        else:
            print(f"{os.path.basename(filepath):<35} {'—':>20} {'Не найден':>10}")
    
    print("=" * 60)
    print("\nПримечание:")
    print("- pagefile.sys — файл подкачки (виртуальная память)")
    print("- hiberfil.sys — файл гибернации (быстрый запуск)")
    print("- swapfile.sys — дополнительный файл подкачки для UWP-приложений")
    print("- DumpStack.log.tmp — лог дампа памяти (может указывать на ошибки)")

if __name__ == "__main__":
    main()
