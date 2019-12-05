from pyzt import inputi,inputs,inputf
import platform
import settings

if _name_ == '_main_':
    if platform.python_version()[0] == '3':
        import control
        control=control.Control()
        if settings.DEBUG:
            print("DEBUG MODE")
        else:
            control.run()
    else:
        exit("SHOP: Unsupported Python Version!")

