### ATRIBUIÇÕES DAS VARIÁVEIS ####################

fila = []
fila_dos_desistentes = []
cliente = []
opcao = ""
senha = 0 
desistencias = 0
clientes_atendidos = 0
tempo_de_espera = [] # Lista para guardar o tempo de espera de cada cliente
   

### INÍCIO DO PROGRAMA ############################

print()
print("=== FILA BANCÁRIA. ESCOLHA UMA OPÇÃO ===")
print("G - Gerar senha comum")
print("P - Gerar senha preferencial")
print("C - Chamar próximo cliente")
print("A - Avançar tempo")
print("F - Exibir fila")
print("E - Exibir estatísticas")
print("S - Sair")

while opcao != "S":
 print()
 opcao = input("Escolha uma opção: ").upper()
 print()

 match opcao:
 
 # Senha para clientes comuns
    case "G":
       senha += 1
       cliente = [senha, "G", 0]
       fila.append(cliente)
       print(f"Senha {senha} gerada para cliente comum.")
       
 # Senha para clientes preferenciais
    case "P":
       senha += 1
       cliente = [senha, "P", 0]
       fila.append(cliente)
       print(f"Senha {senha} gerada para cliente preferencial.")
       
 # Chamada dos clientes
    case "C":
       if len(fila) > 0:
          tem_P = False # Para verificar se existem clientes preferenciais na fila
          tem_G_maior_q_8 = False # Para verificar se existem clientes comuns com tempo>8 na fila         
          maior_tempo = -1
          for pessoa in fila:
             if "P" in pessoa:
                tem_P = True
             if pessoa[1] == "G" and pessoa[2] >= 8:
                tem_G_maior_q_8 = True
             if pessoa[1] == 'P' and pessoa[2]>maior_tempo:
                maior_tempo = pessoa[2] # Guarda o maior tempo de espera dentre os clientes preferenciais     
          for i, pessoa in enumerate(fila):
             if tem_G_maior_q_8:   
                if pessoa[1] == 'P' and pessoa[2] == maior_tempo:                                     
                   tempo_de_espera.append(pessoa[2])
                   clientes_atendidos += 1
                   senha_pessoal = fila[i][0]
                   tipo_cliente = fila[i][1]
                   esperou = fila[i][2]                  
                   fila.pop(i)                                
                   print('Cliente chamado:')
                   print(f'Senha {senha_pessoal} | Tipo {tipo_cliente} | Tempo {esperou}')           
                   break
                elif pessoa[1] == "G" and pessoa[2] > maior_tempo:
                   tempo_de_espera.append(pessoa[2])
                   clientes_atendidos += 1
                   senha_pessoal = fila[i][0]
                   tipo_cliente = fila[i][1]
                   esperou = fila[i][2]                  
                   fila.pop(i)                                
                   print('Cliente chamado:')
                   print(f'Senha {senha_pessoal} | Tipo {tipo_cliente} | Tempo {esperou}')                  
                   break                                 
             elif tem_P:
                if pessoa[1] == "P":
                   tempo_de_espera.append(pessoa[2])
                   clientes_atendidos += 1
                   senha_pessoal = fila[i][0]
                   tipo_cliente = fila[i][1]
                   esperou = fila[i][2]                  
                   fila.pop(i)                                
                   print('Cliente chamado:')
                   print(f'Senha {senha_pessoal} | Tipo {tipo_cliente} | Tempo {esperou}')           
                   break       
                else:
                   continue
             else:
                tempo_de_espera.append(pessoa[2])
                clientes_atendidos += 1
                senha_pessoal = fila[i][0]
                tipo_cliente = fila[i][1]
                esperou = fila[i][2]                  
                fila.pop(i)                                
                print('Cliente chamado:')
                print(f'Senha {senha_pessoal} | Tipo {tipo_cliente} | Tempo {esperou}')               
                break
       else:
          print('A fila está vazia.')                

 # Avanço do tempo
    case "A":
       print('O tempo foi avançado em 1 unidade.')      
       for i, pessoa in enumerate(fila):
          pessoa[2] += 1   
       for i in range(len(fila) - 1, -1, -1):
            pessoa = fila[i]
            if pessoa[2] >= 10:
               desistente = fila.pop(i)
               fila_dos_desistentes.insert(0, desistente) 
               desistencias += 1
       if len(fila_dos_desistentes)>0:
          print()
          print('Desistiu:')
          for i in range(len(fila_dos_desistentes)):
             senha_pessoal = fila_dos_desistentes[i][0]
             tipo_cliente = fila_dos_desistentes[i][1]
             esperou = fila_dos_desistentes[i][2]
             print(F'Senha {senha_pessoal} |  Tipo {tipo_cliente}  | Tempo {esperou}')
          del fila_dos_desistentes[:]               

# Exibição da fila
    case "F":                         
       if len(fila) == 0:
          print('A fila está vazia.')  
       else:
          print('Fila atual:')
          for i in range(len(fila)):
             senha_pessoal = fila[i][0]
             tipo_cliente = fila[i][1]
             esperou = fila[i][2]
             print(F'{i+1}°  Senha {senha_pessoal} |  Tipo {tipo_cliente} |  Tempo {esperou}')
          
# Estatisticas
    case "E":
       print(f'Total de senhas geradas: {senha}')
       print(f'Total de clientes atendidos: {clientes_atendidos}')
       print(f'Total de clientes que desistiram: {desistencias}')
       print(f'Quantidade de clientes que ainda aguardam na fila: {len(fila)}')
       if clientes_atendidos == 0:
          print('Ainda não é possível calcular o tempo médio de espera dos clientes atendidos.')
       else:
          media = sum(tempo_de_espera)/clientes_atendidos
          print(f'Tempo médio de espera dos clientes atendidos: {media:.2f}')
        
           
    case "S":
       print("Encerrando o programa.")
       print()
 
    case _:
       print("Opção inválida.")