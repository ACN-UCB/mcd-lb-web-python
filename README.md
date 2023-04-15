# Ejemplo de Balanceo de Carga con Docker, NGINX y Python

## Construir la imagen de la App Web en Python

Para construir la imagen siga los siguientes pasos:

```bash
cd docker-image
docker build -t my_web_app:1.0.0 .
```

## Configuramos el balanceador.

- Creamos una red de docker:

```bash
docker network create --driver=bridge --subnet=192.168.100.0/16 my-net
```

- Para probar

```bash
# Ver como la red esta en la maquina
ip a
# Ver la red en docker 
docker network ls
```

# Configuramos el balanceo de carga:

- Levantmos tres nodos de la aplicación Web

```bash
docker run --name node1 --network="my-net" -d my_web_app:1.0.0
docker run --name node2 --network="my-net" -d my_web_app:1.0.0
docker run --name node3 --network="my-net" -d my_web_app:1.0.0
```

- Verificamos que la configuración del NGINX tome en cuenta los tres nodos, para esto revisar el archivo `nginx_conf_d/load_balancer_nginx.conf`, el upstream debería tener los tres nodos:

```
upstream myapp {
    server node1:5000;
    server node2:5000;
    server node3:5000;
}
```

- Levantamos el nginx. Debe ejecutarlo en la carpeta raiz del proyecto que es la que contiene a la carpeta ngix_conf_d

```
cd /workspaces/mcd-lb-web-python
docker run --name lb-nginx -p 7777:80 -d --network="my-net" -v $(pwd)/nginx_conf_d:/etc/nginx/conf.d nginx
```

- Probamos, ejecutar varias veces lo siguiente, parar los nodos 1 y 2 para ver que noda errores.
```
curl http://localhost:7777/api/hello/Luis
```


