POS Tapices
==============

Este módulo agregará  la información de la empresa en el recibo de POS. También se imprimirá el nombre del cliente.
en el recibo si el cliente es seleccionado.
Tambien agregara los elementos que son requeridos en una factura  de acuerdo con los lineamientos del SAR.

PRESENTADO POR :
=======


* ENID SIERRA 20151004892.
* FERNANDO PADILLA  20141002444.

CAMBIOS REALIZADOS:

Cambios realizados en el archivo pos.xml ubicado en static/src/xml/ que define la composicion de los datos vistos en la factura .
agregacion de nuevos campos en base de datos tales como RTN , codigo CAI entre otros.

Se cambion la vista de los datos de la empresa agregrando los nuevos campos , esto se ve reflejado en el archivo views/tapices.xml.
Para poder obtener los datos guardados en la base de datos capturados en la vista antes mencionada se modifico el archivo models.js 
ubicado en la caperta js.



DIFICULTADES:
* INSTALAR ODOO MEDIANTE UNA MÁQUINA VIRTUAL RESUSLTÓ SER MUY COMPLICADO YA QUE LOS COMANDOS SON DIFERENTES A LOS DE WINDOWS, ASÍ COMO EL BAJO RENDIMIENTO QUE PUEDE PRESENTAR EL USAR UNA VM.
PROBLEMAS AL INSTALAR LOS MODULOS; AL ELIMINAR UN MODULO O DESINTALARLO POR COMPLETO. SE NECESITÓ CREAR UNA NUEVA BASE DE DATOS.
* LAS PRIORIDADES O DEPENDENCIAS DE LOS MÓDULOS COMPLICARON LA APLICACIÓN DE LOS MISMOS, POR LO QUE CIERTOS MODULOS QUEDARON LIGADOS A OTROS.
CURVA DE APRENDIZAJE PARA USAR ODOO MEDIANTE GIT.

OBSERVACIONES:

* HAY UN GRAN NÚMERO DE MÓDULOS PARA DIFERENTES USOS Y ÁREAS.
* LOS MÓDULOS SON FÁCILES DE USAR UNA VEZ FUERON IMPLEMENTADOS.
* LOS MÓDULOS SE INTEGRAN MUY BIEN ENTRE SÍ.
* AYUDA MUCHO SÍ SE ESTÁ CORTO DE PRESUPUESTO.

CONSIDERACIONES FINALES:

ODOO ES UNA EXCELENTE HERRAMIENTA PARA IMPLEMENTAR EN UNA EMPRESA O NEGOCIO, UNA VEZ ENTENDIDO EL CONCEPTO DE LA APLICACIÓN SE LE PUEDE SACAR MUCHO PROVECHO.
  

  NOTA::::
  
  Para instalarlo descargar carpeta point_of_sale en la carpeta addons de ODOO.
