<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=34&pause=1000&width=435&lines=PROYECTO+COMPILADOR+" alt="Typing SVG" /></a>

# INSTRUCCIONES DE USO
**En el archivo input.txt se ingresa el nombre y la clase de tu personajes el programa solo admite 3 clases Guerrero,Mago y Arquero las cuales tienen cualidades unicas tales como el mago tiene mana, el Arquero tiene
velocidad y presicion, y el Guerrero tiene rabia.**
**En el output se te dara toda la informacion de tu personaje asiganada de manera aleatoria con la cual empezaras y tambien se te daran unos items en tu inventario**  
```mermaid
flowchart TD
    A[Input] --> B[Analisis Lexico]
    B --> C[Tokens]
    C --> D[Analisis Sintactico]
    D --> E{¿Cumple Con la sintaxis?}
    E --> Si --> F[Analisis Semantico]
    E --> No --> G[Error]
    F --> I{¿Los Tokens Tienen Sentido?}
    F --> Si --> I[Output]
    f --> No --> K[Error]

```
## HERRAMIENTAS
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white)
## EJEMPLO DE SINTAXIS
PERSONAJE  
NOMBRE: alberto  
CLASE: Guerrero  

## EJEMPLO DE OUTPUT
PERSONAJE  
NOMBRE= alberto  
CLASE=GUERRERO  
VIDA=100  
INTELIGENCIA=2  
RABIA=3  
VIDA=100  
INVENTARIO=Espada-Escudo-Pocion De Vida      
### CODIGO COMPLETO  
📄**CODIGO:**[Ver compilador.py](./compilador.py)


