from my_funcs.workers import read_from_file

def create_testdata(test_data):
    with open("testfile.txt", "a") as f_o:
        f_o.writelines(test_data)

def test_read_from_file1():
    test_data = ['one\n', 'two\n', 'three']
    create_testdata(test_data)
    assert test_data == read_from_file("testfile.txt")


def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three']
    create_testdata(test_data)
    assert test_data == read_from_file("testfile.txt")
