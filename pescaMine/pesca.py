"""
minecraft_fish_sound.py
Detección de mordida por sonido y click derecho automático.
Requisitos: sounddevice, numpy, pyautogui, keyboard
pip install sounddevice numpy pyautogui keyboard
"""

import sounddevice as sd
import numpy as np
import pyautogui
import keyboard
import time
from collections import deque

# -------------- CONFIG --------------
DEVICE_NAME_SUBSTR = None  # opcional: substring del nombre del dispositivo de grabación to force selection
SAMPLE_RATE = 44100        # Hz
BLOCK_DURATION = 0.1       # segundos por bloque (latencia = block_duration)
CALIBRATION_SECONDS = 2.0  # medir ruido de fondo
THRESHOLD_MULTIPLIER = 6.0 # pico = multiplier * baseline_rms
MIN_SILENCE_AFTER_TRIGGER = 1.2  # segundos a esperar tras un disparo para evitar multi-trigger
ACTIVATE_KEY = "tab"        # tecla para activar/desactivar
EXIT_KEY = "ctrl"           # tecla para salir
RIGHT_CLICK_DELAY = 0.08   # delay entre recoger y volver a lanzar
# ------------------------------------

def choose_input_device():
    devices = sd.query_devices()
    # mostrar dispositivos
    print("Dispositivos de entrada disponibles:")
    for i, d in enumerate(devices):
        if d['max_input_channels'] > 0:
            print(i, d['name'])
    # si DEVICE_NAME_SUBSTR no es None, buscar matching
    if DEVICE_NAME_SUBSTR:
        for i, d in enumerate(devices):
            if DEVICE_NAME_SUBSTR.lower() in d['name'].lower() and d['max_input_channels'] > 0:
                print("Seleccionando dispositivo:", d['name'])
                return i
    # si hay dispositivo "Stereo Mix" o "WASAPI" virtual loopback, preferirlo por nombre
    for i, d in enumerate(devices):
        name = d['name'].lower()
        if ("stereo mix" in name or "wave out" in name or "loopback" in name) and d['max_input_channels'] > 0:
            print("Seleccionando dispositvo recomendado:", d['name'])
            return i
    # fallback: pedir selección manual
    idx = int(input("Ingresa el número del dispositivo de grabación que usar (ej 1): "))
    return idx

def rms(data):
    return np.sqrt(np.mean(np.square(data.astype(np.float32))))

def calibrate(device, samplerate, block_duration, seconds):
    print("Calibrando ruido de fondo durante {:.1f} s...".format(seconds))
    duration = int(seconds * samplerate)
    rec = sd.rec(duration, samplerate=samplerate, channels=1, dtype='float32', device=device)
    sd.wait()
    baseline = rms(rec.flatten())
    print("RMS baseline:", baseline)
    return baseline

def main():
    device = choose_input_device()
    fish_count = 0
    # calibrar
    # baseline = calibrate(device, SAMPLE_RATE, BLOCK_DURATION, CALIBRATION_SECONDS)
    threshold = 0.06  # <- aquí pones el valor que quieras
    print(f"Umbral de disparo: {threshold:.6f} (multiplicador {THRESHOLD_MULTIPLIER})")
    active = False
    last_trigger_time = 0
    print(f"Presiona {ACTIVATE_KEY} para activar/desactivar. Presiona {EXIT_KEY} para salir.")
    # stream en bloque
    frames_per_block = int(SAMPLE_RATE * BLOCK_DURATION)

    try:
        with sd.InputStream(device=device, channels=1, samplerate=SAMPLE_RATE, blocksize=frames_per_block) as stream:
            while True:
                if keyboard.is_pressed(EXIT_KEY):
                    print("Salida solicitada.")
                    break
                if keyboard.is_pressed(ACTIVATE_KEY):
                    active = not active
                    print("Activo:" , active)
                    time.sleep(0.3)  # evitar toggles múltiples por rebote
                data, _ = stream.read(frames_per_block)
                arr = np.frombuffer(data, dtype=np.float32)
                level = rms(arr)
                # debug opcional:
                print(f"Nivel RMS actual: {level:.6f}", end="\r")
                if active and (time.time() - last_trigger_time) > MIN_SILENCE_AFTER_TRIGGER:
                    if level > threshold:
                        fish_count += 1
                        print(f"\nTrigger detectado! nivel={level:.6f} > umbral={threshold:.6f} | Total: {fish_count}")
                        # click derecho para recoger
                        pyautogui.mouseDown(button='right')
                        time.sleep(0.03)
                        pyautogui.mouseUp(button='right')
                        time.sleep(RIGHT_CLICK_DELAY)
                        # volver a lanzar
                        pyautogui.mouseDown(button='right')
                        time.sleep(0.08)
                        pyautogui.mouseUp(button='right')
                        last_trigger_time = time.time()

                        # cada 20 peces, abrir chat y enviar mensaje
                        if fish_count % 20 == 0:
                            time.sleep(0.2)  # pequeña pausa antes de abrir chat
                            pyautogui.press('t')  # abrir chat
                            time.sleep(0.1)
                            mensaje = "/pesca sellall"  # aquí tu mensaje
                            pyautogui.write(mensaje, interval=0.02)
                            pyautogui.press('enter')  # enviar mensaje
                            time.sleep(0.2)  # pequeña pausa antes de seguir
                # pequeña espera no necesaria porque stream.read ya es bloqueante
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
