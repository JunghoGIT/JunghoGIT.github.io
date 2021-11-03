---
title:  "Matplotlib 1"
excerpt: "axes와 figure 객체, 선 그래프 그리기"
categories:
 - Matplotlib
tags:
 - [python,matplotlib,study,TIL,data]
last_modified_at: 2021-11-03
toc: true
toc_sticky: true
---

# Matplotlib

<br>
<br>

**matplotlib**  은 파이썬에서 데이터 `차트`나 `플롯`으로 시각화 할 수 있게 도와주는 라이브러리이다.<br>
플롯은 일반적으로 둘 이상의 변수 간의 관계를 나타내는 그래프로 데이터 세트를 나타내는 그래픽 기술이다.

<br>

## 선 그래프 그리기

<br>

우선 python에서 첫번째로 matplotlib을 포함한 필요한 라이브러리들을 import 해준 후 데이터를 가져 오는 과정이 필요하다.<br>
본문에서는 간단하게 리스트와 배열 형식으로 데이터를 설정후에 진행하겠다.
<br>


```python
import matplotlib.pyplot as plt
import numpy as np

data = [1,2,3,4,5,6,7]
data2 = np.arange(100,800,100)

```

X축과 Y축에 해당하는 데이터를 설정했다.<br>
두번째 데이터는 추후에 plot을 하나 더 만들 때 값을 다르게 주기 위해서 Numpy를 이용해 배열로 만들었다.<br>
이후에는 figure,axes 객체를 생성해준 후 객체를 이용하여 plot 그래프 까지 만들어보자.<br>


```python
fig, ax = plt.subplots(figsize=(10,5)) #figure, axes 객체 생성
ax.plot(data,data2,marker = '.',label='X') # 생성된 axes 에 대한 plot() 멤버 직접 호출 
ax.plot(data,data2-100,marker = 'v',label='Y') # 생성된 axes 에 대한 plot() 멤버 직접 호출 
```

matplotlib로 그래프를 그리려면 Figure 객체와 하나 이상의 subplot(Axes) 객체가 필요하다.<br>
Axes 객체는 다시 두 개의 Axis 객체를 포함한다.<br> 여기서 Axis 객체가 y축과 x축을 나타냅니다.<br>
.subplots() 함수를 통해 figure와 axes 객체를 직접 생성해줄 수 있다.<br>
figure는 그래프가 그려질 전체적인 캔버스라고 보면 된다. <br>
figsize=(x축의크기,y축의크기)로 캔버스의 크기를 설정 가능하다.<br><br>
그 후 Axes 객체의 .plot() 함수로 플롯 그래프를 만들 수 있다.<br>
plot함수는 매개 변수로 [x축이 될 데이터(axis0)], [y축이 될 데이터(axis1)], [plot설정] 순서로 입력을 해주면 된다.<br>
[plot설정] 부분에는 fmt = '[marker][line][color]'로 대체 될 수있다.
'v-r' 이라고 입력해게 된다면 빨간색 실선에 V모양 마커표시를 하겠다는 의미이다.
<br>
이렇게 해주면 axes 객체 안에 plot은 다수 일 수 있다. 즉 한 캔버스 안에 여러 plot그래프를 담을 수 있다는 뜻이다.
<br>
이제 선형 plot 그래프를 만들기 위한 모든 재료는 준비가 된거다.
<br> 간단한 추가 설정 후에 실행까지 해보자.
<br>

```python
import matplotlib.pyplot as plt
import numpy as np

data = [1,2,3,4,5,6,7]
data2 = np.arange(100,800,100)



fig, ax = plt.subplots(figsize=(10,5)) #figure, axes 객체 생성
ax.plot(data,data2,marker = '.',label='X') # 생성된 axes 에 대한 plot() 멤버 직접 호출 
ax.plot(data,data2-100,marker = 'v',label='Y') # 생성된 axes 에 대한 plot() 멤버 직접 호출 
ax.set_title('line graph') # 제목 설정
ax.legend(loc='best',fontsize=15,shadow=True) # 레전드(범례) 생성
ax.set_xlabel('X') #각 축에대한 이름 설정
ax.set_ylabel('Y')
plt.show() # 실행
```

<br>
    
![png](\assets\images\matplotlib1_files\matplotlib1_5_0.png)
    
<br>

보는 바와 같이 set_title()을 통해 제목을, set_xlabel()을 통해 각 축에 대한 이름을 설정해 줄 수 있다.
<br> 레전드는 그래프에서 보이는 좌측 상단의 범례 박스를 만들어 주는데 다양한 스타일을 줄 수 있다.
