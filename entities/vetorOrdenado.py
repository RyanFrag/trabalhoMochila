def compare_default(item1, item2):
    if item1 == item2:
        return 0
    
    return 1 if item1 > item2 else -1

class OrderedVectorException(Exception):
    pass

class OrderedVector:

    def __init__(self, max_elements: int, compare = compare_default) -> None:
        if max_elements < 0:
            raise OrderedVectorException(
                "Minimum value of elements in invalid OrderedVector"
            )

        self.__elements = list([None] * max_elements)
        self.__max_elements = max_elements
        self.__index_last_element = -1
        self.__compare = compare

    def insert(self, new_value: int) -> None:
        new_index_last_element = self.__index_last_element + 1

        if new_index_last_element == self.__max_elements:
            raise OrderedVectorException("Maximum elements in OrderedVector")

        index_first_more = self.__find_first_more(new_value)
        if index_first_more == -1 or index_first_more == new_index_last_element:
            self.__elements[new_index_last_element] = new_value
            self.__index_last_element = new_index_last_element
            return

        
        for index in range(new_index_last_element, index_first_more, -1):
            self.__elements[index] = self.__elements[index - 1]

        self.__elements[index_first_more] = new_value
        self.__index_last_element = new_index_last_element
        
    def __find_first_more(self, value: int):
        if self.__index_last_element == -1:
            return -1

        for index in range(self.__index_last_element + 1):
            if self.__compare(value, self.__elements[index]) == -1:
                return index
    
        return self.__index_last_element + 1
        

    def get(self, index_item):
        if index_item < 0 or index_item > self.__index_last_element:
            return None
        
        return self.__elements[index_item]



    def pop(self, index_item_remove: int):
        if index_item_remove < 0 or index_item_remove > self.__index_last_element:
            return None
        
        element = self.__elements[index_item_remove]
        for index in range(index_item_remove, self.__index_last_element):
            self.__elements[index] = self.__elements[index + 1]

        self.__elements[self.__index_last_element] = None
        self.__index_last_element -= 1

        return element
    
    def __len__(self):
        return self.__index_last_element + 1
    
    def __iter__(self):
        for data in self.__elements:
            if data is None:
                continue
            
            yield data

