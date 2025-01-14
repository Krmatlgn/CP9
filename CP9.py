import os
import subprocess
import time
import random
import string
import requests

# Şifre oluşturma fonksiyonu
def generate_random_password(min_length=8, max_length=20):
    """Rastgele şifre oluşturur. 8 ile 20 karakter arasında, özel karakterler dahil."""
    characters = string.ascii_letters + string.digits + "!'^+%&/()=)?_-*>£#$½{[]}\|"
    password_length = random.randint(min_length, max_length)  # Şifre uzunluğunu rastgele belirle
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password

def install_dependencies():
    """Gerekli kütüphaneler ve araçlar otomatik olarak kurulur."""
    print("[INFO] Gerekli kütüphaneler ve araçlar kuruluyor...")

    # Sistemde gerekli araçları yükleyelim
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "tor", "macchanger", "python3-pip"], check=True)
        print("[INFO] Sistem araçları başarıyla kuruldu.")
    except subprocess.CalledProcessError:
        print("[HATA] Sistem araçları yüklenemedi.")
    
    # Python kütüphanelerini yükleyelim
    try:
        subprocess.run(["pip3", "install", "requests"], check=True)
        print("[INFO] Python kütüphaneleri başarıyla kuruldu.")
    except subprocess.CalledProcessError:
        print("[HATA] Python kütüphaneleri yüklenemedi.")

def create_tor_password():
    """TOR şifresi oluşturur."""
    print("[INFO] TOR şifresi oluşturuluyor...")

    # 8 ile 20 karakter arasında rastgele şifre oluşturuyoruz
    password = generate_random_password()
    print(f"[INFO] Oluşturulan TOR şifresi: {password}")

    return password

def configure_tor():
    """TOR servisini yeniden başlatır ve yapılandırır."""
    try:
        subprocess.run(["sudo", "service", "tor", "restart"], check=True)
        print("[INFO] TOR servisi yeniden başlatıldı.")
    except Exception as e:
        print(f"[HATA] TOR servisi başlatılamadı: {e}")

def change_mac_address(interface="eth0"):
    """MAC adresini rastgele değiştirir."""
    try:
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        subprocess.run(["sudo", "macchanger", "-r", interface], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(f"[INFO] {interface} arayüzünün MAC adresi değiştirildi.")
    except Exception as e:
        print(f"[HATA] MAC adresi değiştirilemedi: {e}")

def change_tor_identity():
    """Tor kimliğini değiştirmek için Tor servisinin yeniden başlatılması."""
    print("[INFO] Tor kimliği değiştiriliyor...")
    configure_tor()

    # Tor kimliği değişiminden sonra "newnym" komutunu çalıştırarak yeni bir IP almayı sağlayalım
    try:
        subprocess.run(["sudo", "torctl", "newnym"], check=True)
        print("[INFO] Tor kimliği başarıyla değiştirildi ve yeni IP alındı.")
    except Exception as e:
        print(f"[HATA] Tor kimliği değiştirilirken hata oluştu: {e}")

def get_current_ip():
    """Mevcut TOR IP adresini döndürür."""
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        response = requests.get("http://httpbin.org/ip", proxies=proxies)
        return response.json().get("origin")
    except requests.RequestException as e:
        print(f"[HATA] IP alınamadı: {e}")
        return None

def main():
    """Ana anonimlik döngüsü."""
    install_dependencies()  # Gerekli araçları yükle
    password = create_tor_password()  # Rastgele Tor şifresini oluştur
    configure_tor()  # TOR servisini yapılandır

    print("[INFO] Anonimlik aracı başlatılıyor...")

    while True:
        print("\n[1] MAC adresi değiştiriliyor...")
        change_mac_address("eth0")

        print("[2] TOR kimliği değiştiriliyor...")
        change_tor_identity()  # Tor kimliği değiştirildi

        print("[3] Yeni IP adresi alınıyor...")
        new_ip = get_current_ip()
        if new_ip:
            print(f"Yeni TOR IP adresiniz: {new_ip}")
        else:
            print("IP adresi alınamadı.")

        print("[4] Bekleniyor (120 saniye)...")
        for i in range(120, 0, -1):  # 120 saniye için geri sayım
            print(f"\rBekleniyor: {i} saniye", end="")
            time.sleep(1)

        print("\n")

if __name__ == "__main__":
    main()
