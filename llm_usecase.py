#Create pallindrome
def create_pallindrome(d):
    left_st="" #qqrrt
    right_st = "" #qqrr

    print(d)
    if 'a' in d:
        if d['a']%2==0:
            for i in range((d['a']//2)):
                left_st += 'a'
            for i in range((d['a']//2)):
                right_st += 'a'
        else:
            for i in range(d['a']):
                left_st += 'a'
        d.pop('a')
    for key in d:
        if d[key]%2==0:
            for i in range((d[key]//2)):
                left_st += key
            for i in range((d[key]//2)):
                right_st += key
        else:
            for i in range(d[key]):
                left_st += key
    return left_st+right_st[::-1]


#calc for even ln string
def even_len(d):
    for key in d:
        if key!="?":
            if d[key]%2!=0:
                if d['?']==0:
                    return -1
                d[key]+=1
                d['?']-=1
    #Except ?'s the string can be made pallind
    if d['?']:
        if 'a' in d:
            d['a'] += d['?']
        else:
            d['a'] = d['?']
    d.pop('?')
    return create_pallindrome(d)

def odd_len(d):
    odd_occur_elem = []
    for key in d:
        if key != "?":
            if d[key] % 2 != 0:
                odd_occur_elem.append(key)
    for i in range(len(odd_occur_elem)-1):
        if d['?']:
            d[odd_occur_elem[i]]+=1
            d['?'] -= 1
        else:
            return -1
    if d['?']:
        if 'a' in d:
            d['a']+=d['?']
        else:
            d['a']=d['?']
    d.pop('?')
    for key in d:
        if d[key]%2!=0:
            odd=key
            break
    d[odd]=d.pop(odd)
    return create_pallindrome(d)


s = "?yrt"
sorted_s = sorted(s)
print(sorted_s)
d = {}

#Count occurrences as per lexographical order
for i in sorted_s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

if len(sorted_s)%2==0:
    print(even_len(d))
else:
    print(odd_len(d))

'''

String len is fix

(Even)
1) Make minimum pallindrome
2) Changes remaining ?'s (if exist) to a's

(ODD)

any one elem will occur odd no. of times

aarrrr??? -> 1) {a:2,r:4,?:3} -> a's (all evens)
             2) {a:2,m:4,r:3,?:2} -> a's (Only one odd occ)
             3) {a:2,m:4,r:4,t:3,?:2} (Convert to only once occur of odd elem)->
             (Keep highest lexi as odd only)
             4) {m:3,r:3,t:5,?:4}
             
             [m,r,t]
'''