import PyInstaller.__main__

# Reference:
# https://pyinstaller.readthedocs.io/en/stable/usage.html

target_file = 'hardware_logger.py'

PyInstaller.__main__.run(
    [
        '--distpath', './build/console/dist',
        '--workpath', './build/console/build',
        '--specpath', './build/console',
        # '--windowed',  # not working...?
        '--onefile',  # make build file as one file
        target_file
    ]
)
