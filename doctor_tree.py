class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        side = side.lower()
        if side not in ("left", "right"):
            print(f"'{side}' is not a valid side. Choose left or right.")
            return

        if current_node is None:
            current_node = self.root
        if current_node is None:
            print("The tree has no root yet.")
            return

        # Find the parent by searching the whole tree, then insert once.
        parent = self._find(current_node, parent_name)
        if parent is None:
            print(f"Parent '{parent_name}' not found in the tree.")
            return

        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(doctor_name)
            else:
                print(f"{parent_name} already has a doctor on the left.")
        else:
            if parent.right is None:
                parent.right = DoctorNode(doctor_name)
            else:
                print(f"{parent_name} already has a doctor on the right.")

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find(node.left, name)
        if found is not None:
            return found
        return self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        if node is None:
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)
        return result

    def postorder(self, node):
        if node is None:
            return []
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)
        return result


# Tests
tree = DoctorTree()
tree.insert("Dr. Croft", "Dr. Phan", "left")  # edge case: no root yet
tree.root = DoctorNode("Dr. Croft")
tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))

tree.insert("Dr. Nobody", "Dr. Ghost", "left")   # edge case: missing parent
tree.insert("Dr. Croft", "Dr. Extra", "left")    # edge case: side taken
tree.insert("Dr. Croft", "Dr. Extra", "middle")  # edge case: invalid side
print(DoctorTree().preorder(None))               # edge case: empty tree