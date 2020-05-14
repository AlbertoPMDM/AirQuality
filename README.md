# Actividad Eje

## La calidad de aire y el COVID-19

[![Coronavirus](https://imgur.com/xdJxEDR)](https://www.youtube.com/watch?v=E9sUpVQ4izY "Coronavirus")

- Alberto Méndez
- Aldo Hernández
- Benjamín Barraza
- Jorge Márquez

Para encontrar nuestra idea, comenzamos tomando en cuenta la problemática más notable actual, el coronavirus, y tratamos de pensar en un aspecto que no fuera tan notable, pero aún así influyera en el problema, como es la calidad del aire que respira un enfermo. (BBC, 2020.). En facilidades médicas, quizá si se pueda tener un control estricto sobre la cantidad de partículas de aire y la composición, pero es muy costoso el equipo, por lo tanto, decidimos tratar de resolver el problema de una manera un poco más simple.

Dé esta manera tuvimos la idea de utilizar una placa Arduino, un sensor ultrasónico y estadísticas de diversos datos, para hacer un contador de personas, que mediante datos proporcionados , la mayoría basados en estadísticas, podrá predecir el nivel de partículas que se encontrarán en un cuarto, y por lo tanto avisar a las personas cuando se esté llegando a un nivel crítico, y se requiera de ventilación o de que algunos salgan, con el fin de poder mantener una calidad de aire decente en el cuarto, apta para el bienestar de algún enfermo.

Para empezar, ocupamos saber cuales son los riesgos que puede presentar la presencia de una persona. Para empezar, según el mismo artículo (BBC, 2020.), la presencia de partículas pequeñas (<2.5 μm.) puede causar daños considerables al corazón, pulmones y cerebro, y las personas pueden aumentar notablemente, ya que una persona sana puede llegar a exhalar aproximadamente 70 partículas/litro, de igual manera, si hay alguna bacteria o virus que se aloje en la garganta superior, es muy probable que ésta también se difunda en el ambiente, y en igual proporción, la presencia de partículas grandes (>10 μm.), las cuales también están presentes en el contenido exhalado de una persona, pueden servir de transporte para el COVID-19 (Fabian, Brain, Houseman, Gern, & Milton, 2011). De igual manera, el aumento de concentraciones de NO2 y CO2 en el aire pueden tener un gran impacto en el sistema inmune de una persona, lo cual se debe evitar, porque para alguien sano aumenta la vulnerabilidad de volverse transmisor o de adquirir alguna condición, y para alguien enfermo, reduce su capacidad de recuperarse, y como se demuestra, la presencia de estos gases en alta concentración se puede vinculara a una mayor infectividad y mortalidad (EPA, 2020).

Y si, los mayores contribuidores a una mala calidad de aire son las empresas que llevan a cabo procesos de manufactura, y son cosas que no podemos controlar, aunque debido a la cuarentena se ha visto disminuido. De todas maneras, al estar encerrados, debemos buscar hacia tratar de preservar la calidad del aire de nuestras casas, y otros espacios cerrados en los que nos encontremos o se tenga gente en un estado de salud poco óptimo, para reducir contagios y muertes, y la manera más fácil y menos costosa de llevar esto a cabo es controlando la cantidad de personas y ventilación de los espacios.

El sistema funcionará, como se mencionó anteriormente, a partir de datos como el volumen de la habitación, la calidad del aire de la zona de residencia, y los datos de lo que cada persona puede aportar al área, contando con un sensor ultrasónico la cantidad de personas que entran, de manera que mediante un buzzer y leds pueda avisar cuando se sobrepasen niveles no seguros.

Y aunque es cierto que hay limitaciones para el modelo de funcionamiento, es como mínimo, una manera muy costeable de estar informado de la calidad del aire, ya que el costo de un sensor de gases y partículas propio comienza en más de 100 dólares, mientras que el nuestro costaría aproximadamente 10 dólares.

Referencias:
European Public Health Alliance. (2020). Coronavirus threat greater for polluted cities. Retrieved from <https://epha.org/coronavirus-threat-greater-for-polluted-cities/>
BBC (2020, April 28). How air pollution exacerbates Covid-19.Retrieved from <https://www.bbc.com/future/article/20200427-how-air-pollution-exacerbates-covid-19>
Fabian, P., Brain, J., Houseman, E. A., Gern, J., & Milton, D. K. (2011, June). Origin of exhaled breath particles from healthy and human rhinovirus-infected subjects. Retrieved from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3123971/>

## Guía

![Guía](https://imgur.com/WiEi9aE)(https://www.youtube.com/watch?v=E9sUpVQ4izY "Guía")

## Instalación

Solo se requiere que se descargue o clone el proyecto a algún directorio del ordenador

## Uso

### Primeros pasos

Como primer paso se debe de ejecutar **start.bat**, el cual creará un archivo de configuración **config.ini**, en ésta se encuentra un espacio llamado *Room Size*, en el cual se especifica que campos se tienen que editar, para que el programa conozca las características del cuarto en el que se encuentra.

De igual manera se exponen otros datos, como los límites de exposición, la calidad del aire actual, y la localización actual, todos basados en datos de [ésta página](https://waqi.info/).

### Mantenimiento

Seguido de ésto se ejecuta **update.bat**, éste generará un directorio llamado **tally** en donde se encontrará **tally.ino**. Se abre el programa y se carga a la placa.

>Se recomienda ejecutar el proceso de mantenimiento cada hora como mínimo, para asegurarse de tener los datos más recientes.

### Recomendaciones y limitaciones

- El programa utiliza datos de localización proveídos por el ip, por lo tanto no siempre tiene la localización correcta; si en **config.ini** no aparece tu ciudad, se recomienda que entres a [ésta página](https://waqi.info/) y actualices los datos bajo el campo de *Air Quality* por tu cuenta, y luego ejecutes **ManualUpdate.bat**.

- De igual manera, se recomienda no utilizar la puerta con el sensor, ya que éste se podría confundir.

- A veces , en algunas zonas, la calidad del aire inicial ya es riesgosa, en éstos casos se recomienda solamente tener una buena ventilación.

- *Aunque no es recomendable* se puede editar el límite de personas que maneja el sensor en el campo *limit* del código de arduino:

>```arduino
>int grn = 11;
>int red = 8;
>int us1[] = {6,5};//[trig, echo]1
>int us2[] = {3,2};
>int trig = 6;
>int echo = 5;
>int limit = 0;
>int button = 13;
>int calibration1;
>int calibration2;
>int counter;
>double soundSpeed = 0.0343;
>long dist;
>long pulse;
>```

- Si conoces el código de arduino, entonces quizá sepas conectarlo, de otra manera refiere a [ésta página de Tinkercad](https://www.tinkercad.com/things/g2BWiqrGhbB ) para averiguar las conexiones y probar el código.

## Implementaciones futuras

- Uso de la localización gps para poder proveer datos más precisos.
- Un contador más confiable

## Impacto Personal