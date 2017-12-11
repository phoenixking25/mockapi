import click
from api import runapi
endpoint = ''

req_options = {1: 'GET', 2: 'POST', 3: 'DELETE', 4: 'PATCH'}

@click.command(help = "Mock-Api is a offline tool that is used to create dummy api to build frontend that will make request on the api running on the localhost")
@click.option('--port', default = 8080, help = "Specipfy port for running api on localhost")
@click.option('--name', prompt = "Name for the Api", help = "Name of the api")

def getinfo(port, name):
    endpoint = name
    field_names = []
    field_count = int(raw_input('Enter the number of fields: '))
    for i in range(1, field_count + 1):
        field_names.append(raw_input("Enter the name of Field No %r[Field %r]: " % (i, i)).strip() or "Field %r" % i)
    datasets = makedata(field_names)
    print "List of request methods"
    for i in req_options:
        print "%r: %r" % (i, req_options[i])
    get_methods = map(int, raw_input("Which request methods you want in your Api? ").strip().split(' '))
    methods = []
    for i in get_methods:
        methods.append(req_options[i])
    runapi(port)

def makedata(fields):
    data = []
    for i in xrange(10):
        for j in fields:
            objdata = {"%r" % (j):j + " " + str(i)}
            data.append(objdata)
    return data


if __name__ == '__main__':
    getinfo()
