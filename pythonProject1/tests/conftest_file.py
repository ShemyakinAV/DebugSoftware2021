import pytest

count = 0
@pytest.fixture(autouse=True)
def clean_text():
    global count
    with open("testfile.txt", "w"):
        pass
    print(count)
    count+=1