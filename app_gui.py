# -*- coding: utf-8 -*-
"""
🍗 갓슴살 AI 코치 — 화면(GUI) 버전
창이 뜨고, 버튼을 누르면 운동 분석 결과와 캐릭터 코멘트가 나옵니다.
(main.py의 분석 로직을 그대로 가져와 화면만 입혔습니다.)
"""

import tkinter as tk
from tkinter import scrolledtext

# main.py에서 만든 함수·데이터를 그대로 재사용
from main import 운동기록, 약점_분석, 캐릭터_코멘트, 호칭_만들기


def 분석하기():
    """버튼을 누르면 실행되는 함수 — 분석 결과를 화면에 표시"""
    이름 = 이름입력.get().strip() or "주한"

    분류_횟수, 가장_많은, 가장_적은 = 약점_분석(운동기록)

    # 결과 글 만들기
    줄들 = ["[오늘 한 운동]"]
    for 항목 in 운동기록:
        줄들.append(f"  · {항목['동작']}({항목['분류']}): {항목['값']}{항목['단위']}")

    줄들.append("\n[분류별 운동 횟수]")
    for 분류, 횟수 in 분류_횟수.items():
        줄들.append(f"  {분류:4s} | {'■' * 횟수} {횟수}개")

    줄들.append("\n[닭가슴살 코치의 한마디]")
    줄들.append(캐릭터_코멘트(이름, 가장_많은, 가장_적은, len(운동기록)))

    # 결과창에 출력 (기존 내용 지우고 새로 쓰기)
    결과창.config(state="normal")
    결과창.delete("1.0", tk.END)
    결과창.insert(tk.END, "\n".join(줄들))
    결과창.config(state="disabled")


# ── 창(윈도우) 만들기 ──
창 = tk.Tk()
창.title("🍗 갓슴살 AI 코치")
창.geometry("440x560")
창.configure(bg="#FFF6E5")

# 제목
tk.Label(창, text="🍗 갓슴살 AI 코치", font=("맑은 고딕", 20, "bold"),
         bg="#FFF6E5", fg="#D2691E").pack(pady=(18, 4))
tk.Label(창, text="운동 기록을 분석해 캐릭터가 약점을 코멘트해줘요",
         font=("맑은 고딕", 10), bg="#FFF6E5", fg="#7a6a55").pack()

# 이름 입력
입력틀 = tk.Frame(창, bg="#FFF6E5")
입력틀.pack(pady=14)
tk.Label(입력틀, text="캐릭터가 부를 이름: ", font=("맑은 고딕", 11),
         bg="#FFF6E5").pack(side="left")
이름입력 = tk.Entry(입력틀, font=("맑은 고딕", 11), width=12)
이름입력.insert(0, "주한")
이름입력.pack(side="left")

# 분석 버튼
tk.Button(창, text="운동 분석하기  🍗", font=("맑은 고딕", 13, "bold"),
          bg="#FF8C00", fg="white", activebackground="#E07B00",
          relief="flat", padx=20, pady=8, cursor="hand2",
          command=분석하기).pack(pady=6)

# 결과 표시창
결과창 = scrolledtext.ScrolledText(창, font=("맑은 고딕", 11), width=46,
                                  height=16, bg="white", fg="#333",
                                  relief="solid", borderwidth=1, wrap="word")
결과창.pack(padx=18, pady=12, fill="both", expand=True)
결과창.insert(tk.END, "위의 '운동 분석하기' 버튼을 눌러보세요!")
결과창.config(state="disabled")

# 창 띄우기 (닫을 때까지 실행 유지)
창.mainloop()
