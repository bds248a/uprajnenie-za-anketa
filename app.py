st.title("Анкета")

text = st.text_input("Въведи текст")
name = st.text_input("Въведи име")
subject = st.selectbox("Избери предмет", ["Математика", "Английски", "Български"])
grade = st.selectbox("Избери оценка"["6", "5", "4", "3", "2"])
age = st.number_input("Въведи на колко години си")

if age > 18:
  st.write("Ти не си ученик")
else:
  st.write("grade")

