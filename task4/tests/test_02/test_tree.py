from tree_utils_02.tree import Tree
from tree_utils_02.node import FileNode
from os.path import exists, basename
from os import mkdir


def test_tree():
    tree = Tree()

    #CHECKING construct_filenode

    path = "../test"
    mkdir(path)

    file_node = tree.construct_filenode(path, True)

    assert file_node == FileNode("test", True, [])

    #CHECKING update_filenode

    path = "../test/progs"
    mkdir(path)

    new_file_node = tree.construct_filenode(path, False)

    file_node = tree.update_filenode(new_file_node)

    assert file_node == new_file_node

    #CHECKING get
    #when a non existed path is given AttributeError should be raised

    non_existed_path = "../non_existence"

    try:
        file_node = tree.get(non_existed_path, True)
    except AttributeError:
        assert True
    except Exception:
        assert False

    #when a file path is given with dirs_only=True and recurse_call=False AttributeError should be raised

    file_path = "../test/main.cpp"
    file = open(file_path, "w")

    try:
        file_node = tree.get(file_path, True)
    except AttributeError:
        assert True
    except Exception:
        assert False

    #when a file path is given with dirs_only=True and recurse_call=True None should be returned

    file_node = tree.get(file_path, True, True)

    assert file_node == None

    #when a file path is given with dirs_only=False and recurese_call=False
    #construct_filenode(file_path, False) should be called and returned

    file_node = tree.get(file_path, False)

    assert file_node == tree.construct_filenode(file_path, False)

    #given a directory path ../test
    # test
    # |_main.cpp
    # |_progs
    # |_lib
    # | |_sublib
    # a FileNode with name=test and children lib and progs, where lib has a child sublib should be returned

    dir_path = "../test"
    mkdir("../test/lib")
    mkdir("../test/lib/sublib")

    file_node = tree.get(dir_path, True)

    child = FileNode("sublib", True, [])
    ans = FileNode("test", True, [FileNode("lib", True, [child]), FileNode("progs", True, [])])

    assert file_node == ans

    #CHECKING filter_empty_node

    #when a directory is not passed nothing should be changed

    file_node = FileNode("cpp", False, [])

    assert tree.filter_empty_nodes(file_node) == None 
    
    #when given an empty directory delete it

    path = "../test1"
    mkdir(path)

    file_node = FileNode("test1", True, [])
    tree.filter_empty_nodes(file_node, path)

    assert not exists(path)

    #when given a directory with empty subdirectories delete them

    path = "../test"

    file_node = tree.get(path, True)
    tree.filter_empty_nodes(file_node, path)

    new_file_node = tree.get(path, True)
    ans = FileNode("test", True, [FileNode("lib", True, [])])
