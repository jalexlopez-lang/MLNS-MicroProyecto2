import streamlit as st
import joblib
from preprocesamiento import text_preprocess

model = joblib.load("resources/models/model.joblib")


def limpiar_texto():
	st.session_state["texto_entrada"] = ""


st.set_page_config(
	page_title="MicroProyecto # 2 de Machine Learning No Supervisado — MAIA",
	layout="centered",
)

st.markdown(
	"""
	<style>
		

		:root {
			--ink: #17212b;
			--muted: #66717d;
			--line: #d8e0e7;
			--paper: #f7fafc;
			--accent: #0f766e;
			--accent-dark: #0b5c56;
		}

		.stApp {
			background:
				radial-gradient(circle at 8% 5%, rgba(199, 232, 226, 0.7), transparent 32%),
				linear-gradient(135deg, #f7fafc 0%, #eef3f5 100%);
			color: var(--ink);
		}

		.block-container {
			max-width: 760px;
			padding: 8vh 1.5rem 4rem;
		}

		.eyebrow {
			color: var(--accent);
			font-family: 'DM Sans', sans-serif;
			font-size: 0.78rem;
			font-weight: 700;
			letter-spacing: 0.14em;
			margin-bottom: 0.8rem;
			text-transform: uppercase;
		}

		h1 {
			color: var(--ink);
			font-family: 'Space Grotesk', sans-serif;
			font-size: clamp(2.2rem, 6vw, 4.2rem);
			letter-spacing: -0.04em;
			line-height: 1;
			margin: 0;
		}

		.intro {
			color: var(--muted);
			font-family: 'DM Sans', sans-serif;
			font-size: 1.05rem;
			line-height: 1.6;
			margin: 1.2rem 0 2.6rem;
			max-width: 560px;
		}

		label, .stTextArea label {
			color: var(--ink) !important;
			font-family: 'DM Sans', sans-serif !important;
			font-size: 0.9rem !important;
			font-weight: 700 !important;
		}

		textarea {
			background: #ffffff !important;
			border: 1px solid var(--line) !important;
			border-radius: 12px !important;
			color: var(--ink) !important;
			font-family: 'DM Sans', sans-serif !important;
			font-size: 1rem !important;
			line-height: 1.55 !important;
			padding: 1rem !important;
		}

		textarea:focus {
			border-color: var(--accent) !important;
			box-shadow: 0 0 0 2px rgba(15, 118, 110, 0.14) !important;
		}

		.stButton > button {
			background: #ffea00 !important;
			border: 1px solid #ffea00 !important;
			border-radius: 6px;
			color: #000000 !important;
			font-family: 'DM Sans', sans-serif;
			font-size: 0.95rem;
			font-weight: 700;
			min-height: 2.75rem;
			transition: transform 150ms ease, box-shadow 150ms ease;
		}

		.stButton > button:hover {
			background: #f5df00 !important;
			border-color: #f5df00 !important;
			box-shadow: 0 5px 14px rgba(23, 33, 43, 0.12);
			transform: translateY(-1px);
		}

		div[data-testid="stHorizontalBlock"] {
			align-items: end;
			gap: 0.75rem;
			margin: 0.8rem 0 2.2rem;
		}

		.result-heading {
			color: var(--ink);
			font-family: 'Space Grotesk', sans-serif;
			font-size: 1.25rem;
			font-weight: 600;
			margin: 0 0 0.65rem;
		}

		.result-heading span {
			font-size: 1.6rem;
			font-weight: 800;
		}

		.result-note {
			background: rgba(255, 255, 255, 0.6);
			border-left: 3px solid var(--accent);
			color: var(--muted);
			font-family: 'DM Sans', sans-serif;
			font-size: 0.84rem;
			margin-top: 0.75rem;
			padding: 0.7rem 0.9rem;
		}
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">MicroProyecto # 2 de Machine Learning No Supervisado — MAIA</div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">Jairo Alexander López Garcia -  Miguel Angel Rodriguez Marin</div>', unsafe_allow_html=True)
st.title("Validador de Objetivos de Desarrollo Sostenible (ODS)")
st.markdown(
	'<p class="intro">Escribe un texto para analizarlo y visualizar su resultado de clasificación.</p>',
	unsafe_allow_html=True,
)

texto = st.text_area(
	"Texto de entrada",
	height=190,
	placeholder="Escribe o pega aquí el texto que deseas evaluar...",
	label_visibility="visible",
	key="texto_entrada",
)

evaluar, borrar = st.columns([1, 1])
with evaluar:
	evaluar_presionado = st.button("Evaluar", type="primary", use_container_width=True)
with borrar:
	st.button("Borrar", on_click=limpiar_texto, use_container_width=True)

resultado = ""
if evaluar_presionado and texto.strip():
	texto_procesado = text_preprocess(texto)
	resultado = str(model.predict([texto_procesado])[0])
elif evaluar_presionado:
	resultado = "Escribe un texto para iniciar la evaluación."

if resultado:
	st.markdown(
		f'<div class="result-heading">Objetivos de Desarrollo Sostenible Relacionado: '
		f'<span>{resultado}</span></div>',
		unsafe_allow_html=True,
	)
else:
	st.markdown(
		'<div class="result-heading">Objetivos de Desarrollo Sostenible Relacionado:</div>',
		unsafe_allow_html=True,
	)

st.markdown(
	'<div class="result-note">El resultado corresponde a la predicción del modelo entrenado previamente en jupyter (model.joblib) notebook y entregado en el taller.</div>',
	unsafe_allow_html=True,
)
