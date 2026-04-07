# Errores

Ejemplo erroneo: Intenta cerrar cosas cuando no debe, etc

``` C++
void process(){
  try {
  char *buf = (char*) malloc(sizeof(char)*100);

    FILE *f = fopen("file.txt", "r");
    if (f == nullptr){
        perror("Error al abrir el archivo");
        exit(EXIT_FAILURE);
    }

    int n = fread(buf, sizeof(char), 100, f);
    if (n < 0){
        perror("Error al leer el archivo");
        exit(EXIT_FAILURE);
    }
    int s = fclose(f);
    if (s != 0){
        perror("Error al cerrar el archivo");
        exit(EXIT_FAILURE);
    }
    } catch (...) {
        perror("Error desconocido");
        exit(EXIT_FAILURE);
    }
}
```

Ejemplo correcto: Siguiend RAII (Resource Acquisition Is Initialization) -> Adquiere recursos en el constructor y los libera en el destructor. De esta manera, se asegura que los recursos se liberen correctamente incluso si ocurre una excepcion.

``` C++
class Buffer{
    char *buf;
    size_t size;
public:
    Buffer(size_t size): size(size){
        buf = (char*) malloc(sizeof(char)*size);
        if (buf == nullptr){
            perror("Error al asignar memoria");
            exit(EXIT_FAILURE);
        }
    }
    ~Buffer(){
        free(buf);
    }
};

void process(){
    Buffer buf(100);
    File *f = fopen("file.txt", "r");

    f.read(buf->get(), sizeof(char), 100);
    //...//
    f.close();
}
```

Encapsulamiento de otra clase para seguir mas RAII

``` C++
class Double buffer{
    Buffer buf1;
    Buffer buf2;
public:
    DoubleBuffer(size_t size): buf1(size), buf2(size){

    }//constructor simple, no utiliza try catch porque el constructor de Buffer ya se encarga de manejar los errores
    ~DoubleBuffer() {

    }

}

class Lock{
    Mutex &mutex;
public:
    Lock(Mutex &mutex): mutex(mutex){
        mutex.lock();
    }
    ~Lock(){
        mutex.unlock();
    }
}
//incorrecto por Raii
void changesharedData(){
    this->mutex.lock();
    //...//
    this->mutex.unlock();
}
// Correcto por RAII
void changesharedData(){
    Lock lock(this->mutex);
    //...//
}
```

Mutex sirve para proteger recursos compartidos entre hilos. Es un mecanismo de sincronizacion que permite a los hilos acceder a un recurso compartido de manera exclusiva. Un mutex se bloquea cuando un hilo lo adquiere y se desbloquea cuando el hilo lo libera. Si otro hilo intenta adquirir el mutex mientras está bloqueado, se bloquea hasta que el mutex se desbloquee.(Aclaración de otra clase)

## Diseño de buenas excepciones

``` C++
    void parser(/*...*/){
        if (/*...*/){
            throw std::invalid_argument("Error: El argumento no es valido");
        }
        if (/*...*/){
            throw std::runtime_error("Error: Error de runtime");
        }
    }
```

El __FILE__ y __LINE__ son macros predefinidos en C++ que proporcionan información sobre el archivo y la línea de código donde se encuentran. Se pueden usar para mejorar la depuración y el manejo de errores al incluir esta información en los mensajes de error o excepciones.

``` C++
    void parser(/*...*/){
        if (/*...*/){
            throw std::invalid_argument("Error: El argumento no es valido en " + std::string(__FILE__) + ":" + std::to_string(__LINE__));
        }
        if (/*...*/){
            throw std::runtime_error("Error: Error de runtime en " + std::string(__FILE__) + ":" + std::to_string(__LINE__));
        }
    }
```

Los ... en una función indican que la función puede aceptar un número variable de argumentos. Esto se conoce como funciones variádicas. En C++, se pueden usar con la biblioteca #include "cstdarg" para manejar estos argumentos de manera segura.

``` C++
try {
    parser(/*...*/);
} catch (...) { // Captura cualquier excepción
    std::cerr << "Excepción capturada" << std::endl;
}
```

Hay que tener pocas clases de catch pero bien realizadas
En Multithreading es importante manejar las excepciones de manera adecuada para evitar que un hilo se bloquee o que el programa se termine inesperadamente. Se pueden usar try-catch dentro de los hilos para capturar y manejar las excepciones de manera segura.
Syslog es una función que se utiliza para registrar mensajes de error o información en el sistema. Es importante usar syslog para registrar errores en lugar de imprimirlos en la consola, ya que syslog permite una mejor gestión y análisis de los registros de errores.
