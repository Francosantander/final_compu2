from os import scandir
import os


def generar_index_0(abspath):
    html = "<!DOCTYPE html>\n<html>\n<head><meta charset=\"UTF-8\">\n<link rel='stylesheet' type='text/css' href='../assets/css/index.css'>\n<title>Index</title>\n</head>\n<body>\n"
    html += "<div class='home-container'>\n\t<h2>Geocoverage</h2>\n<div class='kml-list'>\n\t<h4>Files KML:</h4>"
    path = os.getcwd() + "/files"
    archivos = [obj.name for obj in scandir(path) if obj.is_file()]
    for archivo in archivos:
        if ".py" not in archivo:
            html += "<li><a href=\"files/{}\">{}</a></li>\n".format(archivo, archivo)
    html += """ 
                </div>
                <br/>
                <br/>
                <form method="post" enctype="multipart/form-data" class="form-file-input">
                    <div>
                        <label for="kml">Choose file to upload</label>
                        <br/>
                        <br/>
                        <input
                        type="file"
                        id="kml"
                        name="kml"
                        accept=".kml"
                        />
                    </div>
                    <br/>
                    <div>
                        <button>Submit</button>
                    </div>
                </form>"""
    html += """ <br/>
                <br/>
                <form method="post" enctype="text/plain" class="form-coordinates-input">
                    <label>Verify your coverage</label>
                    <br/>
                    <div>
                            <input
                            type="text"
                            id="lt"
                            name="lt"
                            placeholder="LT, ej:-33.0801393"
                            />
                            <br/>
                            <input
                            type="text"
                            id="lg"
                            name="lg"
                            placeholder="LG, ej:-68.97434"
                            />
                    </div>
                    <br/>
                    <div>
                        <button>Verify</button>
                    </div>
                </form></div>"""
    html += "</body>\n</html>"
    file = open(f"{abspath}/html/index.html", "w")
    file.write(html)
    file.close()

def generar_index_1(abspath):
    html = "<!DOCTYPE html>\n<html>\n<head><meta charset=\"UTF-8\">\n<link rel='stylesheet' type='text/css' href='../assets/css/index.css'>\n<title>Index</title>\n</head>\n<body>\n"
    html += "<div class='home-container'>\n\t<h2>Geocoverage</h2>\n<div class='kml-list'>\n\t<h4>Files KML:</h4>"
    path = os.getcwd() + "/files"
    archivos = [obj.name for obj in scandir(path) if obj.is_file()]
    for archivo in archivos:
        if ".py" not in archivo:
            html += "<li><a href=\"files/{}\">{}</a></li>\n".format(archivo, archivo)
    html += """ 
                </div>
                <br/>
                <br/>
                <form method="post" enctype="multipart/form-data" class="form-file-input">
                    <div>
                        <label for="kml">Choose file to upload</label>
                        <br/>
                        <br/>
                        <input
                        type="file"
                        id="kml"
                        name="kml"
                        accept=".kml"
                        />
                    </div>
                    <br/>
                    <div>
                        <button>Submit</button>
                        <br/>
                        <h5 class="error-type-file">File server only accept kml files</h5>
                    </div>
                </form>"""
    html += """ <br/>
                <br/>
                <form method="post" enctype="text/plain" class="form-coordinates-input">
                    <label>Verify your coverage</label>
                    <br/>
                    <div>
                            <input
                            type="text"
                            id="lt"
                            name="lt"
                            placeholder="LT, ej:-33.0801393"
                            />
                            <br/>
                            <input
                            type="text"
                            id="lg"
                            name="lg"
                            placeholder="LG, ej:-68.97434"
                            />
                    </div>
                    <br/>
                    <div>
                        <button>Verify</button>
                    </div>
                </form></div>"""
    html += "</body>\n</html>"
    file = open(f"{abspath}/html/index.html", "w")
    file.write(html)
    file.close()

def generar_index_2(abspath):
    html = "<!DOCTYPE html>\n<html>\n<head><meta charset=\"UTF-8\">\n<link rel='stylesheet' type='text/css' href='../assets/css/index.css'>\n<title>Index</title>\n</head>\n<body>\n"
    html += "<div class='home-container'>\n\t<h2>Geocoverage</h2>\n<div class='kml-list'>\n\t<h4>Files KML:</h4>"
    path = os.getcwd() + "/files"
    archivos = [obj.name for obj in scandir(path) if obj.is_file()]
    for archivo in archivos:
        if ".py" not in archivo:
            html += "<li><a href=\"files/{}\">{}</a></li>\n".format(archivo, archivo)
    html += """ 
                </div>
                <br/>
                <br/>
                <form method="post" enctype="multipart/form-data" class="form-file-input">
                    <div>
                        <label for="kml">Choose file to upload</label>
                        <br/>
                        <br/>
                        <input
                        type="file"
                        id="kml"
                        name="kml"
                        accept=".kml"
                        />
                    </div>
                    <br/>
                    <div>
                        <button>Submit</button>
                        <br/>
                        <h5 class="error-type-file">Please upload kml file does not empty</h5>
                    </div>
                </form>"""
    html += """ <br/>
                <br/>
                <form method="post" enctype="text/plain" class="form-coordinates-input">
                    <label>Verify your coverage</label>
                    <br/>
                    <div>
                            <input
                            type="text"
                            id="lt"
                            name="lt"
                            placeholder="LT, ej:-33.0801393"
                            />
                            <br/>
                            <input
                            type="text"
                            id="lg"
                            name="lg"
                            placeholder="LG, ej:-68.97434"
                            />
                    </div>
                    <br/>
                    <div>
                        <button>Verify</button>
                    </div>
                </form></div>"""
    html += "</body>\n</html>"
    file = open(f"{abspath}/html/index.html", "w")
    file.write(html)
    file.close()

def generar_index_3(abspath):
    html = "<!DOCTYPE html>\n<html>\n<head><meta charset=\"UTF-8\">\n<link rel='stylesheet' type='text/css' href='../assets/css/index.css'>\n<title>Index</title>\n</head>\n<body>\n"
    html += "<div class='home-container'>\n\t<h2>Geocoverage</h2>\n<div class='kml-list'>\n\t<h4>Files KML:</h4>"
    path = os.getcwd() + "/files"
    archivos = [obj.name for obj in scandir(path) if obj.is_file()]
    for archivo in archivos:
        if ".py" not in archivo:
            html += "<li><a href=\"files/{}\">{}</a></li>\n".format(archivo, archivo)
    html += """ 
                </div>
                <br/>
                <br/>
                <form method="post" enctype="multipart/form-data" class="form-file-input">
                    <div>
                        <label for="kml">Choose file to upload</label>
                        <br/>
                        <br/>
                        <input
                        type="file"
                        id="kml"
                        name="kml"
                        accept=".kml"
                        />
                    </div>
                    <br/>
                    <div>
                        <button>Submit</button>
                    </div>
                </form>"""
    html += """ <br/>
                <br/>
                <form method="post" enctype="text/plain" class="form-coordinates-input">
                    <label>Verify your coverage</label>
                    <br/>
                    <div>
                            <input
                            type="text"
                            id="lt"
                            name="lt"
                            placeholder="LT, ej:-33.0801393"
                            />
                            <br/>
                            <input
                            type="text"
                            id="lg"
                            name="lg"
                            placeholder="LG, ej:-68.97434"
                            />
                    </div>
                    <br/>
                    <div>
                        <button>Verify</button>
                        <br/>
                        <h5 class="error-type-file">Please entry a float input</h5>
                    </div>
                </form>"""
    html += "</body>\n</html>"
    file = open(f"{abspath}/html/index.html", "w")
    file.write(html)
    file.close()

def generar_index_4(abspath):
    html = "<!DOCTYPE html>\n<html>\n<head><meta charset=\"UTF-8\">\n<link rel='stylesheet' type='text/css' href='../assets/css/index.css'>\n<title>Index</title>\n</head>\n<body>\n"
    html += "<div class='home-container'>\n\t<h2>Geocoverage</h2>\n<div class='kml-list'>\n\t<h4>Files KML:</h4>"
    path = os.getcwd() + "/files"
    archivos = [obj.name for obj in scandir(path) if obj.is_file()]
    for archivo in archivos:
        if ".py" not in archivo:
            html += "<li><a href=\"files/{}\">{}</a></li>\n".format(archivo, archivo)
    html += """ 
                </div>
                <br/>
                <br/>
                <form method="post" enctype="multipart/form-data" class="form-file-input">
                    <div>
                        <label for="kml">Choose file to upload</label>
                        <br/>
                        <br/>
                        <input
                        type="file"
                        id="kml"
                        name="kml"
                        accept=".kml"
                        />
                    </div>
                    <br/>
                    <div>
                        <button>Submit</button>
                    </div>
                </form>"""
    html += """ <br/>
                <br/>
                <form method="post" enctype="text/plain" class="form-coordinates-input">
                    <label>Verify your coverage</label>
                    <br/>
                    <div>
                            <input
                            type="text"
                            id="lt"
                            name="lt"
                            placeholder="LT, ej:-33.0801393"
                            />
                            <br/>
                            <input
                            type="text"
                            id="lg"
                            name="lg"
                            placeholder="LG, ej:-68.97434"
                            />
                    </div>
                    <br/>
                    <div>
                        <button>Verify</button>
                        <br/>
                        <h5 class="error-type-file">Fields LT and LG required!</h5>
                    </div>
                </form></div>"""
    html += "</body>\n</html>"
    file = open(f"{abspath}/html/index.html", "w")
    file.write(html)
    file.close()

def generar_index_5(abspath, text, result):
    html = "<!DOCTYPE html>\n<html>\n<head><meta charset=\"UTF-8\">\n<link rel='stylesheet' type='text/css' href='../assets/css/index.css'>\n<title>Index</title>\n</head>\n<body>\n"
    html += "<div class='answer-container'>\n\t<h2>Geocoverage</h2>\n<div class='answer-coverage'>\n"
    html += '<h2>'+ text +'</h2>\n'
    html += '<h4>\n'
    if len(result) != 0:
        for i in result.keys():
            html += "<li>{}: {}</li>\n".format(i, result[i])
    html += "</h4></div>\n<br/>\n<a href='http://localhost:5000/'>\n<button class='go-back-button'> Go Back </button>\n</a>\n</div>\n</body>\n</html>"
    file = open(f"{abspath}/html/index.html", "w")
    file.write(html)
    file.close()

def generateHeader(path, abspath):
    print("Entro a buscar un archivo")
    dic = {"jpg": "image/jpeg", "pdf": "application/pdf", "html": "text/html", "ppm": "image/x-portable-pixmap"}
    if os.path.exists(path + "/files/"):
        try:
            extension = path.split(".")[1]
            extension = dic[extension]
            codeR = "HTTP/1.1 200 OK"
        except KeyError:
            codeR = "HTTP/1.1 500 Internal Server Error"
            path = f"{abspath}/html/500error.html"
    else:
        path = f"{abspath}/html/400error.html"
        codeR = "HTTP/1.1 404 Not Found"
    extension = path.split(".")[1]
    size = os.stat(path).st_size
    header = "{}\r\nContent-type: {}\r\nContent-lenght: {}\r\n\r\n".format(codeR, dic[extension], size)
    header = bytearray(header, "utf8")
    return path, header
