import streamlit as st
import os

# Configurações iniciais
st.set_page_config(
    page_title="TM Systems | Automação Inteligente",
    page_icon="🤖",
    layout="wide"
)

# --- ESTILO CSS PREMIUM ---
st.markdown("""
    <style>
    /* Gradiente suave no fundo */
    .main { 
        background: linear-gradient(180deg, #f0f4f8 0%, #ffffff 300px); 
    }
    
    /* Títulos com a cor do Logo */
    h1, h2, h3 { 
        color: #002347; 
        text-align: center; 
        font-family: 'Inter', sans-serif;
    }
    
    /* Efeito de elevação nos Cards (Hover) */
    .card {
        padding: 30px; 
        border-radius: 15px; 
        background-color: #ffffff;
        border-left: 5px solid #00d4ff; 
        box-shadow: 0px 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 250px;
        margin-bottom: 20px;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0px 12px 20px rgba(0,0,0,0.1);
        border-left: 5px solid #002347;
    }

    /* Botão Profissional */
    .stButton>button {
        width: 100%;
        background-color: #002347;
        color: white;
        border: none;
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        background-color: #00d4ff;
        color: #002347;
    }

    /* Ajuste do Formulário */
    [data-testid="stForm"] {
        border-radius: 20px;
        background-color: #f8f9fa;
        padding: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
if os.path.exists("logo.png"):
    st.image("logo.png", width=180)
else:
    st.title("TM Systems")

st.divider()

# --- HERO SECTION ---
st.markdown("<br>", unsafe_allow_html=True)
col_centro = st.columns([0.1, 0.8, 0.1])

with col_centro[1]:
    st.markdown("<h1>Transforme o seu atendimento em uma máquina de vendas 24/7.</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.3rem; color: #555;'>Engenharia de processos e IA para escalar o seu negócio em Portugal e na Europa.</p>", unsafe_allow_html=True)

    c_btn1, c_btn2, c_btn3 = st.columns([1, 1.5, 1])
    with c_btn2:
        if st.button("Consultoria Gratuita"):
            st.toast("Descubra como podemos ajudar abaixo!")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- ESPECIALIDADES ---
st.markdown("## Nossas Soluções Inteligentes")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="card">
            <h3 style='text-align: left;'>🤖 Agentes de IA</h3>
            <p style='color: #666;'>Implementamos cérebros digitais que atendem, qualificam e vendem 24 horas por dia.</p>
        </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
        <div class="card">
            <h3 style='text-align: left;'>⚙️ Automação Total</h3>
            <p style='color: #666;'>Conectamos o seu WhatsApp, CRM e ferramentas de gestão num único fluxo eficiente.</p>
        </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
        <div class="card">
            <h3 style='text-align: left;'>📊 Dashboards IA</h3>
            <p style='color: #666;'>Decisões baseadas em dados reais com painéis inteligentes de performance.</p>
        </div>
    """, unsafe_allow_html=True)

# --- FORMULÁRIO DE CONTACTO ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("## Fale com um Especialista")
col_form = st.columns([0.25, 0.5, 0.25])

with col_form[1]:
    with st.form("contacto_tm"):
        nome = st.text_input("Empresa / Responsável")
        email = st.text_input("E-mail Profissional")
        whatsapp = st.text_input("WhatsApp com indicativo (ex: +351)")
        mensagem = st.text_area("Qual o maior gargalo da sua operação hoje?")

        submit = st.form_submit_button("SOLICITAR ANÁLISE DE PROCESSO")
        if submit:
            if nome and email:
                st.balloons()
                st.success(
                    f"Excelente, {nome}! Recebemos o seu pedido. Entraremos em contacto em breve.")
            else:
                st.warning("Por favor, preencha o Nome e E-mail.")

# --- RODAPÉ ---
st.divider()
st.caption("© 2026 TM Systems | Engenharia de Processos & IA | tmsystems.pt")
