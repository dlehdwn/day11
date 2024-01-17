#comprehension
#for 문의 심화라고 읽고 단축 버전

#[i for i in range(10)] # 0~9
#[for i in "snow"] #'s','n','o','w'

#필터링
#[i for i in range(10) if i %2 ==0]
#f = ['apple', 'banana']
#[i for i in f if i.count('b') >0 or 'b' in i]

#맵핑[변환/치환]
#for 앞에다 쓰는것

#dict
#coffee = ['아메리카노','라떼','바닐라']
#price = [2000,3000,2500]
#zip
#리스트 안에 dict
#[{'커피':x,'가격':y} for x,y in zip(coffee,price)]
#dict 안에 dict
#{{i:{'커피':x,'가격':y} for i,(x,y) in enumerate(zip(coffee,price))}