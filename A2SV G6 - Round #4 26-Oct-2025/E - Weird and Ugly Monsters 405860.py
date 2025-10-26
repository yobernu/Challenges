# Problem: E - Weird and Ugly Monsters - https://codeforces.com/gym/590053/problem/E

class ListNode:
    def __init__(self, index, ugliness):
        self.index = index
        self.ugliness = ugliness
        self.next = None
        self.prev = None


def merge_monsters(node, monster_map, count):
    while True:
        merged = False
        if node.prev != node and node.ugliness == node.prev.ugliness:
            left = node.prev
            if node.index > left.index:
                left.next = node.next
                node.next.prev = left
                left.ugliness *= 2
                count[0] -= 1
                node = left
            else:
                node.prev = left.prev
                left.prev.next = node
                node.ugliness *= 2
                count[0] -= 1
            merged = True

        elif node.next != node and node.ugliness == node.next.ugliness:
            right = node.next
            if node.index > right.index:
                node.prev.next = right
                right.prev = node.prev
                right.ugliness *= 2
                count[0] -= 1  
                node = right  
            else:
                right.next.prev = node
                node.next = right.next
                node.ugliness *= 2
                count[0] -= 1
            merged = True
        if not merged:
            break


def solve():
    num_insertions, initial_ugliness = map(int, input().split())
    count = [1]

    head = ListNode(1, initial_ugliness)
    head.next = head 
    head.prev = head
    monster_map = {1: head}

    indices = list(map(int, input().split()))
    ugliness_values = list(map(int, input().split()))
    next_index = 2 
    results = []

    for i in range(num_insertions):
        monster_index, ugliness_score = indices[i], ugliness_values[i]
        monster = monster_map[monster_index]
        new_monster = ListNode(next_index, ugliness_score)
        next_index += 1
        
        new_monster.next = monster.next
        new_monster.prev = monster
        monster.next.prev = new_monster
        monster.next = new_monster

        monster_map[new_monster.index] = new_monster  
        count[0] += 1 
        merge_monsters(new_monster, monster_map, count)
        results.append(count[0])

    print(*results)


t = int(input())
for _ in range(t):
    solve()