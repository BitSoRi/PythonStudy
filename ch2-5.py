```
q_1 = {'name':'홍길동', 'birth':1128, 'age':30}

q_2 = dict()
q_2['name'] = 'python'
q_2[('a', )] = 'python'
q_2[250] = 'python'
#list is invalid key

q_3 = {'A':90, 'B':80, 'C':70}
q_3.pop('B')

q_4 = {'A':90, 'B':80}
a_4 = q_4.get('C', 70)

q_5 = {'A':90, 'B':80, 'C':70}
a_5 = min(q_5.values())

q_6 = {'A':90, 'B':80, 'C':70}
a_6 = list(q_6.items())
```
