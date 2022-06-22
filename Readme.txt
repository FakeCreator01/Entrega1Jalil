Guardería para bebes

Web donde los padres pueden entrar y ver la lista de bebes dentro de la guardería. Así cómo tambíen pueden ver las niñeras que los cuidarán y pueden sugerir comidas para sus hijos.
Los administradores tendrán más permisos dentro de la página y podrán registrar bebes nuevos, niñeras nuevas, ver que bebe está vacunado y cual no y ver el 'ID' de todos los bebes (la guardería tiene un sistema de identificación propio de 1 o más digitos llamado 'ID').



NOTA: 
- Por convención no utilize la letra 'ñ' en la palabra "Niñeras". En vez de ello usé 'Ninieras'.
- El nombre del proyecto django por convención es 'src'


Detalles técnicos:

- MODELOS:

Sólo se utilzo una app 'AppGuarderia' donde se crearon las siguientes tablas:
'Bebe' con los campos: 'Nombre', 'Edad' y 'Vacunado'
'Niniera' con los campos: 'Nombre', 'Edad' y 'Años_experiencia'
'Comida' con los campos: 'Nombre' y 'Gramos'

- FORMULARIOS:
En el archivo 'forms.py' se utilizaron tres ModelForm para cada modelo: 'BebeForm', 'NinieraForm' y 'ComidaForm'. Cada uno con los campos nombrados anteriormente.

- VISTAS: 

En cuanto a las views, se utilizaron cinco, cuatro para la 'AppGuarderia' que son:
'Buscar': que guarda la logica del buscador que tenemos en inicio
y 'Bebe', 'Niniera' y 'Comida' donde se guarda la logica de un formulario para registrar un objeto nuevo.
y una para el projecto general en 'src':
'Inicio': donde enlisté todas las ninieras y las comidas sugeridas, así cómo también un buscador de bebes.

- URLS Y LINKS:

Cada view se registró en el archivo 'urls.py' donde cuando se hace una solicitud a una determinada url, dirige al cliente a un template.
Hay dos archivos urls.py -> el del proyecto que redirije al inicio (localhost:8000/) y el de la AppGuarderia que redirije a:

'/bebes' Donde se registraran bebes nuevos
'/ninieras' Donde se registran ninieras nuevas
'/comidas' Donde se sugieren (y registran) comidas nuevas
'/buscar' Donde a travez del metodo GET se busca un bebe

- TEMPLATES:

En este caso contamos con 5 templates:
El html padre 'base.html' que se usará para heredar su estructura básica y ahorrar código.

La pagina de inicio 'inicio.html' que mostrará una lista de niñeras y comidas. También cuenta con un buscador donde se podrá buscar un bebe por su nombre. En caso que haya registrado un objeto en el modelo del tipo 'Bebe' con ese nombre, se mostrará el resultado. En caso contrario que no esté registrado, se mostrará un mensaje de error. Y en caso que no se haya escrito nada y se de a 'buscar' se mostrara otro mensaje que dirá 'No enviaste datos.'

Los formularios 'bebes.html', 'comidas.html' y 'ninieras.html' que se usarán para crear un objeto nuevo.

