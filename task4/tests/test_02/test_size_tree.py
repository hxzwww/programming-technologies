from tree_utils_02.size_tree import SizeTree
from tree_utils_02.size_node import FileSizeNode
from tree_utils_02.tree import Tree
from os import mkdir


def test_size_tree():
    size_tree = SizeTree()
    tree = Tree()

    #CHECKING construct_filenode
    #when given a directory set size to BLOCKSIZE=4096

    dir_path = "../test_size"

    mkdir(dir_path)

    file_size_node = size_tree.construct_filenode(dir_path, True)
    ans = FileSizeNode("test_size", True, [], 4096)

    assert file_size_node == ans

    #when given a file set size to file size

    file_path = open("../test_size/main.cpp", "w")
    file_path.write("""#include <iostream>

    void hello() {
        std::cout << "Hello" << std::endl;
    }
    """)
    file_path.flush()
 
    file_size_node = size_tree.construct_filenode("../test_size/main.cpp", False)
    ans = FileSizeNode("main.cpp", False, [], 93)

    assert file_size_node == ans
    
    #CHECKING update_filenode

    file = open("../test_size/main.h", "w")
    file.write("""void hello();
    """)
    file.flush()

    file_size_node = FileSizeNode("test_size", True, [FileSizeNode("main.cpp", False, [], 93), FileSizeNode("lib.h", False, [], 15)], 0)
    ans = file_size_node
    ans.size = 108
    
    file_size_node = size_tree.update_filenode(file_size_node)

    assert ans == file_size_node
