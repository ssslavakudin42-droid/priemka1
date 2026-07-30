# -*- coding: utf-8 -*-
"""
Обновление вшитой базы номенклатуры из выгрузки Айтиды.

Шаг 1. В Айтиде: Справочники -> Товары -> печать/экспорт «Список товаров» в Excel.
Шаг 2. python update_base.py "вся база айтиды.xlsx"
        -> перезапишет base_data.js
Шаг 3. python build.py
        -> соберёт новый «Башмачок Приёмка.html»

Формат выгрузки (лист «Список товаров»):
  колонка A — № строки (число) или название папки (текст, остальное пусто)
  колонка B — наименование
  колонка J — код
  колонка K — артикул
"""
import sys, json
import openpyxl

src = sys.argv[1] if len(sys.argv) > 1 else "вся база айтиды.xlsx"
wb = openpyxl.load_workbook(src, read_only=True)
ws = wb.active

items = []
for row in ws.iter_rows(values_only=True):
    a, name = row[0], row[1]
    if not isinstance(a, (int, float)) or not name:
        continue  # заголовки и строки-папки пропускаем
    code = str(row[9]).strip() if row[9] is not None else ""
    art = str(row[10]).strip() if row[10] is not None else ""
    items.append([str(name).strip(), code, art])

with open("base_data.js", "w", encoding="utf-8") as f:
    f.write("const BASE=")
    json.dump(items, f, ensure_ascii=False, separators=(",", ":"))
    f.write(";")

print(f"Готово: base_data.js — {len(items)} товаров. Теперь запусти build.py")
