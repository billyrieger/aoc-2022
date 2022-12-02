if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        groups = f.read().split('\n\n')
        sum_group = lambda group: sum(map(int, group.strip().split()))
        sums = sorted(list(map(sum_group, groups)))
        print('part 1:', sums[-1])
        print('part 2:', sum(sums[-3:]))
