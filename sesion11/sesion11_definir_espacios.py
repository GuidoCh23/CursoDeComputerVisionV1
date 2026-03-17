"""
Herramienta para definir espacios de estacionamiento sobre una imagen.
Controles:
Click izquierdo x2: 
primer click esquina superior-izquierda,
segundo click esquina inferior-derecha
Flechas: mover la vista
Rueda del mouse: zoom
+/-: zoom in / out
U: deshacer ultimo espacio
S: guardar en archivo .txt
Q/ESC: salir
"""

import cv2
import numpy as np
import sys
import os

IMAGEN_PATH = sys.argv[1] if len(sys.argv) > 1 else 'frame_referencia.jpg'
OUTPUT_TXT = sys.argv[2] if len(sys.argv) > 2 else 'espacios_parking.txt'

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
PAN_STEP = 40
ZOOM_STEP = 0.15
ZOOM_MIN = 0.2
ZOOM_MAX = 8.0

imagen_original = None
espacios = []       # lista de (x1, y1, x2, y2) en coords originales
punto_ini = None     # primer punto del espacio en curso
mouse_pos = (0, 0)   # posicion actual del mouse en coords de pantalla
zoom = 1.0
offset_x = 0.0
offset_y = 0.0


def clamp_offset():
    global offset_x, offset_y
    h, w = imagen_original.shape[:2]
    offset_x = max(0.0, min(offset_x, w - ANCHO_VENTANA / zoom))
    offset_y = max(0.0, min(offset_y, h - ALTO_VENTANA  / zoom))


def pantalla_a_imagen(px, py):
    ix = px / zoom + offset_x
    iy = py / zoom + offset_y
    h, w = imagen_original.shape[:2]
    return max(0.0, min(w - 1, ix)), max(0.0, min(h - 1, iy))


def imagen_a_pantalla(ix, iy):
    px = int((ix - offset_x) * zoom)
    py = int((iy - offset_y) * zoom)
    return px, py


def render():
    h, w = imagen_original.shape[:2]

    # Calcular region visible en coords de imagen
    vis_x1 = int(offset_x)
    vis_y1 = int(offset_y)
    vis_x2 = min(w, int(offset_x + ANCHO_VENTANA / zoom) + 1)
    vis_y2 = min(h, int(offset_y + ALTO_VENTANA  / zoom) + 1)

    recorte = imagen_original[vis_y1:vis_y2, vis_x1:vis_x2]

    nuevo_w = min(ANCHO_VENTANA, int((vis_x2 - vis_x1) * zoom))
    nuevo_h = min(ALTO_VENTANA,  int((vis_y2 - vis_y1) * zoom))

    if nuevo_w <= 0 or nuevo_h <= 0:
        return

    canvas = cv2.resize(recorte, (nuevo_w, nuevo_h), interpolation=cv2.INTER_LINEAR)

    # Fondo negro si la imagen no llena la ventana
    if nuevo_w < ANCHO_VENTANA or nuevo_h < ALTO_VENTANA:
        fondo = np.zeros((ALTO_VENTANA, ANCHO_VENTANA, 3), dtype=np.uint8)
        fondo[:nuevo_h, :nuevo_w] = canvas
        canvas = fondo

    # Dibujar espacios guardados
    for i, (sx1, sy1, sx2, sy2) in enumerate(espacios):
        px1, py1 = imagen_a_pantalla(sx1, sy1)
        px2, py2 = imagen_a_pantalla(sx2, sy2)
        cv2.rectangle(canvas, (px1, py1), (px2, py2), (0, 220, 0), 2)
        cv2.putText(canvas, str(i + 1), (px1 + 4, py1 + 18),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 220, 0), 2)

    # Dibujar rectangulo de preview si hay primer punto
    if punto_ini is not None:
        px0, py0 = imagen_a_pantalla(punto_ini[0], punto_ini[1])
        cv2.circle(canvas, (px0, py0), 5, (0, 200, 255), -1)

        # Preview con la posicion actual del mouse
        mx, my = mouse_pos
        ix2, iy2 = pantalla_a_imagen(mx, my)
        pxm, pym = imagen_a_pantalla(ix2, iy2)
        cv2.rectangle(canvas, (px0, py0), (pxm, pym), (0, 200, 255), 1)

    # Info en pantalla
    estado = f"Espacios: {len(espacios)}  |  Zoom: {zoom:.1f}x"
    if punto_ini is not None:
        estado += "  |  Primer punto colocado, click para cerrar espacio"
    else:
        estado += "  |  Click para colocar primer punto"

    ayuda = "[Flechas] mover   [+/-/rueda] zoom   [U] deshacer   [S] guardar   [Q] salir"

    for texto, y, grosor_fondo in [(estado, 25, 2), (ayuda, 48, 2)]:
        cv2.putText(canvas, texto, (10, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.52, (0, 0, 0), grosor_fondo + 1)
        cv2.putText(canvas, texto, (10, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.52, (255, 255, 255), grosor_fondo)

    cv2.imshow('Definir espacios de parking', canvas)


def mouse_callback(event, px, py, flags, param):
    global punto_ini, espacios, offset_x, offset_y, zoom, mouse_pos

    mouse_pos = (px, py)

    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = pantalla_a_imagen(px, py)

        if punto_ini is None:
            punto_ini = (ix, iy)
        else:
            x1 = int(min(punto_ini[0], ix))
            y1 = int(min(punto_ini[1], iy))
            x2 = int(max(punto_ini[0], ix))
            y2 = int(max(punto_ini[1], iy))
            if x2 > x1 and y2 > y1:
                espacios.append((x1, y1, x2, y2))
                print(f"Espacio {len(espacios):>2}: ({x1}, {y1}, {x2}, {y2})")
            punto_ini = None

    elif event == cv2.EVENT_RBUTTONDOWN:
        # Click derecho cancela el punto inicial en curso
        punto_ini = None

    elif event == cv2.EVENT_MOUSEWHEEL:
        ix_antes, iy_antes = pantalla_a_imagen(px, py)
        factor = 1.15 if flags > 0 else 1 / 1.15
        zoom = max(ZOOM_MIN, min(ZOOM_MAX, zoom * factor))
        offset_x = ix_antes - px / zoom
        offset_y = iy_antes - py / zoom
        clamp_offset()

    elif event == cv2.EVENT_MOUSEMOVE:
        pass  # solo actualiza mouse_pos para el preview

    render()


def guardar():
    with open(OUTPUT_TXT, 'w') as f:
        f.write("# Espacios de parking: numero: x1, y1, x2, y2\n")
        f.write("# Copia el bloque de abajo en la celda del notebook\n\n")
        f.write("espacios_parking = {\n")
        for i, (x1, y1, x2, y2) in enumerate(espacios):
            f.write(f"    {i + 1}: ({x1}, {y1}, {x2}, {y2}),\n")
        f.write("}\n")
    print(f"Guardado: {OUTPUT_TXT}  ({len(espacios)} espacios)")


def main():
    global imagen_original, zoom, offset_x, offset_y

    if not os.path.exists(IMAGEN_PATH):
        print(f"ERROR: No se encontro la imagen: {IMAGEN_PATH}")
        sys.exit(1)

    imagen_original = cv2.imread(IMAGEN_PATH)
    if imagen_original is None:
        print(f"ERROR: No se pudo cargar la imagen: {IMAGEN_PATH}")
        sys.exit(1)

    h, w = imagen_original.shape[:2]
    print(f"Imagen: {w}x{h}  |  Salida: {OUTPUT_TXT}")

    # Ajustar zoom inicial para que la imagen quepa en la ventana
    zoom = min(ANCHO_VENTANA / w, ALTO_VENTANA / h, 1.0)

    cv2.namedWindow('Definir espacios de parking', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Definir espacios de parking', ANCHO_VENTANA, ALTO_VENTANA)
    cv2.setMouseCallback('Definir espacios de parking', mouse_callback)

    render()

    # Codigos de teclas de flecha (multiplataforma)
    ARRIBA    = {2490368, 65362, 63232}
    ABAJO     = {2621440, 65364, 63233}
    IZQUIERDA = {2424832, 65361, 63234}
    DERECHA   = {2555904, 65363, 63235}

    while True:
        key = cv2.waitKey(30)
        if key == -1:
            continue

        if key in ARRIBA:
            offset_y = max(0.0, offset_y - PAN_STEP / zoom)
            render()
        elif key in ABAJO:
            offset_y = min(h - ALTO_VENTANA / zoom, offset_y + PAN_STEP / zoom)
            clamp_offset()
            render()
        elif key in IZQUIERDA:
            offset_x = max(0.0, offset_x - PAN_STEP / zoom)
            render()
        elif key in DERECHA:
            offset_x = min(w - ANCHO_VENTANA / zoom, offset_x + PAN_STEP / zoom)
            clamp_offset()
            render()
        else:
            k = key & 0xFF
            if k in (ord('q'), 27):
                break
            elif k == ord('s'):
                guardar()
            elif k == ord('u'):
                if punto_ini is not None:
                    punto_ini = None
                    print("Primer punto cancelado")
                elif espacios:
                    print(f"Deshecho espacio {len(espacios)}: {espacios[-1]}")
                    espacios.pop()
                render()
            elif k in (ord('+'), ord('=')):
                zoom = min(ZOOM_MAX, zoom + ZOOM_STEP)
                clamp_offset()
                render()
            elif k == ord('-'):
                zoom = max(ZOOM_MIN, zoom - ZOOM_STEP)
                clamp_offset()
                render()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
