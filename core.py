from ram import _read
from ram import _mov
from ram import _read_metadata
from ram import _mov_metadata

coreinfo = {
    'corearm': '1089',
    'corever': 'A1_',
    'corename': 'Core_AlphaPy '
    }

def _app(app):

    applist = _read(app)
    appcommands = applist.split(";\n")
    metadata = appcommands[0]

    for appinit in appcommands:

        appcom = appinit.split("=")

        if(appcom[0] == "print"):

            if(appcom[1] == "_md"):

                print(_read_metadata(metadata, appcom[2]))

            else:

                print(appcom[1])

        elif(appcom[0] == "input"):

            _mov_metadata(metadata, input(appcom[1]), appcom[2])

        elif(appcom[0] == "metadata"):

            if(appcom[1] == "_file"):

                _mov_metadata(metadata, _read(appcom[2]), appcom[3])

            elif(appcom[1] == "_md"):

                _mov(appcom[2], _read_metadata(metadata, appcom[3]))

            else:

                _mov_metadata(metadata, appcom[1], appcom[2])

        elif(appcom[0] == "run"):

            if(appcom[1] == "_file"):

                ___app(_read(appcom[2]))

            elif(appcom[1] == "_md"):

                ___app(_read_metadata(metadata, appcom[2]))

            else:

                ___app(appcom[1])

        elif(appcom[0] == "intopr"):

            if(appcom[1] == "+"):

                _mov_metadata(metadata, str(int(_read_metadata(metadata, appcom[2])) + int(_read_metadata(metadata, appcom[3]))), appcom[4])

            elif(appcom[1] == "-"):

                _mov_metadata(metadata, str(int(_read_metadata(metadata, appcom[2])) - int(_read_metadata(metadata, appcom[3]))), appcom[4])

            elif(appcom[1] == "*"):

                _mov_metadata(metadata, str(int(_read_metadata(metadata, appcom[2])) * int(_read_metadata(metadata, appcom[3]))), appcom[4])

            elif(appcom[1] == "//"):

                _mov_metadata(metadata, str(int(_read_metadata(metadata, appcom[2])) // int(_read_metadata(metadata, appcom[3]))), appcom[4])

        elif(appcom[0] == "true_false"):

            if(appcom[1] == "md_md"):

                if(_read_metadata(metadata, appcom[2]) == _read_metadata(metadata, appcom[3])):

                    ___app(appcom[4])

                else:
                    
                    ___app(appcom[5])

            if(appcom[1] == "_md"):

                if(_read_metadata(metadata, appcom[2]) == appcom[3]):

                    ___app(appcom[4])

                else:
                    
                    ___app(appcom[5])

        else:

            from bootsys import oprinit

            oprinit(metadata, appcom)

def ___app(_app_):
    _app(_app_)