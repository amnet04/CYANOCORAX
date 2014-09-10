from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('GUI_MMAW/Ui_Hemadaw.py', base=base, targetName = 'WavData2CSV')
]

setup(name='Cyanocorax',
      version = '0.1',
      description = 'Primera entrega de las herramientas de manipulación de archivos para corpus lingüísticos multimodales (extracción masiva de parametros de los archivos wav)',
      options = dict(build_exe = buildOptions),
      executables = executables)
