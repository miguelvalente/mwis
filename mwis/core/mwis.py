from __future__ import annotations


def post_order_traversal(root):
    """
    Perform post-order traversal of the tree rooted at root.
    """
    if root is None:
        return

    for child in root.children:
        yield from post_order_traversal(child)

    yield root


def mwis(root, force_keep_root=False):
    """
    Maximum weight independent set for a tree.
    input: root node of the tree
    output: tuple containing the maximum weight and the set of nodes in the MWIS
    """
    for node in post_order_traversal(root):
        if node.is_leaf:
            node.mwis_exclude = (0, set())
            node.mwis_include = (node.party_score, set([node]))
        else:
            if force_keep_root and node.is_root:
                node.mwis_exclude = (float("-inf"), set())
            else:
                excluded_weight, exclude_nodes = zip(
                    *[mwis(child, force_keep_root) for child in node.children]
                )
                node.mwis_exclude = (sum(excluded_weight), set().union(*exclude_nodes))

            grandchildren = [
                mwis(grandchild, force_keep_root)
                for child in node.children
                for grandchild in child.children
            ]

            if grandchildren:
                include_weight, include_nodes = zip(*grandchildren)
                include_weight = node.party_score + sum(include_weight)
                include_nodes = set([node]).union(*include_nodes)
            else:
                include_weight = node.party_score
                include_nodes = set([node])

            node.mwis_include = (include_weight, include_nodes)

    if root.mwis_include[0] > root.mwis_exclude[0]:
        return root.mwis_include
    else:
        return root.mwis_exclude
