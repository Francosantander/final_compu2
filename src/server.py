from aiohttp import web
import os
from functions import argumentos, get_file_type, get_name_file, clean_comments
from index import generar_index_0, generar_index_1, generar_index_2, generar_index_3, generar_index_4, generar_index_5
import datetime as dt
import asyncio
import array
from kml import process_kml


global abspath

routes = web.RouteTableDef()

@routes.get('/')
@routes.get('/index.html')
async def hello(request):
    addr = request.transport.get_extra_info('peername')
    asyncio.create_task(generar_logs(addr[0], addr[1]))
    abspath = os.getcwd()
    generar_index_0(abspath)
    return web.FileResponse(f"/{abspath}/html/index.html")

@routes.post('/')
@routes.post('/index.html')
async def post_handler(request):
    abspath = os.getcwd() + "/files/"
    data = await request.read()
    # Obtengo el tipo de formulario pasado en el post
    content_type = request.content_type
    if content_type == "multipart/form-data":
        if request.content_length > 225:
            # Obtengo el nombre del archivo
            file_type = get_file_type(data)
            if file_type == "application/vnd.google-earth.kml+xml": 
                file_name=get_name_file(data)
                # Limpio los comentarios que tiene el archivo
                data = clean_comments(data)
                # Guardo el archivo en el server
                output = open(abspath+file_name, "wb", os.O_CREAT)
                kml = array.array('b', data)
                kml.tofile(output)
                output.close()
                abspath = os.getcwd()
                generar_index_0(abspath)
            else:
                abspath = os.getcwd()
                generar_index_1(abspath)
        else:
            abspath = os.getcwd()
            generar_index_2(abspath)
    else:
        #Obtengo los datos del formulario para validar cobertura
        data = await request.text()
        data = data.splitlines()
        form = {}
        error = False
        for i in data:
            i = i.split('=')
            if i[1] != "":
                try:
                    form[i[0]] = float(i[1])
                    error = False
                except ValueError:
                    abspath = os.getcwd()
                    generar_index_3(abspath)
                    error = True
            else:
                abspath = os.getcwd()
                generar_index_4(abspath)
                error = True
        #Valido cobertura
        if error != True:
            abspath = os.getcwd() + "/files/"
            result = process_kml(abspath, form["lt"], form["lg"])
            if len(result) != 0:
                text = "Congratulation!!! You have coverage "
                print(text)
                abspath = os.getcwd()
                generar_index_5(abspath, text, result)
            else:
                text = "Sorry! You don't have coverage"
                print(text)
                abspath = os.getcwd()
                generar_index_5(abspath, text, result)

    return web.FileResponse(f"/{abspath}/html/index.html")


async def generar_logs(ip, port):
    time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = "| Cliente: {} | Puerto: {} | Fecha: {} |\n".format(ip, port, time)
    with open(f"{abspath}/log.txt", "a") as file:
        file.write(registro)
    file.close()


abspath = os.getcwd()
args = argumentos()
# path = os.getcwd()
generar_index_0(abspath)
app = web.Application()
app.add_routes(routes)
app.router.add_static("/", "./")
web.run_app(app, host=["0.0.0.0"], port=5000)
