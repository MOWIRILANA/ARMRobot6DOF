import cv2
import cv2.aruco as aruco
import numpy as np
import urllib.request

url= 'http://192.168.43.147/cam-lo.jpg'
im=None

# Fungsi untuk menghitung jarak antar dua titik
def hitung_jarak(titik1, titik2):
    return np.linalg.norm(titik1 - titik2)

# Inisialisasi detektor ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

# Inisialisasi kamera (ganti dengan parameter kamera Anda)
camera_matrix = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]])
dist_coeff = np.zeros((4, 1), dtype=np.float32)

while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    im = cv2.imdecode(imgnp,-1)
    
    # Konversi ke grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    # Deteksi marker ArUco
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    corners, ids, _ = detector.detectMarkers(im)

    if ids is not None:
            for i in range(len(ids)):
                if ids[i] == 1 or ids[i] == 4:
                    # Hitung jarak antar dua ID
                    jarak = hitung_jarak(corners[i][0][0], corners[i][0][2])

                    # Tampilkan jarak pada frame
                    posisi_teks = tuple(np.mean(corners[i][0], axis=0).astype(int))
                    cv2.putText(im, f"Jarak ID {ids[i]}: {jarak:.2f} piksel",
                                posisi_teks, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Gambar marker dan ID pada frame
        # im = aruco.drawDetectedMarkers(im, corners, ids)

    # Tampilkan frame
    cv2.imshow('Deteksi ArUco', im)

    # Hentikan program dengan menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela
im.release()
cv2.destroyAllWindows()
