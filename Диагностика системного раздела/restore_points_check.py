#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка точек восстановления системы
Примечание: требует доступа к WMI, может потребовать запуск от администратора
"""
import sys

def main():
    print("=" * 60)
    print("ПРОВЕРКА ТОЧЕК ВОССТАНОВЛЕНИЯ СИСТЕМЫ")
    print("=" * 60)
    
    try:
        import wmi
    except ImportError:
        print("\nТребуется установить библиотеку wmi:")
        print("  pip install wmi")
        print("\nИли используйте встроенную команду PowerShell:")
        print("  Get-ComputerRestorePoint")
        sys.exit(1)
    
    try:
        c = wmi.WMI()
        restore_points = c.Win32_RestorePoint()
        
        if not restore_points:
            print("\nТочки восстановления не найдены.")
        else:
            print(f"\nНайдено точек восстановления: {len(restore_points)}")
            print("-" * 60)
            print(f"{'№':<5} {'Дата создания':<25} {'Описание':<30}")
            print("-" * 60)
            
            for i, rp in enumerate(restore_points, 1):
                description = getattr(rp, 'Description', 'Нет описания')[:28]
                creation_time = getattr(rp, 'CreationTime', 'Неизвестно')
                # Форматирование даты из WMI
                if creation_time:
                    try:
                        # WMI дата в формате YYYYMMDDHHMMSS.mmmmmm+###
                        dt = wmi.from_time(creation_time)
                        creation_time = dt.strftime('%d.%m.%Y %H:%M')
                    except:
                        pass
                print(f"{i:<5} {str(creation_time):<25} {description:<30}")
        
        print("=" * 60)
        print("\nДля управления точками восстановления:")
        print("1. Панель управления → Система → Защита системы")
        print("2. Или команда: systempropertiesprotection")
        
    except Exception as e:
        print(f"\nОшибка при получении данных: {e}")
        print("\nАльтернатива — используйте PowerShell:")
        print("  Get-ComputerRestorePoint | Select-Object CreationTime, Description")

if __name__ == "__main__":
    main()
