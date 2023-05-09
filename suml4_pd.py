import streamlit as st
import pickle

filename = 'C:\\Users\\Jasiek\\PycharmProjects\\suml3\\model_.sv'
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model


# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():
	st.set_page_config(page_title="Streamlit Chest Pain APP")
	overview = st.container()
	right = st.container()
	prediction = st.container()

	st.image("https://mlpforums.com/uploads/post_images/img-1330308-2-hnnng.jpg")

	with overview:
		st.title("Czy ten chłop ma chorobę serca?")

	with right:
		z1 = st.slider("Wiek:", value=40, min_value=28, max_value=100)
		z2 = st.slider("Resting Blood Pressure", value=132, min_value=0, max_value=200)
		z3 = st.slider("Cholesterol", value=200 , min_value=60, max_value=610)
		z4 = st.slider("Max Heart Rate", value=136, min_value=60, max_value=210)
		z5 = st.slider("Old peak", value=0.8, min_value=-3.0, max_value=7.0, step=0.1)

	data = [[z1, z2, z3, z4, z5]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("To jak, chory, czy nie?")
		st.subheader(("No, niestety" if survival[0] == 1 else "Uff! Nie!"))
		st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
