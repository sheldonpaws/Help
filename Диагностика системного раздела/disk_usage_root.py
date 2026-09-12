#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Анализ размера папок в корне диска C:\
"""
import os
import sys

def get_folder_size(folder_path):
    """Рекурсивно подсчитывает размер папки в байтах."""
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    if os.path.isfile(filepath) and not os.path.islink(filepath):
                        total_size += os.path.getsize(filepath)
                except (PermissionError, OSError):
                    continue
    except (PermissionError, OSError):
        pass
    return total_size

def format_size(size_bytes):
    """Форматирует размер в человекочитаемый вид."""
    for unit in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} ПБ"

def main():
    root_path = "C:\\"
    print("=" * 60)
    print("АНАЛИЗ РАЗМЕРА ПАПОК В КОРНЕ C:\\")
    print("=" * 60)
    
    folders = []
    try:
        for entry in os.listdir(root_path):
            full_path = os.path.join(root_path, entry)
            if os.path.isdir(full_path):
                size = get_folder_size(full_path)
                folders.append((entry, size))
    except PermissionError:
        print("Требуется запуск от имени администратора!")
        sys.exit(1)
    
    # Сортировка по убыванию размера
    folders.sort(key=lambda x: x[1], reverse=True)
    
    print(f"{'Папка':<30} {'Размер':>25}")
    print("-" * 60)
    for name, size in folders:
        print(f"{name:<30} {format_size(size):>25}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
