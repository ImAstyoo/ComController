# Self-contained windows application
        - Create a venv with "python -m venv PATH_TO_VENV"
        - Activate venv with "PATH_TO_VENV/Scripts/activate"

        - Install necessary packages
            "pip install pygame"
            "pip install pyinstaller"

        - Move content of src/config into dist/
        - Change search path in main.py (line ~100, ~101)
            configuration = init_configuration(".\src\Config\Configuration.json") -> ".\dist\Configuration.json"
            window_configuration = init_configuration(".\src\Config\WindowConfiguration.json") -> "\dist\WindowConfiguration.json"

        - Run $pyinstaller main.py --noconsole