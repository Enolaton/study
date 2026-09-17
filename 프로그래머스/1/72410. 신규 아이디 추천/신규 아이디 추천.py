


def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    id_list = []
    for c in new_id:
        if c.islower() or c.isnumeric():
            id_list.append(c)
        elif c in ['-','_','.']:
            id_list.append(c)
    # 3단계
    for i in range(len(id_list)-1):
        if id_list[i] == '.' and id_list[i+1] == '.':
            id_list[i] = ''
    new_id = ''.join(id_list)
    # 4단계
    id_list = list(new_id)
    if id_list[0] == '.':
        id_list[0] = ''
    elif id_list[len(id_list)-1] == '.':
        id_list[len(id_list)-1] = ''
    new_id = ''.join(id_list)
    # 5단계
    if len(new_id)==0:
        new_id = 'a'
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[len(new_id)-1] == '.':
        new_id = new_id[:len(new_id)-1]
    # 7단계
    if len(new_id) < 3:
        for i in range(3-len(new_id)):
            new_id += new_id[-1]
    return new_id