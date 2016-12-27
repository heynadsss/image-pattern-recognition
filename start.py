#!/usr/bin/env python
from mainClass.EkstrakFitur import EkstrakFitur
from mainClass.TestCitra import DeteksiObjek

# Sudah pake data ikan, tapi masih dikit

isTrain = raw_input("Sudah ada model SVM? (y/n): ")
if isTrain=="n":
	# Mengekstraksi ciri, untuk mendapatkan data vektor objek dan bukan objek yang akan dideteksi,
	# dalam hal ini memisahkan objek dengan background. (Proses ekstraksi menggunakan HOG)
	print "Step 1: Ekstrak fitur vektor dari data latih citra"
	EkstrakFitur().startExtract()

# tes objek citra yg akan dideteksi ikannya
print "\nStep 3: Proses mendeteksi objek dari model yang telah dilatih"

# tesCitra = "data/datalatih/CarData/TestImages/test-132.pgm"
tesCitra = "data/datalatih/Ikan/TestImages/9.jpg"
downscale = 2 # untuk skala pengecilan citra yg dites, default yg ada di kelas = 2.5x
visualisasi = True # untuk melihat proses pendeteksian objek pada citra saat sliding windows, default yg di kelas = True
DeteksiObjek(tesCitra,downscale,visualisasi).startDeteksiObjek()