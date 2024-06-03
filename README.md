# Aura: Manual de Usuario

¡Bienvenido a Aura! Nuestro sistema de biosensado más reciente, desarrollado con una atención meticulosa a la experiencia del usuario, te ofrece una manera intuitiva y potente de interactuar con los datos de tu EEG cap.

## Descripción General

Aura consta de una placa de biosensado y un gorro de EEG diseñados bajo una misma dirección de diseño. Este sistema proporciona una experiencia mejorada al usuario a través de la impresión en pantalla en el gorro, que indica la posición de cada electrodo, y una carcasa de biosensado más resistente y delgada impresa en 3D en SLS (sinterización láser selectiva).

## Tutorial de Uso

### Conexión en Vivo

Este será tu panel principal. Desde aquí, puedes iniciar una conexión en vivo haciendo clic en el botón "Conexión".

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_1.png  width="60%">

1. **Selecciona el Puerto COM Identificado**: Aquí selecciona tu puerto COM identificado para Aura y haz clic en "Conectar". En pocos segundos, comenzarás a recibir datos en vivo.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_2.png width="60%">

### Configuración de Electrodos

Asegúrate de que tus electrodos estén bien conectados y posicionados.

1. **Configuración de Electrodos**: Haz clic en "Archivo" -> "Configurar Electrodos" para abrir el panel de configuración. También puedes hacer clic en el icono de Configuración rápida en la esquina superior izquierda del cerebro.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_3.png width="60%">

2. **Ajuste de los Números de Canal de Electrodo**: Mueve los números de canal de electrodo para reflejar la configuración real de tu auricular Aura. Luego, guarda la configuración de posiciones con el botón sobre el cuero cabelludo.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_4.png width="60%">

3. **Indicadores de Calidad de Contacto en Tiempo Real**: Durante el ajuste de los electrodos en el cuero cabelludo, los indicadores de calidad de contacto se irán volviendo "buenos". El color rojo indica una mala conexión entre el cuero cabelludo y el electrodo correspondiente del número de canal del dispositivo, por lo que puede requerirse más gel conductor.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_5.png width="60%">

### Grabación

1. **Inicio de la Grabación**: Simplemente haz clic en el botón "Grabar" para comenzar a grabar.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_7.png width="60%">

2. **Directorio de Archivos Generados**: Durante una conexión en vivo, los archivos se generan automáticamente en la carpeta de Documentos de tu computadora, bajo ...Usuarios\[ tú ]\Documentos\Aura EEG Records. Puedes elegir tu propia carpeta de destino yendo a "Archivo" -> "Configuración" o haciendo clic en el icono de Guardar arriba del botón de Grabación.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_8.png width="60%">

3. **Registro de Eventos**: Durante la grabación, puedes presionar la barra espaciadora de tu teclado para registrar un evento en tu archivo CSV para referencia futura. Se indicará con un cambio de color en la luz de Evento.

 <img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_9.png width="60%">

### Transmisión

Mientras una conexión en vivo está activa, puedes activar o desactivar la casilla de verificación "LSL Stream Out". De esta manera, enviarás tus señales en bruto a través de la red. También funciona con tus sesiones grabadas.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_11.png width="60%">

#### Uso Avanzado: Integración con LSL y Python

Este documento explica los pasos para obtener datos en bruto del software Aura mediante el protocolo Lab Stream Layer (LSL) utilizando el lenguaje de programación Python. Para obtener más información sobre LSL, consulta: [Lab Stream Layer Documentation](https://labstreaminglayer.readthedocs.io/).

**Pasos:**

1. Abre el software Aura y comienza a leer las señales de EEG.

2. Haz clic en la casilla de verificación "LSL" ubicada encima de los gráficos para iniciar la transmisión de los datos de EEG en bruto. El software Aura genera automáticamente una capa de transmisión LSL llamada "AURA".

3. Para visualizar los datos de EEG en bruto, ejecuta el siguiente archivo: `1_LSL_read_raw_data.py`.

4. Para filtrar los datos en bruto provenientes de la transmisión LSL 'AURA', ejecuta el siguiente archivo: `2_LSL_filter_raw_data.py`. Este script leerá los datos en bruto, los filtrará y generará una nueva transmisión llamada "AURAFilteredEEG" y "AURAKalmanFilteredEEG".

5. Para utilizar solo 3 canales y calcular la potencia espectral de la frecuencia (PSD), ejecuta el archivo `4_LSL_3channel_Banpower`. Este script tomará solo los primeros tres electrodos y calculará la PSD para obtener la EEG_Bandpower, creando una nueva transmisión llamada "AURAPSD".

6. Para visualizar "AURAFilteredEEG" y "AURAKalmanFilteredEEG", puedes ejecutar `5_LSL_Graphic`.

7. Para calcular la potencia de banda de los datos filtrados, ejecuta el siguiente archivo:

   Este archivo recibe una transmisión LSL de ocho canales EEG con datos de EEG filtrados llamada "AURAFilteredEEG". La salida es una transmisión de 40 canales llamada 'EEG_BANDPOWER_X' que contiene valores normalizados de potencia de banda de las señales de entrada en la siguiente forma:

   - Delta CH1
   - Delta CH2
   - ...
   - Delta CH8

   - Theta CH1~CH8
   - Alpha CH1~CH8
   - Beta CH1~CH8
   - Gamma CH1~CH8

### Reproducción

1. **Carga de un Archivo CSV Grabado Anteriormente**: Haz clic en "Archivo" -> "Cargar Conjunto de Datos". Por ejemplo, puedes cargar una muestra de demostración haciendo clic en "Siguiente".

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_12.png width="60%">

2. **Exploración de Funciones de Reproducción**: Juega con todas las escalas y filtros para las señales. Por ejemplo, prueba el control deslizante de suavidad en el panel FFT.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_13.png width="60%">

3. **Visualización de Datos en el Modelo 3D del Cerebro**: Puedes rotar el modelo 3D del cerebro y seleccionar qué banda deseas visualizar con los botones debajo del cuero cabelludo.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_14.png width="60%">

### Acelerómetro y Giroscopio

También puedes verificar las señales de acelerómetro y giroscopio de tu Aura haciendo clic en esta pestaña.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_15.png width="60%">

Esto te desplegará el siguiente panel de visualización.

<img src=https://github.com/edgarhernandez94/ANUIES/blob/main/WAVEX/AURA_SDK/AuraTutorial1/AuraTutorial_16.png width="60%">

---

¡Esperamos que este manual te sea útil para sacar el máximo provecho de Aura! Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con nuestro equipo de soporte. ¡Disfruta explorando las capacidades de Aura integrado en Wavex!


 
