from Program.Config.Config import *
from Program.Config.Util import *

try:
    import webbrowser
    import re
    from tkinter import messagebox
except Exception as e:
    ErrorModule(e)

# OSINT OPTIONS
option_10 = "D0x-Create"
option_11 = "D0x-Tracker"
option_12 = "Get-Image-Exif"
option_13 = "Google-Dorking"
option_14 = "Username-Tracker"
option_15 = "Email-Tracker"
option_16 = "Email-Lookup"
option_17 = "Phone-Number-Lookup"
option_18 = "Ip-Lookup"
option_19 = "Instagram-Account"

# Display text for each option
option_10_txt = f"{purple}[{white}10{purple}]{white} " + option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = f"{purple}[{white}11{purple}]{white} " + option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = f"{purple}[{white}12{purple}]{white} " + option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = f"{purple}[{white}13{purple}]{white} " + option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = f"{purple}[{white}14{purple}]{white} " + option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = f"{purple}[{white}15{purple}]{white} " + option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = f"{purple}[{white}16{purple}]{white} " + option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = f"{purple}[{white}17{purple}]{white} " + option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = f"{purple}[{white}18{purple}]{white} " + option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = f"{purple}[{white}19{purple}]{white} " + option_19.ljust(30)[:30].replace("-", " ")

# Menu only for OSINT tools
menu_osint = f""" 
 ┌─── OSINT TOOLS ─────────────────────────────────────────────────────────────┐
 │                                                                            │
 ├─ {option_10_txt} ─ D0x Create
 ├─ {option_11_txt} ─ D0x Tracker
 ├─ {option_12_txt} ─ Get Image Exif
 ├─ {option_13_txt} ─ Google Dorking
 ├─ {option_14_txt} ─ Username Tracker
 ├─ {option_15_txt} ─ Email Tracker
 ├─ {option_16_txt} ─ Email Lookup
 ├─ {option_17_txt} ─ Phone Number Lookup
 ├─ {option_18_txt} ─ IP Lookup
 └─ {option_19_txt} ─ Instagram Account
"""

def Menu():
    banner = f"""
 ██████╗ ██╗  ██╗███████╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔═████╗╚██╗██╔╝╚════██║    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║██╔██║ ╚███╔╝     ██╔╝    ██║   ██║███████╗██║██╔██╗ ██║   ██║   
████╔╝██║ ██╔██╗    ██╔╝     ██║   ██║╚════██║██║██║╚██╗██║   ██║   
╚██████╔╝██╔╝ ██╗   ██║      ╚██████╔╝███████║██║██║ ╚████║   ██║   
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
 
                      {white}{github_tool}
                         {menu_osint}
"""
    return banner

options = {
    '10': option_10, '11': option_11, '12': option_12,
    '13': option_13, '14': option_14, '15': option_15,
    '16': option_16, '17': option_17, '18': option_18, '19': option_19
}

while True:
    try:
        Clear()
        Title("OSINT Menu")
        Slow(MainColor(Menu()))

        choice = input(MainColor(f""" ┌──({white}{username_pc}@0x7EF4)─{purple}[~/{os_name}/OSINT]
 └─{white}$ {reset}"""))

        if choice in options:
            StartProgram(f"{options[choice]}.py")
        else:
            ErrorChoiceStart()

    except Exception as e:
        Error(e)
