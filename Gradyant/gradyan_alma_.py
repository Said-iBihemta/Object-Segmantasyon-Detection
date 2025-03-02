import argparse
import cv2

# Argüman ayrıştırıcısını oluştur
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=int, required=True,
                help="Path to input image")
ap.add_argument("-s", "--scharr", type=int, default=0,
                help="Apply Scharr operator if set to 1")
args = vars(ap.parse_args())

# Görüntüyü yükleyin
image = cv2.imread(args["OIG2.jpeg"])
if image is None:
    print("Hata: Görüntü yüklenemedi! Lütfen dosya yolunu kontrol edin.")
    exit()

# Gri tonlamalıya çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü göster
cv2.imshow("Gray", gray)
# Çekirdek boyutunu ayarlayın, (Scharr operatörünün Sobel operatörünü kullandığımıza bağlı olarak), 
# ardından sırasıyla x ve y ekseni boyunca gradyanları hesaplayın!
kszie = -1 if args["scharr"] > 0 else 3
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=kszie)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=kszie)

# Gradyan büyüklüğü görüntüleri artık yüzen veri türündedir, 
# bu nedenle bunları işaretsiz 8 bit tam sayı gösterimine geri dönüştürmeye dikkat etmemiz gerekir, 
# böylece diğer OpenCV işlevleri bunlar üzerinde çalışabilir ve bunları görselleştirebilir.
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# gradyan gösterimlerini tek bir görüntüde birleştirin
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

# Çıktı resimelrini göster.
cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr Combined", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
