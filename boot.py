def boot():

    import os

    print("AP loading...") #Start Loadina

    try: #Load core
        print("Core loading...")
        from core import coreinfo
    except Exception:
        print(Exception)
        print("Core crashed!")
    else:
        print(coreinfo['corename'] + coreinfo['corever'] + coreinfo['corearm'] +" loading is successful!")

    try: #Load ram
        print("RAM loading...")
        from ram import raminfo
    except Exception:
        print(Exception)
        print("RAM crashed!")
    else:
        print(raminfo['ramname'] + raminfo['ramver'] + raminfo['ramarm'] +" loading is successful!")

    try: #Load bootsys
        print("BootSys loading...")
        from bootsys import bootsystem
    except Exception:
        print(Exception)
        print("BootSys crashed!")
    else:
        print("BootSys loading is successful!")
        print("System loading...")
        bootsystem()


if __name__ == "__main__":
    boot()