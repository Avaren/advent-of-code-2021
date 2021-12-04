import collections
import itertools


def part_1(sonar_depth):
    return sum(
        [depth_n1 > depth_n for depth_n, depth_n1 in itertools.pairwise(sonar_depth)]
    )


def part_2(sonar_depth):
    def slice(sonar_depth):
        sonar_depth = iter(sonar_depth)
        chunk = collections.deque(itertools.islice(sonar_depth, 3), maxlen=3)
        yield tuple(chunk)
        for sd in sonar_depth:
            chunk.append(sd)
            yield tuple(chunk)

    return sum(
        depth_chunk_n1 > depth_chunk_n
        for depth_chunk_n, depth_chunk_n1 in itertools.pairwise(
            sum(chunk) for chunk in slice(sonar_depth)
        )
    )
