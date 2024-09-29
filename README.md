# PyConEs2024-PatternBusters


Bienvenidos al taller de Pattern Busters. Este documento contiene los pasos necesarios para configurar tu entorno de desarrollo y comenzar a trabajar en el taller.

## Requisitos Previos

Asegúrate de tener instalado `pyenv` y `virtualenv`. Si no los tienes, puedes seguir las instrucciones de instalación en sus respectivas páginas de documentación.

## Pasos para Configurar el Entorno

1. **Instalar `pyenv` y `virtualenv`:**

   Si no tienes `pyenv` y `virtualenv` instalados, ejecuta los siguientes comandos:

   ```bash
   # Instalar pyenv
   curl https://pyenv.run | bash

   # Agregar pyenv al PATH
   echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   source ~/.bashrc

   # Instalar virtualenv
   pip install virtualenv
   ```

2. **Instalar Python 3.9.19 con `pyenv`:**

   Ejecuta el siguiente comando para instalar Python 3.9.19:

   ```bash
   pyenv install 3.9.19
   ```

   Después de la instalación, fija esta versión de Python como local en el directorio del proyecto:

   ```bash
   pyenv local 3.9.19
   ```

3. **Crear un entorno virtual y activarlo:**

   Crea un entorno virtual utilizando `virtualenv`:

   ```bash
   virtualenv venv
   ```

   Activa el entorno virtual:

   ```bash
   # En Linux o macOS
   source venv/bin/activate

   # En Windows
   .\venv\Scripts\activate
   ```

4. **Instalar las dependencias del proyecto:**

   Asegúrate de tener un archivo `requirements.txt` en tu directorio del proyecto y ejecuta el siguiente comando para instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. **Abrir Jupyter Lab:**

   Una vez que las dependencias estén instaladas, puedes abrir Jupyter Lab ejecutando:

   ```bash
   jupyter lab
   ```

Ahora estás listo para comenzar el taller de Pattern Busters. ¡Esperamos que disfrutes el taller!
```
