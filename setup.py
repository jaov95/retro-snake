import cx_Freeze

executables = [cx_Freeze.Executable("snake.py",
                                    base = "Win32GUI")]
build_exe_options = {"packages":["pygame"],
                     "include_files":["arcadeclassic.ttf",
                                     "iconRetroSnakeG64.png",
                                     "logoIconRetroSnake100x100.png",
                                     "BeepSnake.ogg",
                                     "GameOverSnake.ogg",
                                     "PauseOffSnake.ogg",
                                     "PauseOnSnake.ogg",
                                     "SongOfSnake.ogg"]}
cx_Freeze.setup(
    name = "RetroSnake",
    version = "1.0.0",
    description="Recreacion Retro del popular Snake",
    options={"build_exe":build_exe_options},
    executables = executables
    )
#Comando a ejecutar en cmd dentro de la carpeta
#>>> python setup.py build
