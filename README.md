# SISTEMA DE INVETARIO

## Funcionalidad

El sistema de inventarios es un programa diseñado para manejar inventarios en tiendas cuenta con una interfaz de menu para que el usuario pueda navegar por las funciones deseadas a su gusto las cuales son:

**Agregar productos:**
Permitir al usuario agregar productos con atributos como nombre, precio y cantidad disponibles.

**Buscar productos en el inventario:**
Permite al usuario buscar un producto por su nombre y mostrar sus detalles (nombre, precio, cantidad).

**Actualizar precio de producto:**
Permite al usuario modificar el precio de un producto específico en el inventario.

**Eliminar Productos:**
Permite al usuario la eliminación de un producto que ya no está disponible.

**Calcular el valor total de los productos en inventario:**
Permite calcular el valor total del invetario.

**Salir del programa:**
Permite salir del programa

## Modo de uso
Al iniciar el programa se abre el menu de opciones donde puedes navegar por las multiples funcionalidades de este, el primer paso para usarlo es ingresar 5 productos al inventario para debloquear las demas funcionallidades excepto salir del programa que no necesita esta esta condicion.
Puedes seleccionar unas de las siguientes opciones para interactuar con el programa:

![imagen](https://github.com/user-attachments/assets/5f1e48a6-2ebc-4ca7-846a-6cf21550b8ce)


**Opción 1: Agregar productos:**
- Se solicita el nombre del producto al usuario, valida que no ingrese campos vacios y que el producto ingresado no este en el inventario.
- Se solicita el precio del producto, la cantidad y valida que los datos ingresados sean numeros positvos.
- El programa añade los productosal inventario, para cuando el usuario no quiere ingresar mas productos y vuelve al menu.
  ![imagen](https://github.com/user-attachments/assets/667db5be-973f-4422-8725-b8e228dfb11b)
- El programa no deja avanzar si se ingresan valores negativos
  ![imagen](https://github.com/user-attachments/assets/e2768367-2790-4e5c-86c7-e92759e2ca34)


**Opción 2: Buscar productos en el inventario.**
- Primero se solicita que ingrese un producto a buscar, se valida la entrada de dato, y se valida que el producto este creado en el inventario.
- Muestra los detalles del producto como los son nombre, precio por unidad, cantidad y precio total de todas la unidades.
![imagen](https://github.com/user-attachments/assets/9cb73812-369c-456e-abaa-6dd8f14011e4)


**Opción 3: Actualizar precio de producto.**
- Primero se solicita que ingrese el producto que desea modificar, se valida la entrada de dato, y se valida que el producto este creado en el inventario.
- Se valida que el producto ingresado es el que se deasea modificar.
- Se solicita el nuevo valor de producto y se modifica en el inventario
  ![imagen](https://github.com/user-attachments/assets/ca3e830b-bad6-487d-8235-e419cd29c4fb)

**Opción 4: Eliminar Productos.**
- Primero se solicita que ingrese el producto que desea eliminar, se valida la entrada de dato, y se valida que el producto este creado en el inventario.
- Se valida que el producto ingresado es el que se desea eliminar.
  ![imagen](https://github.com/user-attachments/assets/115154e5-eedf-4788-bbef-efd8357b2be3)
- El programa solo deja eliminar productos sin existencia en el inventario, si se intenta eliminar unos con existencia este le informara que no se puede eliminar.
  ![imagen](https://github.com/user-attachments/assets/a72ca1e4-ecbc-4fec-8173-f9943bacf61c)


**Opción 5: Calcular el valor total de los productos en inventario.**
- El programa toma la cantidad de cada producto y la multiplica por su precio individual.
- Suma todos los resultados de cada priducto e imprime el resultado de el valor total de los productos en inventario.
  ![imagen](https://github.com/user-attachments/assets/ec71f1f9-d0ec-448b-b274-9b9570671e83)


**Opción 6: Salir del programa.**
- Se usa para salir del programa
![imagen](https://github.com/user-attachments/assets/09ca44ec-b575-4c13-bbfa-38c8e7f64772)


