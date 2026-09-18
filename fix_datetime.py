import pathlib
import re

# Ловим любую вариацию: |date:'...P' или |date:"...P", где есть Y-m-d и P в конце
pattern = re.compile(r"\|date:['\"]([^'\"]*?)P['\"]")

for p in pathlib.Path('.').rglob('*.html'):
    text = p.read_text(encoding='utf-8')
    new_text = pattern.sub(r"|date:'\1'", text)   # убираем P
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')
        print(f"Исправлено: {p}")