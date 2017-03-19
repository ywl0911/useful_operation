# -*- coding: utf-8 -*-
from collections import defaultdict

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]
result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)
print(result)
# Result:


# OrderedDict
# -*- coding: utf-8 -*-
from collections import OrderedDict

items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)
regular_dict = dict(items)
ordered_dict = OrderedDict(items)
print('Regular Dict:')
for k, v in regular_dict.items():
    print(k, v)
print('Ordered Dict:')
for k, v in ordered_dict.items():
    print(k, v)

# Counter
from collections import Counter

s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()
c = Counter(s)
# 获取出现频率最高的5个字符
print(c.most_common(5))
