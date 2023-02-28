from aiohttp import web
import os
from functions import argumentos, get_file_type, get_name_file, clean_comments
from index import generar_index
import datetime as dt
import asyncio
import array
from kml import read_kml, verify_coverage

routes = web.RouteTableDef()

global abspath


@routes.get('/')
@routes.get('/index.html')
async def hello(request):
    addr = request.transport.get_extra_info('peername')
    asyncio.create_task(generar_logs(addr[0], addr[1]))
    return web.FileResponse(f"/{abspath}/html/index.html")

@routes.post('/')
async def post_handler(request):
    abspath = os.getcwd() + "/files/"
    data = await request.read()
    # Con hilos podria obtener el nombre, otro que limpie la cabecera y por ultimo limpie el footer.
    try:
        # Obtengo el tipo de formulario pasado en el post
        type_file = get_file_type(data)
        if type_file == "kml":
            # Obtengo el nombre del archivo
            file_name=get_name_file(data)
            # Limpio los comentarios que tiene el archivo
            data = clean_comments(data)
            # Guardo el archivo en el server
            output = open(abspath+file_name, "wb", os.O_CREAT)
            imagen_nueva = array.array('b', data)
            imagen_nueva.tofile(output)
            output.close()
    except:
        #Obtengo los datos del formulario para validar cobertura
        data = await request.text()
        data = data.splitlines()
        form = {}
        for i in data:
            i = i.split('=')
            form[i[0]] = i[1]
        #Valido cobertura
        # Terminar de aplicar hilos
        kml = read_kml(abspath + form["file"])
        result = verify_coverage(kml, form["lt"], form["lg"])
        if len(result) != 0:
            print("You have coverage")
            print(result)
            print('\n')
        else:
            print("You don't have coverage")

    abspath = os.getcwd()
    generar_index(abspath)
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
generar_index(abspath)
app = web.Application()
app.add_routes(routes)
app.router.add_static("/", "./")
# Cambiar la ipv6 por la de la pc
web.run_app(app, host=["192.168.100.23", "::1"], port=args.port)
