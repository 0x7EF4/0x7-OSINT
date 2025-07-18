try:
    import sys
    import os

    def OpenSites():
        try:
            # Suppression de l'ouverture des sites
            # import webbrowser
            # from Program.Config.Config import telegram, gunslol
            # webbrowser.open(f'https://{telegram}')
            # webbrowser.open(f'https://{gunslol}')
            pass
        except:
            pass

    def install_and_run():
        if sys.platform.startswith("win"):
            os.system("cls")
            python_cmd = "python"
        elif sys.platform.startswith("linux"):
            os.system("clear")
            python_cmd = "python3"
        else:
            raise Exception("Unsupported platform")

        print("Installing the python modules required for the OSINT tools:\n")
        os.system(f"{python_cmd} -m pip install --upgrade pip")
        os.system(f"{python_cmd} -m pip install -r requirements.txt")
        OpenSites()
        os.system(f"{python_cmd} 0x7EF4.py")

    install_and_run()

except Exception as e:
    input(f"An error occurred: {e}")
