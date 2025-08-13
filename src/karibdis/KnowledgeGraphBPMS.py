
from karibdis.ProcessKnowledgeGraph import ProcessKnowledgeGraph

class KnowledgeGraphBPMS:

    def __init__(self, pkg=None):
        self.pkg = pkg | ProcessKnowledgeGraph()

    def handle_event(self, event):
        pass