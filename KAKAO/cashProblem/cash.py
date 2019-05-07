def solution(cacheSize, cities):
    answer = 0
    queue = []
    for city in cities:
        before_num = len(queue)
        queue.append(city.upper())
        after_num = len(set(queue))
        if before_num == after_num:
            queue.pop(queue.index(city.upper()))
            answer += 1
        else:
            answer += 5
        if len(queue) == cacheSize+1:
            queue.pop(0)
    return answer
