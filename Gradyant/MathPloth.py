# Gerekli paketleri içeri aktar!
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

# Argüman ayrıştırıcısını oluşturun ve argümanları ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
     help="path to input image")
args = vars(ap.parse_args())

# Griş görüntüsünü yükle ve gri renge dönüştür
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sırasıyla x ve y eksenindeki eğimleri hesaplayın
gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

# Gradyan büyüklüğünü ve yönelimini hesaplayın
magnitude = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi)

# Giriş gri tonlamalı görüntüyü, sırasıyla gradyan büyüklüğü ve yönelim 
# gösterimleriyle birlikte görüntülemek için bir şekil başlatın
(fig, axs) = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))

# Her bir resmin grafiğini çiz
axs[0].imshow(gray, cmap="gray")
axs[1].imshow(magnitude, cmap="jet")
axs[2].imshow(orientation, cmap="jet")

# Her eksenin başlığını ayarlayın
axs[0].set_title("Grayscale")
axs[1].set_title("Gradiient Magnitude")
axs[2].set_title("Gradient Orientation [0, 180]")

# Her bir eksenin üzerinden geçin ve x ve y işaretlerini kapatın
for i in range(0, 3):
    axs[i].get_xaxis().set_ticks([])
    axs[i].get_yaxis().set_ticks([])

# Grafiği göster
plt.tight_layout()
plt.show()