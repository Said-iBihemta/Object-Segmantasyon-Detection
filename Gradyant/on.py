import argparse
import cv2

# Argüman ayrıştırıcısını oluştur
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="Path to input image")  # type=int yerine type=str olmalı
ap.add_argument("-s", "--scharr", type=int, default=0,
                help="Apply Scharr operator if set to 1")
args = vars(ap.parse_args())

# Görüntüyü yükleyin
image = cv2.imread(args["image"])
if image is None:
    print("Hata: Görüntü yüklenemedi! Lütfen dosya yolunu kontrol edin.")
    exit()

# Gri tonlamalıya çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Çekirdek boyutunu ayarlayın
ksize = -1 if args["scharr"] > 0 else 3  # Yazım hatası düzeltildi

# X ve Y eksenleri boyunca gradyanları hesapla
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

# Gradyan büyüklüğünü 8 bit formatına dönüştür
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# X ve Y gradyanlarını birleştir
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

# Çıktı görüntülerini göster
cv2.imshow("Gray", gray)
cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr Combined", combined)

# Pencereleri açık tut ve çıkış için bir tuşa basılmasını bekle
cv2.waitKey(0)
cv2.destroyAllWindows()
