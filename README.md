# Proyecto-Imagenes-Subacuaticas

Nuestro proyecto fue realizado utilizando dos métodos para la limpieza de la imagen:

  - Sea Thru: originalmente este método fue seleccionado debido a que utilizaba mapas de profundidad para la limpieza de imágenes. Sin embargo, debido a complicaciones con la obtención de los mapas, se utiliza la metodología Sea Thru, pero en una versión donde se estima el mapa de profundidad.
  - WaveNet: este método fue escogido debido a que como grupo consideramos que es bastante eficaz, ya que a diferencia de Sea Thru, no reduce el tamaño de la imagen. Este método está basado en longitud de onda y utiliza redes neuronales.

El análisis comparativo realizado, fue puramente cualitativo, ya que por temas de tiempo no logramos implementar de manera correcta el cálculo de métricas. Para el análisis comparativo, se trabajo en conjunto con el grupo 8, el cual nos proporcionó su código y pudimos ver como se comporta el tracking de salmones, comida y heces. Como salida de la comparativa, pudimos notar que no hubo mejoría en la detección, esto se debe a que el modelo fue entrenado con imágenes que no fueron preprocesadas, por lo que darle una imagen limpia de entrada no va a generar mejores salidas. Sin embargo, consideramos que entrenar el modelo con imágenes limpias si mejoraría bastante el tracking, ya que permite reconocer de manera mucho más clara los elementos presentes en el video subacuático.

Como trabajo a futuro nos gustaría implementar la obtención de métricas para el análisis cuantitativo de los modelos, además de automatizar el código con ambos métodos preprocesados y la interfaz.
