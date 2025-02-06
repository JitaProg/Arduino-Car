# Coche Arduino 🚗
Este proyecto consiste en la elaboración de un coche con Arduino Uno y Raspberry Pi 4. Es la alternativa definitiva al módulo Bluetooth. Si tienes una placa Arduino Uno y una Raspberry, este es tu proyecto.
Dicho proyecto permite el control remoto de un coche a través de una interfaz web. Se utiliza un servidor Flask para retransmitir comandos entre la interfaz web y un Arduino conectado mediante comunicación serie.

## Descripción ✍🏽
Este proyecto muestra cómo integrar un Arduino con el framework Flask de Python para crear un controlador de coche interactivo. Sirve como un ejemplo práctico de integración robótica, perfecto para aprender proyectos basados en microcontroladores.
* **Para este código, necesitas Arduino IDE y un compilador para Python.**
# Requisitos ⚒️
> [!IMPORTANT]
> Necesitas este hardware y software para realizar este proyecto:
  *  Hardware:
        * Placa Arduino (compatible con los pines definidos en el código).
        * Módulo controlador de motores (por ejemplo, L298N o similar).
        * Motores DC.
        * Conexión USB para la comunicación con Arduino.
  *  Software:
       * Arduino IDE
       * Python 3.9 o superior.
       * Flask (pip install flask)
       * Biblioteca de comunicación serie: pyserial (pip install pyserial).
# Dependencias 📓
> [!IMPORTANT]
> Necesitas descargar las dependencias para que la configuración funcione.
* Explicado a continuación en configuración
* El código para Arduino no necesita dependencias.
# Configuración y Uso ⚙️
  * Subir el código de Arduino:
       * Descargar editor de codigo Arduino IDE <a href="https://www.arduino.cc/en/software" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="20" height="20"/></a>
       * Abre el Arduino IDE y sube el archivo <b>.ino</b> proporcionado a tu placa Arduino.
  *  Instalar las dependencias de Python:
      *  Ejecuta en tu terminal.
          ```bash
          pip install flask pyserial
   * Ejecutar el servidor Flask, ya sea el nuestro o uno creado por vosotros en su defecto sera RemoteCarControl.py:
      *  Ejecuta en tu terminal.
          ```bash
           python .\RemoteCarControl.py
   * El servidor iniciará por defecto en http://<IP->:4353:
      * Reemplaza con la IP que te proporcione el host.
# Vista previa de la interfaz web 👁️👁️
![captura de pantalla](https://github.com/Arnau029/Arduino-Car/blob/main/Image/MOBILE_AND_PC.png)
# Movimientos 🪇
### Demostraciones de movimiento

| **Adelante** | **Atrás** | **Izquierda** | **Derecha** |
|--------------|-----------|---------------|-------------|
| ![Adelante](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/forward.gif) | ![Atrás](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/Backwards.gif) | ![Izquierda](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/To_The_Left.gif) | ![Derecha](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/To_The_Right.gif) |

# Licencia
Este proyecto está licenciado bajo la [Licencia MIT](https://github.com/JitaProg/Arduino-Car/blob/main/LICENSE).
