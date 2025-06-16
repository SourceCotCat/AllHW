
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.out_ind = 0
        self.in_ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.out_ind < len(self.list_of_list):
            lst = self.list_of_list[self.out_ind]
            if self.in_ind < len(lst):
                item = lst[self.in_ind]
                self.in_ind += 1
                return item
            else:
                self.out_ind += 1
                self.in_ind = 0
                
        raise StopIteration
    
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # print(list(FlatIterator(list_of_lists_1)))

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()