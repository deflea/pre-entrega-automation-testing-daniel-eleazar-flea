## Descripción del proyecto

Proyecto realizado en el marco del curso "Automatización QA" del programa **Talento Tech** con el propósito de poner en práctica el contenido aprendido mediante la automatización del sitio web [saucedemo](https://www.saucedemo.com/).
En esta entrega además se utiliza [jsonplaceholder](https://jsonplaceholder.typicode.com/) para realizar pruebas de API.
Se agregó un registro de logs.
Se creo una nueva estructura de carpetas para separar los test de api y los de ui.

Tecnologías utilizadas:
1. Python
2. Pytest
3. Selenium
4. uv

Instructor: Brayann Farfan  
Tutor: Amancay Arribillaga

### Requerimientos

Por defecto el navegador utilizado es **Firefox**, se utiliza webdriver-manager para instalar la última versión.  
Se utiliza uv como gestor de paquetes de python, instalarlo utilizando `pip install uv`

### Instrucciones
1. Clonar el repositorio:   
`git clone git@github.com:deflea/pre-entrega-automation-testing-daniel-eleazar-flea.git`
2. Sincronizar el entorno e instalar dependencias:  
`uv sync`
3. Ejecutar todos los tests:  
`uv run pytest`
4. Ejecutar un archivo especifico:
`uv run pytest tests/test_saucedemo_base.py`
5. Ejecutar y generar reporte:
`uv run pytest -v --html=reports/report.html`


### Estructura del proyecto  
```
	pre-entrega-automation-testing-daniel-eleazar-flea/
	├── api/
	│   └── api_functions.py
	├── logs/
	│	└── test_log.log
	├── reports/
	│	├── screenshots/
	│	└── report.html
	├── tests/
	│   ├── api/
	│	│	└── test_api_methods.py
    │	└── ui/
	│		├── test_complete_checkout_flow.py
	│		└── test_saucedemo_base.py
	├── utils/
	│		└── helpers.py
	├── .gitignore
	├── .python-version
	├── README.md
	├── pytest.ini
	├── conftest.py
	├── pyproject.toml
	└── uv.lock
```

