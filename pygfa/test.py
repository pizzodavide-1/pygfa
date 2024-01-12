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



############################################
#TEST CREO GRAFO CON 1000 NODI 2000 GRAFI E CI OPERO SOPRA
"""""
test2_graph=GFA()
nucleotidi = "ACGT"

randomEid=random.randint(0,999999)
for nid in range(1000000):
    lungh = random.randint(4, 10)
    seq=''.join(random.choice(nucleotidi) for _ in range(lungh))
    nodo=Node(node_id=str(nid), sequence=seq, length=len(seq))
    #print(nodo.sequence)
    test2_graph.add_node(nodo)

#nodes=test2_graph.nodes()
#print (nodes)

for eid in range(2000000):
    nodoCasuale=random.randint(0,999999)
    nodoCasuale2=random.randint(0,999999)

    arco=Edge(edge_id=str(eid), from_node=str(nodoCasuale), from_orn=random.choice(['+','-']) , to_node=str(nodoCasuale2), to_orn=random.choice(['+','-']),from_positions=(0,0) , to_positions=(0,0) ,alignment="")
    test2_graph.add_edge(arco)
    #if arco.from_node== str(randomEid) or arco.to_node==str(randomEid): #stampo idnodi collegati al id casuale per controllo
     #   print(arco)

edges=test2_graph.edges()
print("TOP") #stampo archi

vicini=test2_graph.neighbors(str(randomEid)) #stampo i vicini di un nodo casuale
print("I vicini del nodo con edi=" + str(randomEid) + "sono:")
print(vicini)

################################################################
#NODO DA LINEA
#nome=input("Inserire id Segmento:")
#sequenza=input("Inserire Sequenza nucleotidica: ")
#campoSequenza=Field(name="sequence", value=sequenza)
#campoNome=Field(name="name", value=nome)
#segment=SegmentV1()
#segment.add_field(campoNome)
#segment.add_field(campoSequenza)
#print(segment)
#n1=Node.from_line(segment)
#test2_graph.add_node(n1)
#print("Aggiunto al grafo il nodo :")
#print(n1)
#######AGGIUNGERE NODO DA STRINGA
n1=test2_graph.from_string("S	11	ACCTT") #aggiunto
n2=test2_graph.from_string("S	12	TCAAGG")
n3=test2_graph.from_string("S	13	CTTGATT")
n4=test2_graph.from_string("S	14	GAAC")
n5=test2_graph.from_string("S	15	ATT")
n6=test2_graph.from_string("S	16	AAAAA")
test2_graph.from_string("L	11	+	12	-	4M") #LINK FROM STRING

#print(test2_graph.get("11")) #stampo
#print(test2_graph.as_graph_element("S11"))
###CONTROLLO CON SAFE=TRUE
#nprova=Node(node_id="S11",sequence="AGTA",length=4)
#test2_graph.add_node(nprova,safe=True) #SOLLEVA ECCEZIONE: ELEMENTO CON STESSO ID GIA PRESENTE
#################LINK###################MANUALMENTE
link=Link()##LINK FROM L-LINE
fieldFrom=Field(name='from' , value='12')
fieldFromOrientation=Field(name='from_orn', value='-')
fieldTo=Field(name='to', value='13')
fieldToOr=Field(name='to_orn', value='+')
fieldOverlap=Field(name='overlap', value='5M')
link.add_field(fieldFrom)
link.add_field(fieldFromOrientation)
link.add_field(fieldTo)
link.add_field(fieldToOr)
link.add_field(fieldOverlap)
e2=Edge.from_line(link)
test2_graph.add_edge(e2)
test2_graph.from_string("L	11	+	13	+	3M")
########################################
###CONTAINMENT####
test2_graph.from_string("C	1	-	6	+	110	100M")#######################
optfield=OptField(name='ID', value='2', field_type='A')
fieldFromC=Field(name='from', value='5')
fieldFromOrientationC=Field(name='from_orn', value='-')
fieldToC=Field(name='to', value='6')
fieldToOrC=Field(name='to_orn', value='+')
fieldPos=Field(name='pos', value='110')
fieldOverlapC=Field(name='overlap', value='100M')
cont=Containment()
cont.add_field(optfield) #OPTIONAL FIELD id(EID)
cont.add_field(fieldFromC)
cont.add_field(fieldFromOrientationC)
cont.add_field(fieldToC)
cont.add_field(fieldToOrC)
cont.add_field(fieldPos)
cont.add_field(fieldOverlapC)
e4=Edge.from_line(cont)
test2_graph.add_edge(e4)
e3=test2_graph.get('virtual_3') #returna il dizionario con gli attributi dell arco con quella key
#e3['eid']='Virtual_33' #modifica della chiave
print(e3)
##################
edges=test2_graph.edges()
nodi=nodes=test2_graph.nodes()
archi=test2_graph.edges()
print(nodi)

###########################################################ààà
#####PATH#####
path=Path()
fieldNamePath=Field(name='path_name', value='15')
fieldSegmentNames=Field(name='seqs_names', value='11+,12-,13+')
fieldOverlaps=Field(name='overlaps', value='4M,5M')
path.add_field(fieldNamePath)
path.add_field(fieldSegmentNames)
path.add_field(fieldOverlaps)
sottogr=Subgraph(graph_id='15' , elements={'seqs_name':'	11+,12-,13+','overlaps':'	4M,5M'})#sottografo ma non cammino
#test2_graph.add_subgraph(sottogr)
#HO CREATO UN SOTTOGRAFO PASSANDOGLI UN CAMMINO
test2_graph.from_string("P	10	11+,12-,13+	4M,5M")
test2_graph.from_string("P	17	11-,12-,15+	4M,2M")
#test2_graph.from_string("P	18	14-,16+	3M")
#sottogr18=test2_graph.subgraphs('18')
#gr18=test2_graph.get_subgraph('18')
#print(gr18.nodes())
#print(gr18.edges())
test2_graph.from_string("L	14	-	16	+	3M")
#subgfa=test2_graph.get_subgraph('18') #RESTITUISCE IL GFA EQUIVALENTE AL SOTTOGRFAFO FORMATO COL CAMMINO(Un gfa indipendente dal resto)
#ss=test2_graph.subgraphs('15')
#print(ss)
#sottogr=test2_graph.subgraph(('12', '13','6')) #dati un bunch di nodi ci dice un sottografo di tot nodi e archi
#print(sottogr)
###########################################################
#print(test2_graph.concat_path_sequences('18'))
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
"""""
grafo2=GFA()
grafo2.from_string("S	1	ACCTT")
grafo2.from_string("S	2	GGATT")
grafo2.from_string("S	3	CCCCC")
grafo2.from_string("S	4	ACCTT")
grafo2.from_string("S	5	GGATT")
grafo2.from_string("S	6	CCCCC")

grafo2.from_string("L	1	+	2	-	0M")
grafo2.from_string("L	2	+	3	-	0M")
grafo2.from_string("L	4	+	2	-	0M")
grafo2.from_string("L	2	+	5	-	0M")
grafo2.from_string("L	3	+	6	-	0M")
grafo2.from_string("L	6	+	2	-	0M")
grafo2.from_string("L	3	+	5	-	0M")
grafo2.from_string("L	5	+	6	-	0M")
grafo2.from_string("L	3	+	4	-	0M")

#grafo2.add_subgraph("P	10	1+,2-,3-,6-	3M,5M,0M,1M")
grafo2.from_string("P	10	1+,2-,3-	3M,5M,0M,1M")
grafo2.from_string("P	11	1+,2-,4+	4M,2M,1M,0M")
grafo2.from_string("P	12	2+,1-	3M,5M,0M,1M")
grafo2.from_string("P	13	4+,5-,6-	4M,2M,1M,0M")

#print(grafo2.get('10'))
#print(grafo2.dump(1))

#TEST REMOVENODEANDMERGE

#print("Nodi:")
#print(grafo2.nodes())
#print("Archi:")
#print(grafo2.edges())

grafo2.remove_node_and_merge('2',1)

#print("Nodi:")
#print(grafo2.nodes())
#print("Archi:")
#print(grafo2.edges())


#print(grafo2.paths())
#grafo2.remove_node_and_merge('2',1)
#print(grafo2.paths())
#print(grafo2.get_paths_with_id())


#print(grafo2.concat_path_sequences('10'))
################################################################################
g3=GFA()

g3.from_string("S	1	ACCTT")
g3.from_string("S	2	GGATT")
g3.from_string("S	3	CCCCC")
g3.from_string("S	4	ACCTT")
g3.from_string("S	5	GGATT")
g3.from_string("S	6	CCCCC")
g3.from_string("S	7	GGATT")
g3.from_string("S	8	CCCCC")
g3.from_string("S	9	GGATT")
g3.from_string("S	10	CCCCC")
g3.from_string("S	11	CCCCC")
g3.from_string("S	12	GGATT")
g3.from_string("S	13	CCCCC")

g3.from_string("L	1	+	2	-	0M")
g3.from_string("L	2	+	3	-	0M")
g3.from_string("L	4	+	2	-	0M")
g3.from_string("L	2	+	5	-	0M")
g3.from_string("L	3	+	6	-	0M")
g3.from_string("L	1	+	7	-	0M")
g3.from_string("L	7	+	8	-	0M")
g3.from_string("L	3	+	7	-	0M")
g3.from_string("L	4	+	9	-	0M")
g3.from_string("L	3	+	10	-	0M")
g3.from_string("L	10	+	11	-	0M")
g3.from_string("L	11	+	12	-	0M")
g3.from_string("L	12	+	13	-	0M")

print(g3.neighbors('2'))
#print(g3.extract_Subgraph_from_neighborhood(nid='2', len=3).nodes())
#print(g3.extract_Subgraph_from_neighborhood(nid='2', len=3).edges())

sg=g3.extract_Subgraph_from_neighborhood(nid='2', len=0,)
print(sg.nodes())
print(sg.edges()) #QUESITO: E' POSSIBILE FAR SI CHE LA FUNZIONE CREI UN SOTTOGRAFO PARTENDO DA QUESTO GFA?
#print(sg)



