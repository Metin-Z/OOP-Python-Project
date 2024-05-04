import os
from PyQt5 import uic

# convert.py dosyasının bulunduğu dizin
current_dir = os.path.dirname(__file__)

# panel.ui dosyasının tam yolu
ui_file = os.path.join(current_dir, "panel.ui")

# panel.py dosyasının oluşturulacağı konum
output_file = os.path.join(current_dir, "panel.py")

# uic.compileUi kullanarak panel.py dosyasını oluşturma
with open(output_file, "w", encoding="utf-8") as fout:
    uic.compileUi(ui_file, fout)
