# aws-python-boto3

Este repositorio ha sido creado como un recurso complementario para las prácticas de **Infraestructura como Código** del módulo de [Implantación de Aplicaciones Web][4] del **Ciclo Formativo de Grado Superior ASIR**.

## ¿Qué es Boto3?

[Boto3][1] es un SDK (_Software Development Kit_) de [Python][3] desarrollado por y para **Amazon Web Services (AWS)**. Este SDK permite a los desarrolladores interactuar con los servicios de AWS para crear y gestionar recursos como grupos de seguridad o instancias EC2, a través de aplicaciones escritas en [Python][3]. 

## Boto3 `resource` y `client`

[Boto3][1] permite interactura con los servicios de AWS de dos formas diferentes:

- `resource`: Devuelve una estructura de datos. Se puede considerar como una interfaz de alto nivel.

```python
client = boto3.resource('ec2')
```

- `client`: Devuelve un JSON. Se puede considerar como una interfaz de bajo nivel.

```python
client = boto3.client('ec2')
```

## Creación de un entorno virtual para instalar Boto3

1. Creamos un entorno virtual.

```
python3 -m venv .venv
```

2. Activamos el entorno virtual.

```
. .venv/bin/activate
```

3. Instalamos el paquete [`boto3`][1].

```
python3 -m pip install boto3
```

## Configuramos las credenciales de AWS


Editamos el archivo de credenciales de AWS que está en la ruta:

```
~/.aws/credentials
```

Copiamos nuestras credenciales, sustituyendo los valores de `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` y `AWS_SESSION_TOKEN`, por nuestros valores de [AWS Academy][2].

```
[default]
aws_access_key_id=AWS_ACCESS_KEY_ID
aws_secret_access_key=AWS_SECRET_ACCESS_KEY
aws_session_token=AWS_SESSION_TOKEN
```

Editamos el archivo de configuración de AWS, para indicar la región y el formato de salida de los comandos de AWS CLI.

El archivo de configuración de AWS está en la ruta:

```
~/.aws/config
```

En nuestro caso, la región de [AWS Academy][2] es `us-east-1` y en el formato de salida utilizaremos `json`.

```
[default]
region = us-east-1
output = json
```

## Referencias

- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#securitygroup
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance
- https://www.learnaws.org/2021/02/24/boto3-resource-client/

[1]: https://aws.amazon.com/es/sdk-for-python/
[2]: https://aws.amazon.com/es/training/awsacademy/
[3]: https://www.python.org/
[4]: https://josejuansanchez.org/iaw/