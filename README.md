# final_compu2
Computacion final proyect repo

En la realizacion de este proyecto lo que se quiero hacer es un file server que además pueda validar coberturas geográficas.

En el mismo se podrán subir o descargar mapas geográficos en formato KML y a su vez el file server contará con la capacidad de validar si una coordenada en el plano, el cual se ingresará mediante un formulario, se encuentra dentro de la cobertura de alguno de los mapas que tiene almacenado el storage del file server

Elegí este proyecto ya que para empresas que venden, por ejemplo servicio de internet(Wireless o Fibra Óptica), les permitirá saber si un usuario al que le quieren vender internet, se encuentra dentro de su área de cobertura.

Para la elaboracion del mismo se usara:

- Aiohttp para levantar el server multicliente junto a la libreria asyncio para realizar consultas asincronas
- Paralelismo mediante hilos para leer los mapas kml y verificar la cobertura
- Mecanismo IPC: Se utilizara memoria compartida para almacenar la respuesta acerca de la validación de la cobertura
- Sincronismo: Se utilizara Locks para sincronizar los hilos entre sí y no sobreescribir la respuesta en la variable global
- Parseo de argumentos por línea de comandos(-p o --port)
- Manejo de errores para validar que los archivos subidos al Server sean del tipo KML, como asi tambien verificar los datos ingresados mediante el formulario de la latitud y longitud

Funcionalidades del server:

- Descargar archivos KML
- Subir archivos KML
- Verificar la cobertura de una persona en los mapas almacenados en el file Server.
