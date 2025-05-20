import socket

# Konfigurasi server ESP32
server_ip = "192.168.43.232"  # Ganti dengan IP ESP32 yang sesuai
server_port = 12345

# Inisialisasi socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mencoba terhubung ke server ESP32
try:
    client_socket.connect((server_ip, server_port))
    print(f"Terhubung ke ESP32 di {server_ip}:{server_port}")

    while True:
        # Mengirim data integer ke ESP32
        message = int(25)
        client_socket.send(str(message).encode('utf-8'))

        # Menerima balasan integer dari ESP32
        response = client_socket.recv(1024).decode('utf-8')
        print(f'Menerima balasan dari ESP32: {int(response)}')
except Exception as e:
    print(f'Error: {e}')
finally:
    # Menutup koneksi
    print("Menutup koneksi.")
    client_socket.close()