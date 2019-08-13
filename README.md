### Software Avanzado - Tarea 2 - 201504429
![alt text](https://github.com/gamgustavo/sat2/blob/master/arquitectura.PNG)



# Clientes
- crear_cliente
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- number;
      - [ ] nombre -- nombre;
      - [ ] apellido -- apellido;
      - [ ] logitud -- logitud;
      - [ ] latitud -- latitud; 
  - [ ] result: Cliente creado;
- get_cliente
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] nombre -- nombre 
  - [ ] result: Cliente creado;  
  

# Conductores
- crear_conductor
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- number;
      - [ ] nombre -- nombre;
      - [ ] apellido -- apellido;
      - [ ] automotor -- automotor;      
      - [ ] logitud -- logitud;
      - [ ] latitud -- latitud; 
  - [ ] result: Cliente creado;
- get_conductor
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- number 
  - [ ] result: Cliente creado;    
# Rastreo
- get_posicion
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- numero de identificacion de persona o conductor
      - [ ] Tipo -- PERSONA/CONDUCTOR      
  - [ ] result: POSICION;

- set_posicion
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- numero de identificacion de persona o conductor
      - [ ] Tipo -- PERSONA/CONDUCTOR     
      - [ ] longitud -- longitud     
      - [ ] latitud -- latitud          
  - [ ] result: POSICION;  
- update_posicion
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- numero de identificacion de persona o conductor
      - [ ] Tipo -- PERSONA/CONDUCTOR     
      - [ ] longitud -- longitud     
      - [ ] latitud -- latitud          
  - [ ] result: POSICION;    
  
# Viajes

- crear_cliente
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number cliente -- number;
      - [ ] nombre cliente -- nombre;
      - [ ] number piloto -- number;
      - [ ] nombre piloto -- nombre;      
      - [ ] logitud_cliente -- logitud;
      - [ ] latitud_cliente -- latitud; 
      - [ ] logitud_conductor-- logitud;
      - [ ] latitud_conductor-- latitud;       
  - [ ] result: Vieaje creado;
# EBS
- crear_cliente
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- number;
      - [ ] nombre -- nombre;
      - [ ] apellido -- apellido;
      - [ ] logitud -- logitud;
      - [ ] latitud -- latitud; 
  - [ ] result: Cliente creado;
- crear_conductor
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- number;
      - [ ] nombre -- nombre;
      - [ ] apellido -- apellido;
      - [ ] automotor -- automotor;      
      - [ ] logitud -- logitud;
      - [ ] latitud -- latitud; 
  - [ ] result: Cliente creado;

- pedir_uber
  - [ ] Methotd: POST;
  - [ ] params:;
      - [ ] number -- number;
      - [ ] nombre -- nombre;
      - [ ] apellido -- apellido;
      - [ ] automotor -- automotor;      
      - [ ] logitud -- logitud;
      - [ ] latitud -- latitud; 
  - [ ] result: viaje creado;

# Editor.md