import socket
import random
import pickle
import time
HOST = "192.168.100.62"  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 65433  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 1024
turno="0"
datoenv=[]
dato=[]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Esperando a recibir datos... ")
        inicio=time.time()
        while True:
               
               dato=[]
               datobuffer=[]
               datobuffer=Client_conn.recv(buffer_size)
               dato=pickle.loads(datobuffer)
                # print(f"puntos del cliente:{dato[3]}")
                #print(f"puntos del servidor:{dato[4]}")
               print(dato)
               if dato[5]=="termino":
                    break
                    
                turno=dato[0]
                while turno=="1":
                    datoenv=[]
                    print("TURNO DEL SERVIDOR")
                    par1=dato[1]
                    par2=dato[2]
                    
                    datoenv.append("0")
                  

                    if par1==par2:
                        print("obtuvo un punto el cliente!")
                        datoenv.append("1")
                    
                        #puntajeganador=puntajeganador-1
                    else:
                        print("el cliente envio una respuesta equivocada")
                        cordenadas=[]
                        for i in range(4):
                             num=random.randint(0,3)
                             cordenadas.append(num)
                        print(cordenadas)
                        datoenv.append("0")
                        datoenv.append(cordenadas)

                        
                
                  
                    datoenvbuffer=pickle.dumps(datoenv)
                    Client_conn.send(datoenvbuffer)
            
                    turno="0"
                    
        print(f"puntos del cliente:{dato[3]}")
        print(f"puntos del servidor:{dato[4]}")
        fin=time.time()
        tiempo=fin-inicio
        if dato[3]>dato[4]:
             ganador="el ganador es el cliente con "+str(dato[3])+" puntos"
        elif dato[4]>dato[3]:
             ganador="el ganador es el servidor con "+str(dato[4])+" puntos"
        else:
             ganador="empate"

        puntajefinal=ganador+" y el tiempo que tardo la partida es : "+str(tiempo)+" segundos"
        Client_conn.send(puntajefinal.encode())           
       
        #while True:
            
            #if not dificultad:
             #   break
            
	      
           
            

