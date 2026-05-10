import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA ---
st.set_page_config(
    page_title="TMVio - Inteligência Financeira",
    page_icon="💰",
    layout="wide"
)

# --- 2. ESTILO CSS PREMIUM ---
st.markdown("""
    <style>
    .main { background: linear-gradient(180deg, #f0f4f8 0%, #ffffff 300px); }
    h1, h2 { color: #002347; text-align: center; }
    .card {
        padding: 20px; border-radius: 15px; background-color: #ffffff;
        border-left: 5px solid #00d4ff; box-shadow: 0px 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        min-height: 180px;
    }
    [data-testid="stSidebar"] { background-color: #002347; }
    [data-testid="stSidebar"] * { color: white !important; }
    @media (max-width: 600px) {
        h1 { font-size: 1.8rem !important; }
        .card { height: auto !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MENU LATERAL ---
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)
    else:
        st.title("TMVio")

    st.markdown("---")
    menu = st.radio(
        "Navegação",
        ["Início", "Sobre a TMVio", "Soluções & Sistemas", "Contacto"]
    )
    st.markdown("---")
    st.caption("Uma Solução Tercio Moreira Systems")
    st.caption("By Tércio Moreira")

# --- 4. PÁGINA: INÍCIO ---
if menu == "Início":
    st.markdown("<br><h1>Sua voz é o comando. O Vio é o seu gestor.</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #555;'>Inovação tecnológica para finanças pessoais e gestão de Alojamento Local.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>🎙️ Vio Voz</h3><p>Registo de gastos imediato por voz. Inteligência que entende o mercado português.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>🏠 TMHostbot</h3><p>A revolução no AL. Automação de check-ins e atendimento 24/7 para hóspedes.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h3>📊 Gestão TM</h3><p>Sistemas desenhados para máxima eficiência e conformidade legal (IRS/SEF).</p></div>', unsafe_allow_html=True)

# --- 5. PÁGINA: SOBRE A TMVIO ---
elif menu == "Sobre a TMVio":
    st.title("Inovação com Herança")
    col_a, col_b = st.columns([1, 1.5])
    with col_b:
        st.write("""
        ### O Significado do TM
        A **TMVio** carrega as iniciais do seu fundador, **Tércio Moreira**. É um compromisso de excelência técnica e legado. 
        
        Nascemos em Portugal para colmatar a lacuna entre tecnologia de ponta e a vida prática. Seja gerindo as finanças da casa com o **Vio**, ou automatizando um império de Alojamento Local com o **TMHostbot**, a nossa engenharia foca no que importa: o seu tempo.
        """)
    st.info("Foco estratégico em Albufeira, Lisboa e Porto.")

# --- 6. PÁGINA: SISTEMAS TM (VIO & HOSTBOT) ---
elif menu == "Soluções & Sistemas":
    st.title("Ecossistema de Inovação")

    tab1, tab2 = st.tabs(
        ["💎 TMHostbot (Alojamento Local)", "📱 Vio (Finanças Pessoais)"])

    with tab1:
        st.markdown("""
        ### TMHostbot: A Revolução do AL em Portugal
        O sistema definitivo para quem gere AL e quer escala sem perder o toque humano.
        
        * **Automação Total:** Gestão de check-ins e chaves.
        * **IA Multilingue:** Atendimento aos hóspedes em qualquer idioma, 24 horas por dia.
        * **Conformidade:** Integração com SEF e faturação automática.
        """)
        st.info("💡 A solução para 100% de ocupação com 0% de stress.")

    with tab2:
        st.markdown("""
        ### Vio: O Seu Gestor Financeiro por Voz
        A simplicidade de apenas falar e ter tudo organizado.
        
        * **Registo Direto:** "Gastei 50 euros no Pingo Doce".
        * **Categorização:** Separação automática para o e-fatura.
        * **Exportação:** Relatórios prontos para o seu IRS.
        """)
        st.success("📱 Transforme a sua voz na sua maior aliada financeira.")

# --- 7. PÁGINA: CONTACTO ---
elif menu == "Contacto":
    st.title("Fale com a Equipa TMVio")
    col_f1, col_f2, col_f3 = st.columns([0.2, 0.6, 0.2])
    with col_f2:
        with st.form("contacto_tmvio"):
            st.text_input("Seu Nome")
            st.text_input("E-mail Profissional")
            st.text_area("Como podemos ajudar o seu negócio ou rotina?")
            if st.form_submit_button("Solicitar Diagnóstico"):
                st.balloons()
                st.success(
                    "Mensagem enviada! Tércio Moreira entrará em contacto brevemente.")

# --- 8. RODAPÉ ---
st.divider()
st.caption(
    "© 2026 TMVio | Uma Solução Tercio Moreira Systems | tm-vio.com | Portugal")
