class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __get_height(self, node):
        if node is None:
            return 0
        left_height = self.__get_height(node.left)
        right_height = self.__get_height(node.right)
        return 1 + max(left_height, right_height)

    def tree_balanced(self):
        left_height = self.__get_height(self.left)
        right_height = self.__get_height(self.right)

        if abs(left_height - right_height) > 1:
            return False

        left_balanced = self.left.tree_balanced() if self.left else True
        right_balanced = self.right.tree_balanced() if self.right else True

        return left_balanced and right_balanced

    @staticmethod
    def __read_file(filename):
        with open(filename, 'r') as f:
            return f.read().strip()

    @staticmethod
    def __deserialize(data):
        values = list(map(int, data.split()))
        
        def build(vals):
            if not vals:
                return None
            root_val = vals[-1]
            root = BinaryTree(root_val)
            split = len(vals) - 1
            for i, v in enumerate(vals[:-1]):
                if v > root_val:
                    split = i
                    break
            root.left  = build(vals[:split])
            root.right = build(vals[split:-1])
            return root
        
        return build(values)

    @classmethod
    def load_from_file(cls, filename):
        raw = cls.__read_file(filename)   
        return cls.__deserialize(raw)     

    def __get_lines(self, node):
            if node is None:
                return [], 0, 0

            val = str(node.value)
            vlen = len(val)

            if node.left is None and node.right is None:
                return [val], 0, vlen

            L_lines, L_start, L_w = self.__get_lines(node.left)  if node.left  else ([], -1, 0)
            R_lines, R_start, R_w = self.__get_lines(node.right) if node.right else ([], -1, 0)

            gap = 3

            if node.left and node.right:
                W = L_w + gap + R_w
                L_center = L_start + len(str(node.left.value)) // 2
                R_center = L_w + gap + R_start + len(str(node.right.value)) // 2
                slash  = L_center + 1
                bslash = R_center - 1
                root_center = (slash + bslash) // 2
                root_start  = root_center - vlen // 2
                root_line  = ' ' * root_start + val
                slash_line = ' ' * slash + '/' + ' ' * max(0, bslash - slash - 1) + '\\'
                body = []
                for i in range(max(len(L_lines), len(R_lines))):
                    l = (L_lines[i] if i < len(L_lines) else '').ljust(L_w)
                    r =  R_lines[i] if i < len(R_lines) else ''
                    body.append(l + ' ' * gap + r)
                return [root_line, slash_line] + body, root_start, W

            elif node.left:
                W = L_w
                L_center = L_start + len(str(node.left.value)) // 2
                slash = L_center + 1
                root_start = max(0, slash - vlen // 2)
                root_line  = ' ' * root_start + val
                slash_line = ' ' * slash + '/'
                return [root_line, slash_line] + L_lines, root_start, W

            else:
                W = R_w + gap
                R_center = gap + R_start + len(str(node.right.value)) // 2
                bslash = R_center - 1
                root_start = max(0, bslash - vlen // 2)
                root_line  = ' ' * root_start + val
                slash_line = ' ' * bslash + '\\'
                r_lines = [' ' * gap + r for r in R_lines]
                return [root_line, slash_line] + r_lines, root_start, W
    
    def print_tree(self):
        lines, _, _ = self.__get_lines(self)
        for line in lines:
            print(line)


if __name__ == "__main__":
    tree = BinaryTree.load_from_file("tree.txt")

    tree.print_tree()

    print("\nTree balanced?", tree.tree_balanced())

    
    



