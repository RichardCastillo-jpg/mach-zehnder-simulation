# Simulación Foto Sin Luz
 
Simulación en Python de una cámara que registra la imagen parcial de un objeto "sin luz": cada píxel de una imagen en blanco y negro se trata como una bomba de Elitzur-Vaidman y se le aplica el protocolo del interferómetro de Mach-Zehnder. Los detalles del modelo y los resultados están en el informe.
 
## Estructura
 
```
├── server.py    # Interfaz web (Streamlit)
├── photo.py     # Carga, binarización y reconstrucción de la imagen
├── pixel.py     # Simulación del protocolo por píxel
└── metrics.py   # Cálculo de métricas
```
 
## Instalación
 
```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install streamlit numpy pillow
```
 
## Ejecución
 
```bash
streamlit run server.py
```
