# Fast-Api-1

Este es un proyecto de ejemplo utilizando FastAPI.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/Fast-Api-1.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd Fast-Api-1
    ```

3. Crea un entorno virtual:

    ```bash
    python -m venv env
    ```

4. Activa el entorno virtual:
    - En Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - En Unix o MacOS:

        ```bash
        source env/bin/activate
        ```

5. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
uvicorn main:app --reload
```

## Estructura del Proyecto

```txt
Fast-Api-1/
├── main.py
├── requirements.txt
├── README.md
└── ...
```

## Endpoints

- `GET /`: Retorna un mensaje de bienvenida.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia MIT.
