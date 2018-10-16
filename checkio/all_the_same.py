from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:

    for i in elements:
        if elements[0] != i:
            return False
    return True
    

if __name__ == '__main__':
    # print("Example:")
    # print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    print("---")
    assert all_the_same([1, 2, 1]) == False
    print("---")
    assert all_the_same(['a', 'a', 'a']) == True
    print("---")        
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")