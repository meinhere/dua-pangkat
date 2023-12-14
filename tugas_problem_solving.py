import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout)

def cek_bilangan(n):
  for i in reversed(range(layout2.count())):
    layout2.itemAt(i).widget().setParent(None)

  label = QLabel("Hasil Perhitungan")
  layout2.addWidget(label)

  while (n > 0 and n % 2 == 0):
    bagi = round(n / 2)
    hitung = QLabel("Bilangan " + str(n) + " / 2 = " + str(bagi))
    layout2.addWidget(hitung)
    n = bagi
  
  hasil = QLabel()
  if (n == 1):
    hasil.setText("TERMASUK Bilangan 2 Pangkat")
  else:
    hasil.setText("BUKAN Bilangan 2 Pangkat")
  layout2.addWidget(hasil)
  
  layoutUtama.addLayout(layout2)

def set_window():
  global layoutUtama, layout1, layout2
  layoutUtama = QVBoxLayout()
  layout1 = QHBoxLayout()
  layout2 = QVBoxLayout()

  label = QLabel("Bilangan")
  inp = QLineEdit()
  btn = QPushButton("Cek")
  btn.setStyleSheet("background-color: #0d6efd; color: #f8f9fa;")
  btn.clicked.connect(lambda : cek_bilangan(int(inp.text())))
  layout1.addWidget(label)
  layout1.addWidget(inp)
  layout1.addWidget(btn)

  layoutUtama.addLayout(layout1)
  window.setLayout(layoutUtama)

  window.setWindowTitle("Problem Solving - Cek Bilangan 2 Pangkat")
  window.show()
  sys.exit(app.exec())

app = QApplication(sys.argv)
window = QWidget()
set_window()