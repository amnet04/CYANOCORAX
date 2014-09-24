from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
incluirDLL="C:\Python34\Lib\site-packages\PyQt5\libEGL.dll" #esto corrige el problema de carga por fallo en plugin windows... minimal
buildOptions = dict(packages = [], excludes = [], include_files=[incluirDLL])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None


executables = [
    Executable('GUI_MMAW/Ui_Hemadaw.py', base=base, targetName = 'WavData2CSV.exe')
]

setup(name='Cyanocorax',
      version = '0.1',
      description = 'Primera entrega de las herramientas de manipulación de archivos para corpus lingüísticos multimodales (extracción masiva de parametros de los archivos wav)',
      options = dict(build_exe = buildOptions),
      executables = executables)
