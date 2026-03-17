
# Cosas Básicas

```C
char c= 'a';
int i =1;
short int s=4;
char *p=0; puntero a caracter
int *g=0;
int b[2]={1,2};
char a[]= "AB"; El string ocupa un byte mas de su largo (3)
struct S{
    int a;
    char b;
    int c;
    char d;
}
struct S s={1,2,3,4};

Host to network
htons(short int)
htonl(int)

network to host
ntohs(short int)
ntohl(int)

```

**todos los punteros tienen el mismo tamaño**

## Constructores y destructores

```C++
class Buffer{
    private:
        char *data;
        size_t size;
    public:
        Buffer(size_t size){
            this->size=size;
            this->data= new char[size]();
        } #Constructor, se llama automaticamente cuando se crea un objeto de la clase
        ~Buffer(){
            delete[] this->data;
        } # Destructor, se llama automaticamente cuando el objeto sale del scope
}
```

```C++
Buffer b(10); # se llama al constructor
# se llama al destructor cuando b sale del scope
```

Hay que tener cuidado con los getters y setters, ya que pueden permitir modificar el estado interno del objeto de manera no controlada. Es importante asegurarse de que los getters y setters no permitan modificar el estado interno del objeto de manera no controlada.

```C++
public:
    char* getData(){
        return this->data;
    }
    void setData(char* data){
        this->data=data;
    }
    #No se recomienda usar getters y setters que permitan modificar el estado interno del objeto de manera no controlada
```

En este caso, el getter devuelve un puntero a la data, lo que permite modificar el estado interno del objeto de manera no controlada. Es importante asegurarse de que los getters y setters no permitan modificar el estado interno del objeto de manera no controlada. En este caso, se podría devolver una copia de la data en lugar de un puntero a la data, para evitar que se modifique el estado interno del objeto de manera no controlada.
Metodos constantes: Son metodos que no modifican el estado interno del objeto. Se declaran con la palabra clave const al final de la declaracion del metodo.

```C++
class Buffer{
    private:
        char *data;
        size_t size;
    public:
        Buffer(size_t size):
            this->size=size,
            this->data= new char[size]()
        {
            if (this->data==nullptr){
                throw std::bad_alloc();
            }
        }
        ~Buffer(){
            delete[] this->data;
        }
        char* getData() const{
            return this->data;
        }
        void setData(char* data){
            this->data=data;
        }
}
```

Tener en cuenta el ":" en el constructor, es una forma de inicializar los atributos de la clase. Es importante tener en cuenta que el orden de inicializacion de los atributos es el mismo que el orden en el que se declaran en la clase, no el orden en el que se escriben en el constructor.

```C++
struct TemperatureDTO{
    const double value;
    const TemperatureUnit unit;
    //Buena practica! colocarle const hace que no se puedan modificar los atributos de la clase, lo que garantiza que el estado interno del objeto no se modifique de manera no controlada
    TemperatureDTO(double value, TemperatureUnit unit):
        value(value),
        unit(unit)
    {}
};
//Cliente
protocol.sendTemperature(TemperatureDTO(30.5, TemperatureUnit::Celsius));
// Servidor(esta escuchando)
const TemperatureDTO temp=protocol.receiveTemperature();
//redundancia del const
```

referencias por sobre punteros: Las referencias son una forma de pasar un objeto por referencia sin tener que usar punteros. Las referencias se declaran con el operador & y no pueden ser nulas. Las referencias son más seguras que los punteros, ya que no pueden ser nulas y no requieren de una sintaxis especial para acceder a los miembros del objeto.

```C++
void processTemperature(const TemperatureDTO& temp){
    //procesar la temperatura
}
```

En este caso, se pasa la temperatura por referencia constante, lo que garantiza que el estado interno del objeto no se modifique de manera no controlada. Es importante tener en cuenta que las referencias no pueden ser nulas, por lo que no es necesario verificar si la referencia es nula antes de usarla. Además, al ser una referencia constante, no se pueden modificar los atributos del objeto, lo que garantiza que el estado interno del objeto no se modifique de manera no controlada.

```C++
int i=10;
int& ref=i; //ref es una referencia a i
ref=20; //modifica el valor de i a 20
```

Constructor por copia: Es un constructor que se llama cuando se crea un objeto a partir de otro objeto de la misma clase. El constructor por copia se declara con la palabra clave const y el operador &.
No hacer copias en Tps, ya que pueden ser costosas en términos de rendimiento. Es importante asegurarse de que el constructor por copia no realice copias innecesarias de los objetos, ya que esto puede afectar el rendimiento de la aplicación.
Hay que implementar el destructor de copias, ya que el constructor por copia realiza una copia superficial de los objetos, lo que puede causar problemas de memoria si los objetos contienen punteros. El destructor de copias se declara con la palabra clave const y el operador &.

```C++
//lineas del destructor de copias
Buffer(const Buffer& other):
    size(other.size),
    data(new char[other.size]())
{
    if (this->data==nullptr){
        throw std::bad_alloc();
    }
    std::copy(other.data, other.data+other.size, this->data);
}
~Buffer(){
    delete[] this->data;
}
```

Ownership: Que dos objetos no compartan recursos. Un objeto un recurso.

Constructor por movimiento: Es un constructor que se llama cuando se crea un objeto a partir de otro objeto de la misma clase, pero en lugar de realizar una copia del objeto, se mueve el recurso del objeto original al nuevo objeto. El constructor por movimiento se declara con la palabra clave &&.

Motivacion de move semantics: Aceptar una conexion de un cliente, pero no queremos copiar la conexion, sino moverla al nuevo objeto que se encarga de manejar la conexion. El constructor por movimiento permite mover el recurso del objeto original al nuevo objeto, lo que puede mejorar el rendimiento de la aplicación al evitar copias innecesarias de los objetos.

```C++
Socket s = acep.accept(); // se llama al constructor por movimiento, ya que acep.accept() devuelve un objeto temporal que se mueve al nuevo objeto s
Socket accept(){
    int fd = ::accept(this->fd, nullptr, nullptr);
    return std::move(Socket(fd)); // se mueve el recurso del objeto temporal al nuevo objeto Socket que se devuelve
}

```

Swap de objetos: Es una técnica que se utiliza para intercambiar los recursos de dos objetos de la misma clase. El swap de objetos se declara con la palabra clave void y el operador &.

```C++
void swap(Buffer& a, Buffer& b){
    Buffer t = std::move(a); // se mueve el recurso de a al nuevo objeto temporal t
    a = std::move(b); // se mueve el recurso de b al nuevo objeto a
    b = std::move(t); // se mueve el recurso de t al nuevo objeto b
}

```

