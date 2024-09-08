.PHONY: install run

install:
	poetry install

run:
	poetry run streamlit run app.py --server.port=8501 --server.enableCORS=false
