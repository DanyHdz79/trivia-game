#PROYECTO FINAL
#Pensamiento Computacional para Ingeniería y Ciencias
#TC1028.2
#Prof. Hugo Méndez
#Daniela Hernández y Hérnández   A01730397
#Axel Vicenté Rodríguez          A01732927

import random

#El código inicia explicando las instrucciones del juego al usuario
print('¡Bienvenido a PISA TRAINING!.')
print('Este juego te ayudará a practicar problemas de la prueba PISA y mejorar tus resultados.')
print()
print('Para jugar debes oprimir la tecla "x", lo que hará girar la ruleta y elegirá un tema.')
print('Una vez elegido el tema, se te hará una pregunta.')
print('Si la contestas correctamente avanzarás un espacio, de lo contrario retrocederás uno.')
print('A lo largo de tu camino podrás resporder preguntas divertidas para obtener un bonus de 2 puntos.')
print('Para cada pregunta tendrás dos intentos.')
print('Recuerda escribir todas tus respuestas en minúsculas, sin acentos y sin unidades.')
print()
print('Necesitas obtener 20 preguntas correctas para llegar a la meta y ganar. ¡Tu puedes!')
print()

#A lo largo del programa se encontrarán dibujos de caracteres como el siguiente
#El objetivo de esto es darle un toque más atractivo y divertido para el usuario
print(' ._____. ._____. ._____. ._____.')
print(' | ._. | | ._. | | ._. | | ._. |')
print(' | !_| |_|_|_! | | !_| |_|_|_! |')
print(' !___| |_______! !___| |_______!')
print(' .___|_|_| |_________|_|_| |___.')
print(' | ._____| |_____________| |_. |')
print(' | !_! | | |         | | ! !_! |')
print(' !_____! | |         | | !_____!')
print(' ._____. | |         | | ._____.')
print(' | ._. | | |         | | | ._. |')
print(' | !_| |_|_|_________| |_|_|_! |')
print(' !___| |_____________| |_______!')
print(' .___|_|_| |___. .___|_|_| |___.')
print(' | ._____| |_. | | ._____| |_. |')
print(' | !_! | | !_! | | !_! | | !_! |')
print(' !_____! !_____! !_____! !_____!')
print()
print()

#Estos son los bancos de preguntas para cada tema, declarados en forma de diccionarios
#Cada diccionario tiene dos llaves, una para la pregunta y otra para la respuesta

base_lectura = {'preguntaL':['Lee esta frase: “Para evitar molestias menores, pero dolorosas, como ampollas, grietas o “pie de atleta” (infección por hongos)” (primera parte); “el calzado debe permitir la evaporación del sudor y evitar que penetre la humedad exterior” (segunda parte). ¿Cuál es la relación entre la primera y la segunda parte de la frase? La segunda parte…''\n''a) Contradice la primera parte.''\n''b) Repite la primera parte.''\n''c) Describe el problema planteado en la primera parte.''\n''d) Describe la solución al problema planteado en la primera parte.','Lee el siguiente texto una sóla vez: Ayer fuimos al zoo y vimos animales de muchos lugares del mundo. Había un hombre que nos lo enseñó. El animal que más me gustó fue el zorro. Tenía el hocico puntiagudo, las orejas grandes y una cola muy larga y peluda. Dicen que es muy listo.','¿Alguna vez te has levantado con la impresión de que algo iba mal? Así fue el día para mí. Me senté en la cama. Poco después descorrí las cortinas. El tiempo era horrible; estaba lloviendo a cántaros. Entonces, bajé la vista al patio. ¡Claro! Allí estaba la moto. Tan destrozada como la noche anterior. Y empezaba a dolerme la pierna. Algo le ocurrió al personaje de la historia la noche anterior. ¿Qué fue lo que le pasó? ''\n''a) El mal tiempo había estropeado la moto.''\n''b) El mal tiempo había impedido salir al personaje.''\n''c) El personaje había comprado una moto nueva.''\n''d) El personaje había tenido un accidente de moto','¿Por qué a veces los escritores comienzan sus textos con una pregunta? ''\n''a) Porque el escritor quiere saber la respuesta. ''\n''b) Para involucrar al lector en la historia. ''\n''c) Porque la pregunta es difícil de responder. ''\n''d) Para recordar al lector que este tipo de experiencia es poco corriente.','Pronto Rivière oiría ese avión; la noche abandonaba ya a uno de ellos, como un mar, lleno de flujo y reflujo y misterios, abandona en la orilla el tesoro que ha zarandeado tanto tiempo. Y más tarde, devolvería a los otros dos.''\n''a) Los dos esconden lo que hay en ellos. ''\n''b) Los dos son ruidosos. ''\n''c) Los dos son peligrosos para el hombre. ''\n''d) Los dos son silenciosos.','Lee el siguiente poema sólo una vez: Por las ramas del laurel vi dos palomas oscuras. La una era el sol; la otra, la luna. ¿Qué representan las palomas?','El oso es un animal salvaje, vive libre en la naturaleza. Su cuerpo está cubierto de pelo. Tiene la cabeza grande, los ojos pequeños, el hocico puntiagudo y las patas cortas y fuertes con uñas muy largas. Vive en una cueva que se llama osera. Sus cachorros se llaman oseznos y se alimentan de la leche de su madre. ¿Qué tipo de texto es el anterior?''\n''a)narrativo''\n''b)argumentativo''\n''c)descriptivo','Lee el siguiente texto sólo una vez: Beatriz estudia en un colegio de Málaga. En su clase reciclan el papel y los envases. Reciclar es hacer que algo que era para tirar se pueda volver a usar. Echan el papel en el contenedor azul y los envases en el amarillo. Ellos intentan que su clase este limpia y ordenada. ¿De qué color es el contenedor del papel?','Lee el siguiente texto una sóla vez: La gata de Marina se manchó en el jardín. La mancha era de chocolate y su madre lo bañó enseguida. Le echó un champú con olor a rosas. Desde aquel día la llamamos Rosita. ''\n''La gata es de María, ¿cierto o falso?','El pastelero''\n''El pastelero fabrica los dulces. Primero hace la masa. Después los mete en el horno. Al final les echa azúcar, nata y chocolate. ¿Cuál es el título de la lectura?','Lee el siguiente texto una sóla vez: Ayer estuve en el circo con mi familia. Salió un payaso con un pantalón rojo. A mi hermano le dio miedo y nos fuimos. ¿De qué color era el pantalón del payaso?','Lee el siguiente texto una sóla vez: La calle tiene una casa, la casa tiene una ventana, la ventana tiene un niño, el niño una hermosa flor.''\n''La casa tiene un buzón, ¿cierto o falso?','Lee el siguiente texto una sóla vez: La harina se hace moliendo los granos de trigo. El trigo es una planta que cuando es pequeña es una matita de color verde. En verano ya ha crecido y se pone de color amarillo. Después se siega y se recoge para hacer la harina.''\n''El trigo en verano es verde, ¿cierto o falso?','Ordena las palabras para formar una frase: buddy llama en y gusta perro el parque se correr mi le','Tipo de texto literario lírico compuesto por versos y que puede o no tener rima.'], 'respuestaL':['d','zorro','d','b','a','el sol y la luna','c','azul','falso','el pastelero','rojo','falso','falso','mi perro se llama buddy y le gusta correr en el parque','poema']}
base_mate = {'preguntaM':['La subida al Monte Fuji solo está abierta al público desde el 1 de julio hasta el 27 de agosto de cada año. Alrededor de unas 200.000 personas suben al Monte Fuji durante este periodo de tiempo. Como media, ¿alrededor de cuántas personas suben al Monte Fuji cada día?''\n''a)340''\n''b)710''\n''c)3400''\n''d)7100','Toshi llevó un podómetro para contar los pasos durante su recorrido por la ruta del Gotemba. Según el podómetro, dio 22.500 pasos en la ascensión. Calcula la longitud media del paso de Toshi en su ascensión de 9 km por la ruta del Gotemba. Expresa tu respuesta en centímetros (cm) y sin unidades.','En un concierto de rock se reservó para el público un terreno rectangular con unas dimensiones de 100 m por 50 m. Se vendieron todas las entradas y el terreno se llenó de fans, todos de pie. Considerando que caben 3 personas por metro cuadrado, ¿cuál de las siguientes cifras constituye la mejor estimación del número total de asistentes al concierto?''\n''a)1660 personas''\n''b)5000 personas''\n''c)3500 personas''\n''d)2760 personas','En el colegio de Irene, su profesora de ciencias les hace exámenes que se puntúan de 0 a 100. Irene tiene una media de 60 puntos de sus primeros cuatro exámenes de ciencias. En el quinto examen sacó 80 puntos. ¿Cuál es la media de las notas de Irene en ciencias después de los cinco exámenes?','Marta tiene 15 años, que es la tercera parte de la edad de su madre. ¿Qué edad tiene la madre de Marta?','Vicente se gasta 20 euros en un pantalón y una camisa. No sabe el precio de cada prenda, pero sí sabe que la camisa vale dos quintas partes de lo que vale el pantalón. ¿Cuánto vale el pantalón?','Calcular la altura que podemos alcanzar con una escalera de 3 metros apoyada sobre la pared si la parte inferior la situamos a 70 centímetros de ésta.','Si la hipotenusa de un triángulo rectángulo mide 2cm y uno de sus lados mide 1cm, ¿cuánto mide el otro lado?','¿Cuál de las siguientes sucesiones no es aritmética?''\n''a) 16, 26, 36, 46,...''\n''b) 16, 6, 13, 3,...''\n''c)-26, -36, - 46, -56,...','Calcular cuántos números impares hay entre 20 y 50 y calcular su suma.','En una bolsa hay 10 bolas numeradas del 11 al 20, algunas rojas y otras verdes. Si sacamos sin mirar una bola, ¿cuál es la probabilidad de sacar un número primo? Expresa tu resuesta como decimal.','Una clase consta de 10 hombres y 20 mujeres; la mitad de los hombres y la mitad de las mujeres tienen los ojos castaños. Determinar la probabilidad de que una persona elegida al azar sea un hombre o tenga los ojos castaños. Expresa tu respuesta como fracción.','En una panadería, con 80 kilos de harina hacen 120 kilos de pan. ¿Cuántos kilos de harina serían necesarios para hacer 99 kilos de pan?','Para construir una casa en ocho meses han sido necesarios seis albañiles. ¿Cuántos habrían sido necesarios para construir la casa en tan sólo tres meses?','Un padre reparte un premio de lotería de 9.300 € en proporción inversa a las edades de sus hijos, que son 6, 8, 12 y 18 años. Halla lo que corresponde al hijo de 18 años.'], 'respuestaM':['c','40','a','64','45','14.29','2.92','1.73','b','525','0.4','2/3','66','16','1200']}
base_ciencia = {'preguntaC':['La mayoría de las aves migratorias se reúnen en un área y después migran en grandes grupos en lugar de hacerlo individualmente. Este comportamiento es resultado de la evolución. ¿Cuál de las siguientes es la mejor explicación científica para la evolución de este comportamiento en la mayoría de las aves migratorias?''\n''a) Las aves que migran individualmente o en pequeños grupos tienen menos chances de sobrevivir y reproducirse.''\n''b) Las aves que migran individualmente o en pequeños grupos son más propensas a encontrar comida suficiente.''\n''c) Volar en grandes grupos permite que otras especies de aves se unan a la migración.''\n''d) Volar en grandes grupos permite a cada ave tener una mejor chance de encontrar un sitio para anidar.','Las rocas en el espacio que entran en la atmósfera de la Tierra se llaman meteoroides. Los meteoroides se calientan y brillan mientras caen a través de la atmósfera. La mayoría se consume antes de llegar a la superficie terrestre. Cuando un meteoroide choca contra la Tierra puede crear un agujero llamado cráter. A medida que el meteoroide se acerca a la Tierra y su atmósfera, acelera. ¿Por qué ocurre esto?''\n''a) El meteoroide es halado por la rotación de la Tierra''\n''b) El meteoroide es empujado por la luz del sol' '\n' 'c) El meteoroide es atraído por la masa de la Tierra''\n''d) El meteoroide es rechazado por el vacío del espacio','¿Cuánto se tarda en recorrer una distancia de 10km a una velocidad de 40 km/h? Expresa tu respuesta en minutos.','La distancia entre las ciudades A y B es de 50km. A la misma hora, salen un camión de la ciudad A a 60km/h y un ciclista de la ciudad B a 25km/h. Se desea calcular cuánto tardarán en encontrarse si ambos vehículos circulan por la misma carretera pero en sentido opuesto. Expresa tu respuesta en minutos.','Completa el texto: el cambio de estado de la materia por el cual se pasa de estado ________ se denomina condensación.''\n''a) líquido-gaseoso''\n''b) líquido-sólido''\n''c) sólido-líquido''\n''d) gaseoso-líquido','¿Cómo se llama la galaxia donde se ubica el sistema solar?','Centro de control de la célula:''\n''a)Aparato de Golgi''\n''b)Citoplasma''\n''c)Núcleo','Órgano celular en el que se realiza la fotosíntesis:''\n''a)Cloroplasto''\n''b)Citoplasma''\n''c)Libosoma','Los ____ se encargan de sintetizar proteínas.','Da forma y soporta a la célula:''\n''a)Citoesqueleto''\n''b)Núcleo''\n''c)Pared celular','Son creadas por el aparato de Golgi: ''\n''a)Libosomas''\n''b)Centriolos''\n''c)Peroxisomas','La célula obtiene la energía de las ___.','Las bacterias y las arqueas forman parte del tipo de célula ___.','Las células vegetales tienen ____ y éstas almacenan, alimentos, agua y desechos.','La ___ ___ es rígida y rodea a las células vegetales.'], 'respuestaC':['a','c','15','35.4','d','via lactea','c','a','ribosomas','a','b','mitocondrias','procariota','vacuolas','pared celular']}
base_fun = {'preguntaF':['¿Cuál es el nombre real de Spiderman?','¿En qué ciudad se encuentra la Torre Eiffel?','¿Cuál es el segundo planeta del sistema solar?','¿Cuántas patas tiene una araña?','¿Cómo se llama el enemigo de Hércules?','¿Quién es es personaje principal de Piratas del Caribe?','Completa la frase: Hasta la ____, baby.','La capa de Superman es color ____.','¿Cómo se llama el mejor amigo de Bob Esponja?','¿Cuál es nombre del dragón de Mulán?','¿De qué color es el caballo blanco de Napoleón?','¿Cada cuántos años se llevan a cabo los Juegos Olímpicos?','¿Cuál es la letra número 14 del alfabeto?','¿Qué arma utiliza Katniss Everdeen en los Juegos del Hambre?','¿Cómo se llama la canción más famosa de John Lennon?'], 'respuestaF':['peter parker','paris','venus','8','hades','jack sparrow','vista','rojo','patricio','mushu','blanco','4','n','arco y flecha','imagine']}

#Esta es la función que hace "girar" la ruleta en cada turno del jugador
#La ruleta tiene tres posibles opciones, correspondientes a los tres temas de la prueba PISA


def ruleta():
    '''Esta función representa la ruleta y genera un número aleatorio para seleccionar el tema.
       Aquí también se valida la tecla ingresada por el usuario'''
    print()
    print('Ingresa "x" para girar la ruleta.')
    girar = input()
    
    while girar != 'x':
        print('Tecla inválida. Ingresa "x" para girar la ruleta.')
        girar = input()
        print()
        
    else:
        tema = random.randint(1,3)
        if tema == 1:
            print('Te tocó Comprensión Lectora.')
            print('  /////|')
            print(' ///// |')
            print('|~~~|  |')
            print('|===|  |')
            print('|e  |  |')
            print('| s |  |')
            print('|  p| / ')
            print('|===|/  ')
            print(' ---    ')
            print()
            
        elif tema == 2:
            print('Te tocó Matemáticas.')
            print(' __________ ')
            print('| ________ |')
            print('||12345678||')
            print('|""""""""""|')
            print('|[M|#|C][-]|')
            print('|[7|8|9][+]|')
            print('|[4|5|6][x]|')
            print('|[1|2|3][%]|')
            print('|[.|O|:][=]|')
            print('"----------"')
            print()
            
        elif tema == 3:
            print('Te tocó Ciencias.')
            print('     __         ')
            print('     ||         ')
            print('    ====        ')
            print('    |  |__      ')
            print('    |  |-.\     ')
            print('    |__|  \\    ')
            print('     ||   ||    ')
            print('   ======__|    ')
            print('  ________||__  ')
            print(' /____________| ')
            print()
            print()
            
    return(tema)

def dibujo_respuesta_correcta():
    '''Imprime un dibujo si el usuario contesta correctamente en el primer intento'''
    print('       ______        ____    ')
    print('      /_____/\      /___/|   ')
    print('     /      \ \   __|  | |__ ')
    print('    /   /\   \/| /__|  |/__/|')
    print('    |  | ||  | ||___    ___|/')
    print('    |  |/_|  | |    |  | |   ')
    print('    |   __   | |    |__|/    ')
    print('    |  | ||  | |             ')
    print('    |  | ||  | |             ')
    print('    |__|/ |__|/              ')
    print()
    
def dibujo_segundo_intento():
    '''Imprime un dibujo si el usuario contesta correctamente en el segundo intento'''
    print('     _        ')
    print('   _| |       ')
    print(' _| | |       ')
    print('| | | |       ')
    print('| | | | __    ')
    print('| | | |/  \   ')
    print('|       /\ \  ')
    print('|      /  \/  ')
    print('|      \  /\  ')
    print('|       \/ /  ')
    print(' \        /   ')
    print('  |     /     ')
    print('  |    |      ')
    print()

def dibujo_respuesta_incorrecta():
    '''Imprime un dibujo motivacional si el usuario responde incorrectamente'''
    print(' ____________________ ')
    print('|                    |')
    print('| ¡Puedes hacerlo    |')
    print('|       mejor!       |')
    print('\____________________/')
    print('         !  !         ')
    print('         L_ !         ')
    print('        / _)!         ')
    print('       / /__L         ')
    print(' _____/ (____)        ')
    print('        (____)        ')
    print(' _____  (____)        ')
    print('      \_(____)        ')
    print('         !  !         ')
    print('         \__/         ')
    print()
     
puntaje = 0

#En este ciclo while se va acumulando el puntaje del jugador
while puntaje <= 20:
    #Esta línea valida cuándo saldra la pregunta bonus
    if puntaje != 5 and puntaje != 10 and puntaje != 15 and puntaje != 20:
        tema = ruleta()
        #La seguiente línea hace la selección de la pregunta dependiendo del tema
        num_pregunta = random.randint(0,14)
        
        #A partir de aquí inicia el mecanismo de interacción con el juegador
        if tema == 1:
            #Primero se despliega la pregunta
            print(base_lectura['preguntaL'][num_pregunta])
            #Se espera la respuesta del jugador
            respuesta_usuario = input()
            
            #Si su respuesta es correcta avanza un lugar
            if respuesta_usuario == base_lectura['respuestaL'][num_pregunta]:
                print('¡Respuesta correcta! Avanzas un lugar.')
                dibujo_respuesta_correcta()
                puntaje += 1
                print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                print()
                #Si su respuesta es incorrecta le da una segunda oportunidad
                
            else:
                print('Respuesta incorrecta. Intenta de nuevo.')
                respuesta_usuario = input()
                if respuesta_usuario == base_lectura['respuestaL'][num_pregunta]:
                    print('¡Respuesta correcta! Avanzas un lugar.')
                    dibujo_segundo_intento()
                    puntaje += 1
                    print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                    print()
                    
                #Si su respuesta es nuevamente incorrecta retrocede un lugar
                else:
                    print('Respuesta incorrecta. Retrocedes un lugar.')
                    print('La respuesta correcta es: ' + base_lectura['respuestaL'][num_pregunta])
                    dibujo_respuesta_incorrecta()
                    if puntaje > 0:
                        puntaje -= 1
                        print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                    
                    #Esta condición sólo se aplica si su puntaje es 0
                    elif puntaje == 0:
                        puntaje = 0
                        print('Respuesta incorrecta.')
                        print(' '*(20)+'^^Meta^^')
                        print()
        
        #El proceso anterior se repite para los otros dos temas
        elif tema == 2:
            print(base_mate['preguntaM'][num_pregunta])
            respuesta_usuario = input()
            
            if respuesta_usuario == base_mate['respuestaM'][num_pregunta]:
                print('¡Respuesta correcta! Avanzas un lugar.')
                dibujo_respuesta_correcta()
                puntaje += 1
                print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                print()
                
            else:
                print('Respuesta incorrecta. Intenta de nuevo.')
                respuesta_usuario = input()
                
                if respuesta_usuario == base_mate['respuestaM'][num_pregunta]:
                    print('¡Respuesta correcta! Avanzas un lugar.')
                    dibujo_segundo_intento()
                    puntaje += 1
                    print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                    print()
                    
                else:
                    print('Respuesta incorrecta. Retrocedes un lugar.')
                    print('La respuesta correcta es: ' + base_mate['respuestaM'][num_pregunta])
                    dibujo_respuesta_incorrecta()
                    
                    if puntaje > 0:
                        puntaje -= 1
                        print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                    elif puntaje == 0:
                        print('Respuesta incorrecta.')
                        print(' '*(20)+'^^Meta^^')
                        print()
                        
        elif tema == 3:
            print(base_ciencia['preguntaC'][num_pregunta])
            respuesta_usuario = input()
            
            if respuesta_usuario == base_ciencia['respuestaC'][num_pregunta]:
                print('¡Respuesta correcta! Avanzas un lugar.')
                dibujo_respuesta_correcta()
                puntaje += 1
                print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                
            else:
                print('Respuesta incorrecta. Intenta de nuevo.')
                respuesta_usuario = input()
                
                if respuesta_usuario == base_ciencia['respuestaC'][num_pregunta]:
                    print('¡Respuesta correcta! Avanzas un lugar.')
                    dibujo_segundo_intento()
                    puntaje += 1
                    print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                    print()
                    
                else:
                    print('Respuesta incorrecta. Retrocedes un lugar.')
                    print('La respuesta correcta es: ' + base_ciencia['respuestaC'][num_pregunta])
                    dibujo_respuesta_incorrecta()
                    
                    if puntaje > 0:
                        puntaje -= 1
                        print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                    elif puntaje == 0:
                        print('Respuesta incorrecta.')
                        puntaje = 0
                        print(' '*(20)+'^^Meta^^')
                        
    else:
        #En esta parte del código se generan las preguntas bonus
        if puntaje != 20:
            print()
            print('¡Felicidades! Puedes contestar la pregunta para obtener un bonus de 2 puntos. Si tu respuesta es incorrecta sólo ganarás un punto.')
            print(base_fun['preguntaF'][num_pregunta])
            respuesta_usuario = input()
            
            if respuesta_usuario == base_fun['respuestaF'][num_pregunta]:
                print('¡Respuesta correcta! Avanzas dos lugares.')
                dibujo_respuesta_correcta()
                puntaje += 2
                print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                print()
                
            else:
                print('Respuesta incorrecta. Aún así, avanzas un lugar.')
                dibujo_segundo_intento()
                puntaje += 1
                print('*'*puntaje +' '*(20-puntaje)+'^^Meta^^')
                
        else:
            print('¡Felicidades, ganaste!')
            print('  _______  ')
            print(' |       | ')
            print('(| PISA  |)')
            print(' |  #1   | ')
            print('  \     /  ')
            print('   `---´   ')
            print('   _|_|_   ')
            break
        
    