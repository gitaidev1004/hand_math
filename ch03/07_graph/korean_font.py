import matplotlib
import matplotlib.pyplot as plt
import platform

# 운영체제별 한글 글꼴 설정
system = platform.system()
if system == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"      # 맑은 고딕
elif system == "Darwin":                                # macOS
    plt.rcParams["font.family"] = "AppleGothic"
else:                                                   # Linux
    plt.rcParams["font.family"] = "NanumGothic"

# 음수 부호가 깨지는 것도 함께 해결
plt.rcParams["axes.unicode_minus"] = False

print("현재 운영체제:", system)
print("설정된 글꼴  :", plt.rcParams["font.family"])
