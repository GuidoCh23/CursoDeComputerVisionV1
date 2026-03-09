# Proyectos Finales - Deteccion de Objetos con YOLOv11

Guido Anthony Chipana Calderon

---

## Instrucciones Generales

Cada estudiante puede seleccionar **uno** de los siguientes proyectos y desarrollarlo completamente siguiendo los requisitos del curso:

**Entregables:**
- Modelo entrenado (best.pt)
- Notebook de entrenamiento documentado
- Graficas de resultados (results.png, confusion_matrix.png)
- Video de inferencia en dataset de prueba
- Analisis de metricas (mAP, precision, recall)
- Documentacion en README.md

---

## Proyecto 1: Sistema de Deteccion de EPP en Obras de Construccion

### Problematica

Las empresas constructoras enfrentan altos indices de accidentes laborales por falta de equipos de proteccion personal (EPP). Segun estadisticas del Ministerio de Trabajo, el 60% de accidentes graves podrian prevenirse con uso correcto de cascos, chalecos y botas de seguridad. Un sistema automatizado de deteccion de EPP mediante camaras de seguridad permitiria identificar trabajadores sin proteccion en tiempo real y generar alertas automaticas, reduciendo significativamente el riesgo de accidentes.

### Dataset

**Construction Site Safety (RF100)**
- **URL:** https://universe.roboflow.com/roboflow-100/construction-safety-gsnvb
- **Imagenes:** 2,801
- **Clases:** 10 (casco, chaleco, guantes, maquinaria pesada, persona con EPP, persona sin EPP, conos de seguridad, excavadora, hormigonera, andamio)
- **Formato:** YOLOv8 (exportable a YOLOv11)
- **Split:** Train/Val/Test predefinido

**Alternativa (dataset mas grande):**
- **SH17 Dataset:** https://www.kaggle.com/datasets/mugheesahmad/sh17-dataset-for-ppe-detection
- **Imagenes:** 8,099
- **Clases:** 17 (incluye proteccion auditiva, zapatos de seguridad, hairnet)

### Modelos Recomendados

- **YOLOv11s** (recomendado para balance precision/velocidad)
- **YOLOv11m** (si se busca mayor precision)
- **YOLOv11n** (para pruebas rapidas)

---

## Proyecto 2: Detector de Productos en Estantes de Supermercado

### Problematica

Los supermercados pierden millones en ventas por productos fuera de stock o mal ubicados en estantes. El proceso manual de verificacion de inventario es lento, costoso y propenso a errores. Un sistema de deteccion automatica mediante camaras instaladas en pasillos permitiria monitorear en tiempo real el nivel de stock, detectar productos mal colocados, y generar alertas automaticas de reabastecimiento. Esta tecnologia ya es utilizada por cadenas como Amazon Go y Walmart en mercados desarrollados.

### Dataset

**SKU-110K (CVPR 2019)**
- **URL:** https://docs.ultralytics.com/datasets/detect/sku-110k/
- **Imagenes:** 11,762 (con ~154 objetos por imagen en promedio)
- **Clases:** 1 (producto generico - deteccion densa)
- **Formato:** YOLO nativo (Ultralytics)
- **Split:** 8,219 train / 588 val / 2,941 test

**Alternativa (categorias especificas):**
- **Groceries Dataset:** https://universe.roboflow.com/samrat-sahoo/groceries-6pfog
- **Imagenes:** ~83,700
- **Clases:** Multiples categorias de productos, talvez mejor opcion

### Modelos Recomendados

- **YOLOv11m** (recomendado - escenas densas requieren mayor capacidad)
- **YOLOv11s** (alternativa si se piensa en ejecutar en dispositivos con recursos limitados)

---

## Proyecto 3: Detector de Fauna Silvestre para Reservas Naturales

### Problematica

Las reservas naturales y parques nacionales necesitan monitorear poblaciones de fauna silvestre para estudios de conservacion, pero los metodos tradicionales (conteo manual, trampas de camara con revision humana) son extremadamente laboriosos. Un sistema automatizado de deteccion de animales mediante camaras trampa con IA permitiria clasificar automaticamente las especies capturadas, generar estadisticas poblacionales, y alertar sobre presencia de especies en peligro o invasoras. Organizaciones como Wildlife Insights ya implementan esta tecnologia a nivel global.

### Dataset

**African Wildlife (Ultralytics)**
- **URL:** https://docs.ultralytics.com/datasets/detect/african-wildlife/
- **Imagenes:** 1,504
- **Clases:** 4 (buffalo, elephant, rhino, zebra)
- **Formato:** YOLO nativo (Ultralytics)
- **Split:** 1,052 train / 225 val / 227 test

**Alternativa (mas especies):**
- **Wildlife YOLO Format:** https://www.kaggle.com/datasets/ankanghosh651/object-detection-wildlife-dataset-yolo-format
- **Imagenes:** ~2,000+
- **Clases:** 10+ especies (zebras, pandas, leones, tigres, osos, etc.)

### Modelos Recomendados

- **YOLOv11s** (recomendado - dataset pequeño)
- **YOLOv11n** (para deployment en dispositivos con recursos limitados en el campo)
---

## Proyecto 4: Sistema de Deteccion de Enfermedades en Cultivos Agricolas

### Problematica

Las enfermedades en cultivos agricolas causan perdidas millonarias anuales. La deteccion temprana es critica, pero el diagnostico manual requiere expertos agronomos y es costoso. Un sistema de deteccion automatica mediante drones o camaras moviles permitiria a pequeños agricultores identificar enfermedades en etapas tempranas usando solo un smartphone, democratizando el acceso a diagnostico profesional y reduciendo el uso de pesticidas mediante tratamiento focalizado.

### Dataset

**PlantVillage YOLO Format**
- **URL:** https://www.kaggle.com/datasets/sebastianpalaciob/plantvillage-for-object-detection-yolo
- **Imagenes:** ~54,306 (dataset original)
- **Clases:** 38 (14 cultivos × tipos de enfermedades)
- **Formato:** YOLO adaptado
- **Split:** Configurable (sugerido 70/20/10)
- **Cultivos:** Tomate, papa, maiz, uva, manzana, pimiento, fresa, etc.

**Alternativa (cultivo vs maleza):**
- **Crop and Weed Detection:** https://www.kaggle.com/datasets/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes
- **Imagenes:** 1,300
- **Clases:** 2 (cultivo, maleza)

### Modelos Recomendados

- **YOLOv11m** (recomendado - 38 clases requieren mayor capacidad)
- **YOLOv11s** (alternativa con menor precision pero mas rapido)

---

## Proyecto 5: Detector de Defectos en Superficies de Acero

### Problematica

La industria siderurgica y manufacturera requiere inspeccion de calidad exhaustiva para detectar defectos superficiales (grietas, rayaduras, inclusiones) que comprometen la integridad estructural del material. La inspeccion visual manual es lenta, subjetiva y costosa. Un sistema automatizado de deteccion de defectos mediante vision artificial permitiria inspeccion 100% de produccion en tiempo real, reduciendo productos defectuosos que llegan al cliente y mejorando significativamente el control de calidad.

### Dataset

**NEU Surface Defect Database (NEU-DET)**
- **URL:** https://www.kaggle.com/datasets/sovitrath/neu-steel-surface-defect-detect-trainvalid-split
- **Imagenes:** 1,800
- **Clases:** 6 (crazing, inclusion, patches, pitted_surface, rolled-in_scale, scratches)
- **Formato:** YOLO (version pre-convertida)
- **Split:** Train/Val predefinido
- **Benchmark:** Mas de 100 papers academicos lo utilizan

**Dataset original (requiere conversion):**
- http://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/

### Modelos Recomendados

- **YOLOv11s** (recomendado - dataset pequeño, 6 clases)
- **YOLOv11m** (si se requiere maxima precision)

---

## Proyecto 6: Sistema de Conteo Vehicular y Analisis de Trafico

### Problematica

Las municipalidades y ministerios de transporte requieren datos precisos de flujo vehicular para planificacion urbana, sincronizacion de semaforos, y estudios de congestion. Los metodos tradicionales (contadores manuales, sensores de piso) son costosos y limitados. Un sistema de deteccion y tracking vehicular mediante camaras de trafico existentes permitiria obtener estadisticas detalladas (conteo por tipo de vehiculo, velocidad promedio, direccion de flujo) con inversion minima, reutilizando infraestructura ya instalada.

### Dataset

**Vehicle Dataset for YOLO**
- **URL:** https://www.kaggle.com/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo
- **Imagenes:** 3,000
- **Clases:** 6 (car, bus, truck, motorbike, van, three-wheeler)
- **Formato:** YOLO nativo
- **Split:** 2,100 train / 900 test
- **Contexto:** Dataset compilado especificamente para YOLO

**Alternativa (benchmark academico):**
- **KITTI Object Detection:** https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d
- **Imagenes:** 14,999
- **Clases:** 9 (incluye pedestrian, cyclist)
- **Nota:** Requiere conversion de formato

### Modelos Recomendados

- **YOLOv11s** (recomendado - balance velocidad/precision)
- **YOLOv11m** (para mayor precision en clasificacion de tipos)
- **YOLOv11n** (para inferencia en tiempo real con recursos limitados)

### Video de Prueba

**URL:** https://www.youtube.com/watch?v=MNn9qKG2UFI

**Descripcion:** Trafico urbano en interseccion con multiples tipos de vehiculos. Duracion: 5 minutos. Ideal para implementar sistema de conteo con lineas virtuales. Incluye carros, buses, motocicletas, camiones.

**Videos alternativos:**
- https://www.youtube.com/watch?v=wqctLW0Hb_0 (highway traffic)

---

## Proyecto 7: Detector de Peatones para Sistemas de Conduccion Asistida

### Problematica

Los accidentes de transito involucrando peatones son una de las principales causas de muerte en zonas urbanas. Los sistemas avanzados de asistencia al conductor (ADAS) requieren deteccion precisa y rapida de peatones para alertas de colision y frenado automatico de emergencia. Un detector robusto de peatones debe funcionar en condiciones adversas (poca luz, lluvia, oclusiones parciales) y con latencia minima para ser efectivo como sistema de seguridad vehicular.

### Dataset

**People Detection (Roboflow)**
- **URL:** https://universe.roboflow.com/leo-ueno/people-detection-o4rdr/10
- **Imagenes:** 17,401
- **Clases:** 1 (person)
- **Formato:** Multi-formato YOLO (exportable)
- **Split:** 15,210 train / 1,431 val / 760 test
- **Caracteristicas:** Alta variedad de escenarios, multiples oclusiones

**Alternativa (contexto urbano):**
- **CityPerson Pedestrian:** https://universe.roboflow.com/cityperson-yolo-homework/pedestrian-detection-bfv8t/dataset/2
- **Imagenes:** 2,975

### Modelos Recomendados

- **YOLOv11s** (recomendado - inferencia rapida necesaria)
- **YOLOv11m** (para maxima precision en deteccion)
- **YOLOv11n** (para deployment en vehiculos)

---

## Proyecto 8: Sistema de Deteccion de Señales de Transito

### Problematica

Los sistemas de conduccion autonoma y asistida requieren reconocimiento preciso de señales de transito para navegacion segura. La deteccion debe ser robusta a diferentes condiciones climaticas, angulos de vision, degradacion de señales, y oclusiones parciales. Un sistema efectivo de deteccion de señales es componente critico de cualquier vehiculo autonomo nivel 3+ y puede asistir a conductores humanos mediante sistemas de alerta (exceso de velocidad, señal de alto ignorada).

### Dataset

**Traffic and Road Signs (Roboflow)**
- **URL:** https://universe.roboflow.com/usmanchaudhry622-gmail-com/traffic-and-road-signs
- **Imagenes:** ~10,000
- **Clases:** 29 (speed limits, stop, give way, no entry, crosswalk, etc.)
- **Formato:** Multi-formato YOLO
- **Split:** Train/Val/Test predefinido

**Alternativa (benchmark aleman):**
- **GTSDB (German Traffic Sign Detection):** https://universe.roboflow.com/mohamed-traore-2ekkp/gtsdb---german-traffic-sign-detection-benchmark
- **Imagenes:** ~900
- **Clases:** 20-43

### Modelos Recomendados

- **YOLOv11m** (recomendado - 29 clases requieren capacidad)
- **YOLOv11s** (alternativa mas rapida)

---

## Proyecto 9: Detector de Uso de Mascarillas (Post-Pandemia)

### Problematica

Aunque la pandemia de COVID-19 ha disminuido, los sistemas de deteccion de uso de mascarillas siguen siendo relevantes para hospitales, clinicas, laboratorios, y zonas industriales con requerimientos de proteccion respiratoria. Un sistema automatizado permitiria controlar acceso a areas restringidas, generar alertas de incumplimiento de protocolos, y mantener registros automaticos de compliance en entornos donde la proteccion respiratoria es obligatoria permanentemente.

### Dataset

**Face Masks Composite (HuggingFace)**
- **URL:** https://huggingface.co/datasets/hlydecker/face-masks
- **Imagenes:** 9,982 (24,975 anotaciones)
- **Clases:** 2 (with_mask, without_mask)
- **Formato:** YOLO nativo
- **Split:** Train/Val/Test predefinido
- **Caracteristicas:** Dataset mas grande disponible

**Alternativa (3 clases):**
- **Face Mask Detection (Kaggle):** https://www.kaggle.com/datasets/andrewmvd/face-mask-detection
- **Imagenes:** 853
- **Clases:** 3 (with_mask, without_mask, mask_weared_incorrect)

### Modelos Recomendados

- **YOLOv11s** (recomendado - solo 2 clases)
- **YOLOv11n** (para deployment en camaras de acceso)

---

## Proyecto 10: Sistema de Deteccion Temprana de Incendios

### Problematica

Los incendios forestales y urbanos causan perdidas de vidas y millones en daños. La deteccion temprana es critica - cada minuto cuenta. Los sistemas tradicionales (detectores de humo) fallan en espacios abiertos. Un sistema de deteccion de fuego y humo mediante camaras de vigilancia o drones permitiria identificar conatos de incendio en segundos, alertar automaticamente a bomberos con ubicacion GPS precisa, y monitorear la evolucion del incendio en tiempo real para coordinacion de respuesta.

### Dataset

**D-Fire Dataset**
- **URL:** https://github.com/gaiasd/DFireDataset
- **Imagenes:** ~21,000
- **Clases:** 2 (fire, smoke)
- **Formato:** YOLO nativo
- **Split:** Train/Val/Test predefinido
- **Publicacion:** Neural Computing and Applications (dataset academico validado)

**Alternativa (Roboflow):**
- **Fire and Smoke Detection (METU):** https://universe.roboflow.com/middle-east-tech-university/fire-and-smoke-detection-hiwia
- **Imagenes:** ~6,391

### Modelos Recomendados

- **YOLOv11s** (recomendado - solo 2 clases, inferencia rapida critica)
- **YOLOv11n** (para deployment en drones)
- **YOLOv11m** (para maxima precision en deteccion temprana)

---

## Proyecto 11: Clasificador de Residuos para Reciclaje Automatizado

### Problematica

Solo el 20% de residuos solidos se recicla correctamente en Latinoamerica. La clasificacion manual es lenta, insalubre y costosa. Un sistema de vision artificial para clasificacion automatica de residuos permitiria a plantas de reciclaje aumentar drasticamente su throughput, mejorar pureza de materiales reciclados, y reducir contaminacion cruzada. Ciudades como San Francisco y Amsterdam ya implementan sistemas automatizados con tasas de reciclaje superiores al 80%.

### Dataset

**TACO (Trash Annotations in Context)**
- **URL Dataset Original:** http://tacodataset.org/
- **URL Version YOLO:** https://www.kaggle.com/datasets/vencerlanz09/taco-dataset-yolo-format
- **Imagenes:** 1,500 (4,784+ anotaciones)
- **Clases:** 60 categorias jerarquicas (agrupables en 6-8 principales)
- **Formato:** YOLO (version Kaggle)
- **Licencia:** CC BY 4.0
- **Caracteristicas:** Dataset peer-reviewed, contexto real

**Alternativa (mayor volumen):**
- **Garbage Classification YOLO:** https://www.kaggle.com/datasets/spellsharp/garbage-data
- **Imagenes:** ~15,000+
- **Clases:** 6-12

### Modelos Recomendados

- **YOLOv11m** (recomendado - 60 clases jerarquicas)
- **YOLOv11s** (si se agrupan en 6-8 clases principales)

---

## Proyecto 12: Detector de Frutas para Agricultura de Precision

### Problematica

La agricultura de precision requiere estimacion precisa de rendimiento de cultivos antes de cosecha para planificacion logistica y pricing. El conteo manual de frutas es imposible en plantaciones grandes. Un sistema de deteccion y conteo de frutas mediante drones o tractores autonomos permitiria obtener estimaciones de rendimiento campo por campo, detectar maduracion optima para cosecha selectiva, y optimizar rutas de recoleccion, aumentando eficiencia de cosecha hasta 40%.

### Dataset

**Combined Vegetables & Fruits (Roboflow)**
- **URL:** https://universe.roboflow.com/yolo-jpkho/combined-vegetables-fruits
- **Imagenes:** ~41,985
- **Clases:** 47 (apple, banana, avocado, strawberry, orange, lemon, grape, watermelon, etc.)
- **Formato:** Multi-formato YOLO
- **Split:** Train/Val/Test predefinido
- **Caracteristicas:** Dataset muy grande, alta variedad

**Alternativa (foco en frutas especificas):**
- **Fruits & Veg Detection YOLOv4:** https://www.kaggle.com/datasets/kvnpatel/fruits-vegetable-detection-for-yolov4
- **Imagenes:** 4,592
- **Clases:** 14 (incluye frutas en bolsas semi-transparentes)

### Modelos Recomendados

- **YOLOv11m** (recomendado - 47 clases requieren capacidad)
- **YOLOv11l** (para maxima precision en clasificacion)

---

## Proyecto 13: Reconocedor de Objetos de Cocina para Asistentes Culinarios

### Problematica

Los asistentes de cocina inteligentes y robots culinarios requieren identificacion de ingredientes y utensilios para proveer instrucciones contextuales. Un usuario podria preguntarle a su asistente "que puedo cocinar con estos ingredientes?" y el sistema, usando vision artificial, identificaria los ingredientes disponibles y sugeriria recetas. Aplicaciones comerciales incluyen apps de gestion de despensa, conteo de calorias automatico, y robots de cocina como Moley que requieren identificar utensilios para manipulacion.

### Dataset

**Kitchen Utensils Recognition (Roboflow)**
- **URL:** https://universe.roboflow.com/table-utensils-detector/kitchen-utensils-recognition
- **Imagenes:** 879
- **Clases:** ~20 (tongs, bread knife, ladle, whisk, spatula, peeler, grater, rolling pin, measuring cup, cutting board, etc.)
- **Formato:** Multi-formato YOLO
- **Split:** Train/Val/Test predefinido

**Alternativa (mayor coverage - COCO subset):**
- **MS COCO Kitchen Objects:** https://cocodataset.org/
- **Clases:** ~20 (fork, knife, spoon, bowl, cup, wine glass, oven, toaster, microwave, refrigerator, sink)
- **Integracion:** Filtrar clases de cocina del dataset COCO completo

### Modelos Recomendados

- **YOLOv11s** (recomendado - 20 clases)
- **YOLOv11m** (para mayor precision en clasificacion)

---

## Proyecto 14: Detector de Herramientas para Inventario de Taller

### Problematica

Los talleres mecanicos y de manufactura pierden tiempo valioso buscando herramientas extraviadas. El inventario manual es tedioso y propenso a errores. Un sistema de vision artificial instalado en areas de trabajo permitiria tracking automatico de herramientas, alertas de herramientas faltantes antes de cerrar turno, y asistencia a tecnicos ("donde esta la llave de 14mm?" - "cajon 3, compartimento B"). Empresas aeroespaciales como Boeing ya implementan FOD (Foreign Object Debris) detection para prevenir herramientas olvidadas en aeronaves.

### Dataset

**Mechanical Tools-10000 (Roboflow)**
- **URL:** https://universe.roboflow.com/mechanical-tools/mechanical-tools-10000/dataset/3
- **Imagenes:** 9,302
- **Clases:** Multiple (hammers, wrenches, screwdrivers, pliers, allen keys, socket sets, etc.)
- **Formato:** Multi-formato YOLO
- **Split:** Train/Val/Test predefinido

**Alternativa (menor volumen):**
- **Tool Detection (Roboflow):** https://universe.roboflow.com/object-detection-yolo-c8gsd/tool-detection-0xiup
- **Imagenes:** ~275
- **Clases:** 17

### Modelos Recomendados

- **YOLOv11m** (recomendado - multiple clases de herramientas)
- **YOLOv11s** (alternativa mas rapida)

---

## Proyecto 15: Sistema de Deteccion de Drones No Autorizados

### Problematica

Los drones no autorizados representan amenazas de seguridad en aeropuertos, prisiones, instalaciones militares, y eventos masivos. Los sistemas tradicionales (radar) tienen alta tasa de falsos positivos con aves. Un sistema de deteccion visual de drones permitiria discriminar entre drones y aves, activar contramedidas (jamming, captura con nets), y generar alertas tempranas con trayectoria predicha. Aeropuertos como Gatwick han sufrido cierres costosos por drones, impulsando demanda de estos sistemas.

### Dataset

**Drone Detection 10K (Roboflow)**
- **URL:** https://universe.roboflow.com/drone-detection-g4d3g/drone-detection-a1tsf
- **Imagenes:** 10,000
- **Clases:** 1-2 (drone, bird)
- **Formato:** YOLOv8 (exportable a v11)
- **Split:** Train/Val/Test predefinido
- **Caracteristicas:** Dataset grande, variedad de drones

**Alternativa (Kaggle):**
- **YOLO Drone Detection:** https://www.kaggle.com/datasets/muki2003/yolo-drone-detection-dataset
- **Imagenes:** ~1,359
- **Clases:** 1

### Modelos Recomendados

- **YOLOv11m** (recomendado - objetos pequeños requieren precision)
- **YOLOv11l** (para maxima precision en deteccion a larga distancia)
- **YOLOv11s** (balance precision/velocidad)

---

## Recomendaciones Finales

### Seleccion de Proyecto

- **Dataset pequeño (menos 2000 imgs):** Usar YOLOv11n o YOLOv11s para evitar overfitting
- **Dataset medio (2000-10000):** Usar YOLOv11s o YOLOv11m segun complejidad
- **Dataset grande (mas 10000):** Usar YOLOv11m o YOLOv11l para aprovechar datos

### Configuracion de Entrenamiento

```python
model = YOLO('yolo11s.pt')

results = model.train(
    data='data.yaml',
    epochs=80-100,
    batch=16,
    lr0=0.001,          # Fine-tuning
    optimizer='AdamW',
    patience=30,
    augmentation='moderate'  # Ajustar segun dataset
    freeze=0 # Ajustar dependiendo de tu enfoque, por defecto 0
)
```

### Video de Prueba

1. Descargar video de YouTube
2. Descargar video de Pexels(https://www.pexels.com/) o Pixabay(https://pixabay.com/)

### Recursos Adicionales

- **Roboflow Universe:** https://universe.roboflow.com/
- **Ultralytics Docs:** https://docs.ultralytics.com/
- **Kaggle Datasets:** https://www.kaggle.com/datasets
- **GitHub Surface Defect:** https://github.com/Charmve/Surface-Defect-Detection (20+ datasets industriales)

---

**Fecha:** Marzo 2026  
**Contacto:** guidochipana23@gmail.com
