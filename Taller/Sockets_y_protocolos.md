# Clase número 2: Sockets y protocolos

Protocolos: Definen los mensajes intercambiados entre dos o mas participantes u ñas acciones definidas ante la transmision/recepcion de los mismos (Manda y devuelve mensajes)
Existen distintas capas de protocolos. Tcp/ip divide en capas los protocolos.
Ejemplos de protocolos:

- Http
- FTP
- Telmet
- SMTP
- DNS

Telmet, SMTP y DNS son metodos UDP y HTTP, FTP son de TCP
*IP(internet protocol)*: Routeo de paquetes en una red de computadoras(intenta mandar paquetes, pueden llegar o no)

- Ipv4: direcciones de red de 4 bytes(direcciones de computadoras que se quedaron cortos e implementaron Ipv6)
- Ipv6: direcciones de red de 16 bytes

```C++
getaddrinfo('fi.uba.ar',...)-> 186.33.219.219
#forma de obtener la informacion-> tranforma un dominio en una lista enlazada de direcciones ip
dig google.com -> forma de mappear 
```

**TCP**: Protocolo de transmision confiable, orientado a conexion. Se asegura que los mensajes lleguen a destino y en orden. Es un protocolo de transmision de bytes, no de mensajes(Streams). El receptor recibe un flujo de bytes y no sabe como se fragmentan los mensajes. TCP se encarga de fragmentar los mensajes en paquetes y rearmarlos en el destino.

**Three Way Handshake**: Protocolo de conexion de TCP. El cliente manda un mensaje SYN al servidor, el servidor responde con un mensaje SYN-ACK y el cliente responde con un mensaje ACK. Una vez que se completa el Three Way Handshake, se establece la conexion entre el cliente y el servidor.

**Sockets**: Son una abstraccion de la conexion entre dos computadoras. Permiten a las aplicaciones enviar y recibir datos a traves de la red. Un socket es un punto final de una conexion de red. Un socket se identifica por una direccion IP y un numero de puerto. Para comunicar dos computadoras es necesario un solo socket en cada una de ellas, ya que realiza operaciones de lectura y escritura. Un socket se puede usar para enviar y recibir datos a traves de la red.
