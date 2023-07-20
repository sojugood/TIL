'''
보유 중인 도서 리스트 list_of_book과 대여 예정 도서 리스트 rental_list가 주어진다.

반복문을 사용하여 rental_list 요소 중, 보유 중인 도서에 포함되지 않은 요소를 발견하면 {도서 명} 은/는 보유하고 있지 않습니다. 문구를 출력한다.

보유하고 있지 않은 문서가 있다면, 위 문구를 출력한 후, 반복문을 종료한다.

만약 모든 도서를 보유하고 있다면 모든 도서가 대여 가능한 상태입니다. 를 출력한다.
'''
list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

all_have = set()

for i in rental_book:
    if i in list_of_book:
        all_have.add("yes")
    else:
        all_have.add("no")
        print(f"{i} 은/는 보유하고 있지 않습니다.")
        break
if len(all_have) == 1:
    print("모든 도서가 대여 가능한 상태입니다.")