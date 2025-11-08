# 🐟 Sistema de Pesca Automático — Minecraft + Python + VB-CABLE

Este proyecto permite automatizar la pesca en Minecraft utilizando **Python** y el driver de audio virtual **VB-CABLE**.  
El sistema detecta el sonido del juego y actúa automáticamente, simulando una pesca real.

---

## ⚙️ Requisitos

- [Python 3.x](https://www.python.org/downloads/)
- [VB-CABLE Virtual Audio Device](https://vb-audio.com/Cable/)
- Minecraft Java Edition
- Windows 10 o superior

---

## 🚀 Instalación

### 1️⃣ Instalar VB-CABLE

1. Entra a la carpeta `VBCABLE` y ejecuta el archivo  
   **`VBCABLE_Setup_x64.exe`**
2. Haz clic en **Install Driver**.
3. Abre el panel de sonido de Windows (icono de altavoz abajo a la derecha).
4. Cambia la **salida de audio** a:  
   **`CABLE Input (VB-Audio Virtual Cable)`**

> 🔇 Nota: Al hacer esto, no escucharás el sonido del juego, ya que lo procesará el driver.

<img width="356" height="231" alt="image" src="https://github.com/user-attachments/assets/8bcd7ea7-0496-4320-b7a0-f38792f3788b" />

> Si no ves la opción “CABLE Input”, reinicia el PC o reinstala VB-CABLE.

---

### 2️⃣ Instalar Python

1. Ejecuta `python.exe` y sigue la instalación.  
2. Asegúrate de marcar las opciones:
   - ✅ **Install pip**
   - ✅ **Add Python to PATH**

Con eso podrás ejecutar Python desde la terminal.

---

## 💻 Ejecución desde la terminal

1. Presiona **Win + R**, escribe `cmd` y presiona **Enter**.
2. Navega hasta la carpeta del proyecto.  
   Por ejemplo, si está en Descargas:

   ```bash
   cd Downloads;
   cd pescaMine;
   ```

3. Verifica que estás en la carpeta correcta:

   ```bash
   dir
   ```
   <img width="427" height="112" alt="image" src="https://github.com/user-attachments/assets/71f03b98-2cc3-42b0-a938-f3492b2bfefe" />

  - Si aparece el archivo pesca.py, ya puedes ejecutarlo:
     ```bash
     py pesca.py
     ```
4. Al iniciar, el programa mostrará una lista de dispositivos de audio.
Escribe el número correspondiente a:

    ```bash
    "CABLE Output (VB-Audio Virtual Cable)"
    ```
   <img width="543" height="294" alt="image" src="https://github.com/user-attachments/assets/ed6e1ba5-82d0-4afe-83f0-5b979e166d5a" />

---======================---

## 🎣 Uso dentro del juego

- Asegúrate de que Minecraft esté abierto con el sonido activado.
- En la terminal, revisa que aparezca:
 ```bash
 Activo: Truetual: 0.000015
 ```
> Si dice Activo: Falseual: 0.000015, presiona TAB para activarlo y que quede en Truetual.
- Presiona CTRL para detener el script en cualquier momento.
<img width="543" height="380" alt="image" src="https://github.com/user-attachments/assets/371b500a-82b2-4e81-ba15-afb4ecdb377f" />

---

## 🧠 Configuración del script

El sistema está configurado para abrir el chat y vender cada 20 pescas.
Puedes cambiar este número fácilmente:

1. Haz clic derecho sobre pesca.py → Abrir con → Bloc de notas
   <img width="877" height="315" alt="image" src="https://github.com/user-attachments/assets/78edbf68-bbe1-43ab-bdce-cc992d965822" />
2. Busca la línea:
```bash
if fish_count % 20 == 0:
```
3. Cambia el 20 por el número de pescas que quieras antes de vender.

---

## ⚠️ Recomendaciones

- Asegúrate de tener espacio en el inventario, ya que también se pueden pescar cebos.
- No minimices Minecraft mientras el script esté activo.
- Si el sonido no se detecta, revisa que la salida de audio siga siendo “CABLE Input”.


