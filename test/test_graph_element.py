import sys
sys.path.insert(0, '../pygfa')

from graph_element import node, edge as graph_edge
from parser.lines import header, segment, link, path, containment, fragment, edge, gap, group

import unittest

class TestGraphElement (unittest.TestCase):

    def test_node (self):
        nod = node.Node ("15", "acgt", 4)
        with self.assertRaises (node.InvalidNodeError):
            nod = node.Node ("*", "3", "aCGT")
        
    
    def test_node_from_segment (self):
        seg = segment.SegmentV1.from_string ("S\t3\tTGCAACGTATAGACTTGTCAC\tRC:i:4")
        nod = node.Node.from_line (seg)
        self.assertTrue (nod.nid == seg.fields['name'].value)
        self.assertTrue (nod.slen == None)
        self.assertTrue (nod.sequence == seg.fields['sequence'].value)
        
        seg = segment.SegmentV2.from_string ("S\t3\t21\tTGCAACGTATAGACTTGTCAC\tRC:i:4")
        nod = node.Node.from_line (seg)

        self.assertTrue (nod.nid == seg.fields['sid'].value)
        self.assertTrue (nod.slen == seg.fields['slen'].value)
        self.assertTrue (nod.sequence == seg.fields['sequence'].value)

        
    def test_edge_from_fragment (self):
        line = fragment.Fragment.from_string ("F\t12\t2-\t0\t140$\t0\t140\t11M")
        ed = graph_edge.Edge.from_line (line)

        self.assertTrue (ed.eid == None)
        self.assertTrue (ed.from_node == line.fields['sid'].value)
        self.assertTrue (ed.to_node == line.fields['external'].value)
        self.assertTrue (ed.from_positions == (line.fields['sbeg'].value, line.fields['send'].value))
        self.assertTrue (ed.to_positions == (line.fields['fbeg'].value, line.fields['fend'].value))
        self.assertTrue (ed.alignment == line.fields['alignment'].value)


    def test_edge_from_edge (self):
        line = edge.Edge.from_string ("E\t*\t23-\t16+\t0\t11\t0\t11\t11M")
        ed = graph_edge.Edge.from_line (line)

        self.assertTrue (ed.eid == line.fields['eid'].value)
        self.assertTrue (ed.from_node == line.fields['sid1'].value)
        self.assertTrue (ed.to_node == line.fields['sid2'].value)
        self.assertTrue (ed.from_positions == (line.fields['beg1'].value, line.fields['end1'].value))
        self.assertTrue (ed.to_positions == (line.fields['beg2'].value, line.fields['end2'].value))
        self.assertTrue (ed.alignment == line.fields['alignment'].value)

    def test_edge_from_gap (self):
        line = gap.Gap.from_string ("G\tg\tA+\tB-\t1000\t*")
        ed = graph_edge.Edge.from_line (line)

        self.assertTrue (ed.eid == line.fields['gid'].value)
        self.assertTrue (ed.from_node == line.fields['sid1'].value)
        self.assertTrue (ed.to_node == line.fields['sid2'].value)


        
if  __name__ == '__main__':
    unittest.main()
    
