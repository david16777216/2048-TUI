# 2048-TUI

Un clon simple y minimalista del juego **2048** diseñado para ejecutarse directamente en la terminal. Este proyecto fue creado con fines educativos para aprender las bases del desarrollo de algoritmos en Python y el flujo de trabajo en Git/GitHub.

## Cómo Jugar

El objetivo es combinar bloques numéricos similares para sumar sus valores hasta alcanzar el bloque **2048**.

El tablero se controla mediante las clásicas teclas de dirección de terminal de una sola letra (seguidas de la tecla `Enter`):

*   `w` : Mover bloques hacia **Arriba**
*   `s` : Mover bloques hacia **Abajo**
*   `a` : Mover bloques hacia la **Izquierda**
*   `d` : Mover bloques hacia la **Derecha**
*   `x` : Salir del juego inmediatamente

## 🚀 Requisitos e Instalación

Solo necesitas tener instalado **Python 3** en tu sistema (no requiere ninguna librería externa de terceros, corre puramente con la biblioteca estándar).

1. Clona este repositorio en tu máquina:
   ```bash
   git clone git@github.com:david16777216/2048-TUI.git

   
2. Entra a la carpeta del proyecto:

    ```Bash
    cd 2048-TUI

3. Ejecuta el script:
   ```bash
   python 2048.py
   
🛠️ Detalles Técnicos del Desarrollo
Manipulación de Matrices: Los desplazamientos verticales (w / s) reutilizan la lógica de movimiento horizontal mediante rotaciones matriciales iterativas de 90 grados.

Probabilidades: Los nuevos bloques aparecen de forma aleatoria con un sistema ponderado: 90% de probabilidad de generar un 2 y 10% de generar un 4.

🤝 Código Abierto y Contribuciones
Este es mi primer paso en el mundo open-source. El código actual cumple con las mecánicas básicas, pero tiene mucho espacio para optimizaciones (por ejemplo, manejo de colisiones repetidas en un solo turno, detección de fin de partida o limpieza de código repetitivo).

¡Cualquier sugerencia, reporte de bug o mejora mediante un Pull Request es más que bienvenida!

📄 Licencia
Este proyecto está bajo la Licencia MIT – siéntete libre de usarlo, modificarlo y romperlo para aprender.