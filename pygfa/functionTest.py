from gfa import GFA
from graph_element.node import Node
from graph_element.edge import Edge
from graph_element.subgraph import Subgraph
import random
from graph_element.parser.segment import SegmentV1
from graph_element.parser.segment import SegmentV2
from graph_element.parser.line import Line,Field,OptField
from graph_element.parser.link import Link
from graph_element.parser.containment import Containment
import string
from graph_element.parser.path import Path


import time
import psutil  # modulo per monitorare l'uso di memoria
grafo=GFA()
# Funzione per costruire e salvare il grafo
def costruisci_e_salva_grafo():
    # Logica per costruire il grafo
    nucleotidi = "ACGT"
    numnodi= input("Inserire numero nodi: ")
    numarchi=input("Inserire numero archi: ")
    #randomEid = random.randint(0, 999999)

    for _ in range(int(numnodi)):
        lungh = random.randint(4, 10)
        node_id = str(_ + 1)
        sequence = ''.join(random.choice(nucleotidi) for _ in range(lungh))
        grafo.from_string(f"S\t{node_id}\t{sequence}")

        #seq = ''.join(random.choice(nucleotidi) for _ in range(lungh))
        #nodo = Node(node_id=str(nid), sequence=seq, length=len(seq))
        #grafo.add_node(nodo)

    for _ in range(int(numarchi)):

        from_node = str(random.randint(1, int(numnodi)))
        to_node = str(random.randint(1, int(numnodi)))
        from_orient = random.choice(['+', '-'])
        to_orient = random.choice(['+', '-'])
        details = f"{random.randint(1, 10)}M"
        while not(from_node == to_node or (from_node , to_node ) in grafo.edges()):
         grafo.from_string(f"L\t{from_node}\t{from_orient}\t{to_node}\t{to_orient}\t{details}")

       # nodoCasuale = random.randint(0, int(numnodi)-1)
        #nodoCasuale2 = random.randint(0, int(numnodi)-1)

        #arco = Edge(edge_id=str(eid), from_node=str(nodoCasuale), from_orn=random.choice(['+', '-']),
         #           to_node=str(nodoCasuale2), to_orn=random.choice(['+', '-']), from_positions=(0, 0),
          #          to_positions=(0, 0), alignment="")
        #grafo.add_edge(arco)

    grafo.dump(1, out='a.txt')


def carica_grafo_da_file(nome_file):
    #start_time = time.time()

    g = grafo.from_file(nome_file)

    #end_time = time.time()
    #elapsed_time = end_time - start_time
    #print(f"Tempo di esecuzione: {elapsed_time} secondi")
    # Misura l'uso di memoria
    #memory_usage = psutil.Process().memory_info().rss / (1024.0 * 1024.0)  # in megabytes
    #11print(f"Consumo di memoria: {memory_usage} MB")
    return g

def test_funzioneConcat(grafo):
    # Esempio di logica per testare una funzione specifica
    nodi = ""
    overlaps=""
    for i in range(1,50):
            nodi = nodi + str(i) + "+,"
            overlaps=overlaps + "0M,"
            if i == int(49):
                nodi = nodi + str(i) + "+"
                overlaps=overlaps + "0M"
    grafo.from_string("P\t1\t" + nodi + "\t"+overlaps)
    start_time = time.time()

    print(grafo.concat_path_sequences('1'))

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo di esecuzione: {elapsed_time} secondi")
    # Misura l'uso di memoria
    memory_usage = psutil.Process().memory_info().rss / (1024.0 * 1024.0)  # in megabytes
    print(f"Consumo di memoria: {memory_usage} MB")

def test_funzioneMerge(grafo,nodo):
    # Esempio di logica per testare una funzione specifica
    start_time = time.time()

    grafo.remove_node_and_merge(mod=2 , nid=nodo)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo di esecuzione: {elapsed_time} secondi")
    # Misura l'uso di memoria
    memory_usage = psutil.Process().memory_info().rss / (1024.0 * 1024.0)  # in megabytes
    print(f"Consumo di memoria: {memory_usage} MB")
    print(grafo.neighbors('2'))

def test_path(grafo):
    numnodi=input("Quanti nodi nel path? ")
    nodi=""
    for i in range(1 , int(numnodi)+1):
        nodi=nodi+str(i)+"+,"
        if i==int(numnodi):
            nodi = nodi + str(i) + "+"

    start_time = time.time()

    grafo.from_string("P\t1\t"+nodi+"\t4M,7M,0M")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo di esecuzione: {elapsed_time} secondi")
    # Misura l'uso di memoria
    memory_usage = psutil.Process().memory_info().rss / (1024.0 * 1024.0)  # in megabytes
    print(f"Consumo di memoria: {memory_usage} MB")


# Main
costruisci_e_salva_grafo()
grafo = carica_grafo_da_file("a.txt")
test_funzioneMerge(grafo, nodo='2')
