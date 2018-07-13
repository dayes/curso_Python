from cx_Freeze import setup, Executable

setup(name="consola",
	  version="1.0.0",
	  description="prueba de ejecutable",
	  executables=[Executable("telefonia.py")],)


