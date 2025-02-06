Claro, aquí tienes el texto traducido:

# Arduino-Car 🚗
Este proyecto permite el control remoto de un coche basado en Arduino a través de una interfaz web. Se utiliza un servidor Flask para retransmitir comandos entre la interfaz web y un Arduino conectado mediante comunicación serie.

## Descripción
Este proyecto muestra cómo integrar un Arduino con el framework Flask de Python para crear un controlador de coche interactivo. Sirve como un ejemplo práctico de integración robótica, perfecto para aprender proyectos basados en microcontroladores.
* **Para este código, necesitas Arduino IDE y un compilador para Python.**
# Requisitos
> [!IMPORTANTE]
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
# Dependencias
> [!IMPORTANTE]
> Necesitas descargar las dependencias para que la configuración funcione.
* Esto es para las dependencias del código Python.
<pre>pip install flask pyserial</pre>
* El código para Arduino no necesita dependencias.
# Configuración y Uso
  * Subir el código de Arduino:
       * Abre el Arduino IDE y sube el archivo .ino proporcionado a tu placa Arduino.
  *  Instalar las dependencias de Python:
      *  Ejecuta pip install flask pyserial en tu terminal.
   * Ejecutar el servidor Flask:
       *python app.py
   * El servidor iniciará en http://<IP->:4353 (reemplaza con la IP que te proporcione el host).
# Vista previa de la interfaz web
![captura de pantalla](https://github.com/Arnau029/Arduino-Car/blob/main/Image/MOBILE_AND_PC.png)
# Movimientos
### Demostraciones de movimiento

| **Adelante** | **Atrás** | **Izquierda** | **Derecha** |
|--------------|-----------|---------------|-------------|
| ![Adelante](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/forward.gif) | ![Atrás](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/Backwards.gif) | ![Izquierda](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/To_The_Left.gif) | ![Derecha](https://github.com/JitaProg/Arduino-Car/blob/main/GIFs/To_The_Right.gif) |
# Contribuyentes del proyecto
Estamos agradecidos por los esfuerzos de los siguientes contribuyentes que hicieron posible este proyecto:

<a href="https://github.com/Arnau029">
  <img src="https://github.com/Arnau029/Arduino-Car/blob/main/Contributors/Arnau.jpg" alt="Arnau" width="100" style="border-radius: 10px; margin-right: 5px;">
</a>
<a href="https://github.com/JitaProg">
  <img src="https://github.com/Arnau029/Arduino-Car/blob/main/Contributors/Borja.jpg" alt="Borja" width="100" style="border-radius: 10px; margin-right: 5px;">
</a>
<a href="https://github.com/EtreveSTDNT">
  <img src="https://github.com/Arnau029/Arduino-Car/blob/main/Contributors/Etreve.png" alt="Etreve" width="100" style="border-radius: 10px;">
</a>

# Licencia
Este proyecto está licenciado bajo la [Licencia MIT](https://github.com/JitaProg/Arduino-Car/blob/main/LICENSE).