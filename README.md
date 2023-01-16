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

## Ejemplos

- Ejemplos utilizando `boto3.resource`.
  - [Ejemplo 01](resource/ejemplo-01/). Utilizando programación estructurada.
  - [Ejemplo 02](resource/ejemplo-02/). Utilizando programación orientada a objetos.
- Ejemplos utilizando `boto3.client`.
  - [Ejemplo 01](client)

## Ejercicios

### Ejercicio 1

Escriba un script de Python para crear un grupo de seguridad con el nombre `backend-sg`.
Añada las siguientes reglas al grupo de seguridad:
- Acceso SSH (puerto 22/TCP) desde cualquier dirección IP.
- Acceso al puerto 3306/TCP desde cualquier dirección IP.

### Ejercicio 2

Escriba un script de Python para crear una instancia EC2 que tengas las siguientes características.
- Identificador de la AMI: ami-08e637cea2f053dfa. Esta AMI se corresponde con la imagen Red Hat Enterprise Linux 9 (HVM).
- Número de instancias: 1
- Tipo de instancia: t2.micro
- Clave privada: vockey
- Grupo de seguridad: backend-sg
- Nombre de la instancia: backend

### Ejercicio 3

- Crea un script para crear la infraestructura de la práctica 9.
- Crea un script para eliminar la infraestructura de la práctica 9.

### Ejercicio 4

Modifique los ejemplos 01 y 02 de este repositorio que utilizan `boto3.resource`, para añadir una nueva opción al menu del archivo `main.py` que permita crear una dirección IP elástica y asociarla a una instancia EC2. El usuario tendrá que introducir el nombre de la instancia por teclado.

## Referencias

- [Documentación oficial de Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).
- [Documentación de `SecurityGroup` en Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#securitygroup).
- [Documentación de `Instance` en Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance).
- [Boto 3: Resource vs Client](https://www.learnaws.org/2021/02/24/boto3-resource-client/). Learn AWS.
- [Python examples on AWS (Amazon Web Services) using AWS SDK for Python (Boto3)](https://github.com/alfonsof/aws-python-examples). Alfonso Fernandez-Barandiaran.

[1]: https://aws.amazon.com/es/sdk-for-python/
[2]: https://aws.amazon.com/es/training/awsacademy/
[3]: https://www.python.org/
[4]: https://josejuansanchez.org/iaw/