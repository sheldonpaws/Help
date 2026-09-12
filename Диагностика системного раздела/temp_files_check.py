#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка временных файлов Windows
"""
import os
import sys

def get_folder_size(folder_path):
    """Рекурсивно подсчитывает размер папки в байтах."""
    total_size = 0
    file_count = 0
    try:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    if os.path.isfile(filepath) and not os.path.islink(filepath):
                        total_size += os.path.getsize(filepath)
                        file_count += 1
                except (PermissionError, OSError):
                    continue
    except (PermissionError, OSError):
        pass
    return total_size, file_count

def format_size(size_bytes):
    """Форматирует размер в человекочитаемый вид."""
    for unit in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} ПБ"

def main():
    temp_paths = [
        os.environ.get('TEMP', 'C:\\Users\\User\\AppData\\Local\\Temp'),
        os.environ.get('TMP', 'C:\\Users\\User\\AppData\\Local\\Temp'),
        "C:\\Windows\\Temp",
        "C:\\Windows\\SoftwareDistribution\\Download",
        "C:\\Users\\User\\AppData\\Local\\OneDrive\\logs",
    ]
    
    print("=" * 60)
    print("АНАЛИЗ ВРЕМЕННЫХ ФАЙЛОВ")
    print("=" * 60)
    
    print(f"{'Путь':<50} {'Размер':>12} {'Файлов':>10}")
    print("-" * 75)
    
    for path in temp_paths:
        if os.path.exists(path):
            size, count = get_folder_size(path)
            print(f"{path:<50} {format_size(size):>12} {count:>10}")
        else:
            print(f"{path:<50} {'—':>12} {'Не найдено':>10}")
    
    print("=" * 60)
    print("\nПримечание:")
    print("- TEMP/TMP — временные файлы пользователя")
    print("- Windows\\Temp — системные временные файлы")
    print("- SoftwareDistribution\\Download — кэш обновлений Windows")
    print("- OneDrive\\logs — логи OneDrive (если не используется, можно удалить)")

if __name__ == "__main__":
    main()
