import random
from ta_state import *


def alocacao(arq):
    agents = []
    agentes = 0
    arquivo = open(arq,'r')
    data = arquivo.readlines()
    ind_agente = 0
    for line in data:
        if "end" in line:
            ind_agente = 1
            continue
        else:
            if ind_agente == 1:
                agents.append([int(line),[]])
                agentes = agentes + 1
                ind_agente = 0
            else :
                line = line.replace("(","")
                line = line.replace(")\n","")
                dado = line.split(", ")
                loc = Location(int(dado[0]),int(dado[1]))
                # col = int(dado[0])
                # row = int(dado[1])
                agents[agentes-1][1].append(loc)
    arquivo.close()


    for i in range(len(agents)):
        r = random.randint(0,1)
        if r == 0:
            agents[i].append(1)
        else:
            agents[i].append(2)

    agente_temp = []
    max = 0
    a = 0
    for agente_atual in agents:
        temp = []
        r = 0
        for posicao_atual in agente_atual[1]:
            repeticao = 0
            for i in range(len(agents)):
                if i != agente_atual[0]-1:
                    f = 0
                    for loc in agents[i][1]:
                        if loc == posicao_atual and r == f - 1:
                            repeticao = repeticao + agents[i][2] + 1
                        f = f + 1
            if repeticao > 0:
                for t in range(repeticao):
                    temp.append(agente_atual[1][r-1])
            for t in range(agente_atual[2]):
                temp.append(posicao_atual)
            r = r + 1
        if len(temp) > max:
            max = len(temp)
        agents[a][1] = temp
        a = a + 1
        agente_temp.append([agente_atual[0],temp])
    
    for agente in agente_temp:
        if len(agente[1]) < max:
            fim = agente[1][len(agente[1])-1]
            for i in range(max-len(agente[1])):
                agente[1].append(fim)

    print(max)
    for agente in agente_temp:
        print(agente[0]," ",len(agente[1]))

    return agente_temp


# alocacao('caminhos.txt')
# print("fim")
# print("fim")

# print(conta)