import time
import pytest
import multiprocessing

class Child(multiprocessing.Process):

    def run(self):

        for i in range(15):
            time.sleep(1)
            print('Child iteration #', i)


@pytest.fixture
def process_setup():
    print('INSIDE setup()')
    p = Child()
    p.start()
    yield p
    print('INSIDE teardown()')
    p.terminate()


def test_process(process_setup):

    child = process_setup
    print(child)

    for i in range(10):
        time.sleep(1)
        print('Parent iteration #', i)
