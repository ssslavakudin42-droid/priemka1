# -*- coding: utf-8 -*-
"""
Сборка готового приложения: template.html + base_data.js + xlsx.full.min.js
-> «Башмачок Приёмка.html» (один файл, работает без интернета).

python build.py
"""
tpl = open("template.html", encoding="utf-8").read()
base = open("base_data.js", encoding="utf-8").read()
xlsx = open("xlsx.full.min.js", encoding="utf-8").read()

out = tpl.replace('<script src="xlsx.full.min.js"></script>', "<script>\n" + xlsx + "\n</script>")
out = out.replace('<script src="base_data.js"></script>', "<script>\n" + base + "\n</script>")
assert 'src="xlsx' not in out and 'src="base_data' not in out, "шаблон не совпал"

name = "Башмачок Приёмка.html"
open(name, "w", encoding="utf-8").write(out)
import os
print(f"Готово: {name} ({os.path.getsize(name)/1e6:.1f} МБ)")
