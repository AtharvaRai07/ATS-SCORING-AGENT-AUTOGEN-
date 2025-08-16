from autogen_core.memory import MemoryContent,MemoryMimeType
from autogen_ext.memory.mem0 import Mem0Memory

class MemoryTool:
    def get_memory(self):
        mem0_memory = Mem0Memory(
        is_cloud=True,
        api_key = "m0-QXXhimSTpF0BvB3Gf3COiZIG85WknDgFbrkQDBWd",
        limit=10,
        user_id="ats_id"
)
        return mem0_memory