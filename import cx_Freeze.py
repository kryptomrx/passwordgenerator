import cx_Freeze

executables = [cx_Freeze.Executable("my_script.py")]

cx_Freeze.setup(
    name="PasswortManager.py",
    options={"build_exe": {"packages":["numpy"], "include_files":["my_data.dat"]}},
    executables=executables
)
