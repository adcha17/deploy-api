# Deploy Api VMC

API REST construida con <a href="https://fastapi.tiangolo.com/">FastAPI</a> y el paquete <a href="https://ansible-runner.readthedocs.io/en/stable/Ansible-Runner">Ansible-Runner</a> para poder invocar Ansible desde Python!

Las tareas automatizadas con Ansible se encuentran en el repositorio <a href="https://github.com/subascorp/ansible_runner">Subascorp/Ansible-Runner</a>.

## Tecnologías
- Python3.10
- Virtualenv
- Fastapi
- Typer(cli)
- Ansible
- Ansible-Runner

## Prerequisitos
* Python
  ```sh
  sudo apt install -y python3
  ```
* Virtualenv
  ```sh
  sudo pip3 install virtualenv
  ```

## Instalación
- Clonar el repositorio.
```sh
git clone git@github.com:subascorp/deploy_api_vmc.git
```
- Crear entorno virtual.
```sh
virtualenv venv
```
- Activar entorno virtual
```sh
source venv/bin/activate
```
- Instalar las dependencias dentro del entorno virtual. (Fastapi, Typer, Ansible, Ansible-Runner)
```sh
pip install -r requirements.txt
```

## CLI
- Setear las variables de entorno, configurar el .env file
```sh
cp env_example .env
```
- Obtener info de la cli.
```sh
python cli.py --help
```
- Hacer checkout a un proyecto.
```sh
python cli.py checkout *project* *repo_branch*
```

- Hacer pull a un proyecto.
```sh
python cli.py pull *project* *repo_branch*
```

- Hacer status a un proyecto.
```sh
python cli.py status *project*
```
- Crear alias(opcional)
```sh
nano ~/.zshrc
alias vmcdev="python ~/Projects/deploy_api_vmc/cli.py"
source ~/.zshrc
```
