class FlatIterator:
# класс для решения задачи №4
    def __init__(self, list_of_list):
        self.input_list = list_of_list

    def __iter__(self):
        self.cur_iter = iter(self.input_list)
        self.iter_list = []
        return self

    def __next__(self):
        '''проходим по input_list и создаем список итераторов для каждого вложенного листа, выдачу элемента
        выполняем для самого последнего итератора в списке, после его опустошения переходим к предпоследнему  '''
        while True:
            try:
                item = next(self.cur_iter)
                if isinstance(item, list):
                    # текущий итератор добавляем в список, создаем новый итератор и делаем его текущим
                    self.iter_list.append(self.cur_iter)
                    self.cur_iter = iter(item)
                else:
                    return item
            except StopIteration:
                if not self.iter_list:
                    raise StopIteration
                else:
                    # переходим к последнему итератору в списке, причем его удаляем из списка
                    self.cur_iter = self.iter_list.pop()

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

# для проверки кода
list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

# вспомогательная функция для проверки правильности решения задачи №3
def check_flat_list_from_task_3(lst):
    for el in FlatIterator(lst):
        print(el, end=' ')

if __name__ == '__main__':
    test_3()

    check_flat_list_from_task_3(list_of_lists_2)
