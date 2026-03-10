
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
