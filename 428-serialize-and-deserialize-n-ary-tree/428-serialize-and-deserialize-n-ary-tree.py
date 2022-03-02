"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> dict:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
        if root:
            tree = {
                "value": root.val,
                "children": [self.serialize(child) for child in root.children]
            }
        else:
            tree = {}
        return tree
        
	
    def deserialize(self, data: dict) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        if data:
            node = Node(data["value"], [self.deserialize(child) for child in data["children"]])
        else:
            node = None
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))