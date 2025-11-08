# 🌀 DOORS – Wheel Glitch Script (AutoHotkey)

Este script usa **AutoHotkey (AHK)** para girar rápidamente la **rueda del ratón** y aprovechar un bug visual del juego **DOORS** de Roblox.  
El comportamiento causa un ligero *lag* o desincronización que permite volver a una posición previa dentro del juego y asi atravesar paredes con algo de suerte.
> Esto es mas que nada algo como una automatizacón, ya que se puede girar la rueda rápidamente de forma manual, pero es mas difícil de esa forma.

---

## ⚙️ Requisitos

- [AutoHotkey v1 o v2](https://www.autohotkey.com/)
- Roblox instalado
- Juego: [DOORS](https://www.roblox.com/games/6516141723/DOORS)

---

## 💻 Código del script

```ahk
Tab::
While GetKeyState("Tab", "P")
{
    Send {WheelUp}
    Sleep, 10
}
return
```

---

## 🧠 Explicación del código

- Tab::
  Define la tecla que activará el bucle (en este caso, la tecla Tab).
- While GetKeyState("Tab", "P")
  Mantiene el ciclo activo mientras Tab esté presionado.
- Send {WheelUp}
  Envía el comando de “girar rueda del mouse hacia arriba” de forma continua.
- Sleep, 10
  Pausa 10 milisegundos entre cada giro para controlar la velocidad del bucle.

Cuando sueltas Tab, el bucle se detiene automáticamente.

---

## 🕹️ Cómo usarlo

1. Instala AutoHotkey desde su sitio oficial.
2. Crea un nuevo archivo en tu PC con el nombre, por ejemplo:
  wheel_glitch.ahk
3. Pega el código anterior y guarda.
4. Ejecuta el script (doble clic sobre el archivo .ahk).
5. Abre Roblox → DOORS.
6. Dentro del juego:
   - Equipa dos objetos distintos del inventario.
   - Comienza a caminar.
   - Mantén presionada la tecla Tab para que el script gire rápidamente la rueda.
   - Suelta Tab cuando quieras detener el efecto.

El resultado es un bug donde el juego solo guarda tu posición anterior (antes del giro de rueda), y al soltar, te “teletransporta” hacia atrás, a veces atravesando paredes.
> ⚠️ El comportamiento puede variar según la versión del juego o la latencia del servidor.

---

## ⚠️ Advertencias

* Este script se comparte solo con fines experimentales y educativos.
* No se recomienda su uso en partidas públicas, ya que puede ser considerado un exploit.
* No modifica archivos del juego ni interactúa con la red; solo envía eventos de entrada locales (scroll del ratón).
