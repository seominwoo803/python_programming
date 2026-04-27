
fir_li = set(input("첫 번째 리스트 요소 입력 :").split(","))
sen_li = set(input("두 번째 리스트 요소 입력 :").split(","))

print("교집합 :", fir_li & sen_li)
print("합집합 :", fir_li | sen_li)

print("fir_li - sen_li 차집합 :", fir_li - sen_li)
print("sen_li - fir_li 차집합 :", sen_li - fir_li)
