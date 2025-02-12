import subprocess
import time

def start_emulator():
    # Cambia el nombre del AVD por el tuyo
    avd_name = "Pixel_5_API_30"
    subprocess.run(['emulator', '-avd', avd_name, '-no-window', '-no-audio', '-no-boot-anim'])

    # Esperar a que el emulador se inicie
    time.sleep(30)  # Ajusta el tiempo si es necesario

def check_device_online():
    # Verificar que el dispositivo esté online
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
    if b'emulator-5554' in result.stdout:
        print("El emulador está online.")
    else:
        print("El emulador no está online.")

start_emulator()
check_device_online()
