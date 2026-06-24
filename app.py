import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA ---
st.set_page_config(
    page_title="Crearis | Core Tech & AI",
    page_icon="🤖",
    layout="wide"
)

# --- 2. ESTILO CSS INTEGRADO (DARK MODE PREMIUM) ---
st.markdown("""
    <style>
    /* Fundo Principal da Página (Mesmo tom escuro da landing page) */
    .stApp {
        background-color: #030712;
    }
    
    /* Títulos e Textos Principais */
    h1 {
        color: #ffffff !important;
        text-align: center;
        font-weight: 700;
    }
    h2, h3 {
        color: #38bdf8 !important; /* Azul claro vibrante */
        text-align: center;
    }
    p {
        color: #9ca3af !important; /* Cinza claro para leitura confortável */
    }
    
    /* Configuração dos Cards de Produto */
    .card {
        padding: 25px;
        border-radius: 15px;
        background-color: #0b1329; /* Fundo do card ligeiramente mais claro que a página */
        border: 1px solid #1e293b;
        border-top: 4px solid #0052cc;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        min-height: 220px;
    }
    .card h3 {
        margin-top: 0px;
        text-align: left !important;
    }
    .card p {
        text-align: left !important;
        font-size: 0.95rem;
    }
    
    /* Customização da Barra Lateral (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #030712 !important; /* Mesma cor para funder o logo */
        border-right: 1px solid #1e293b;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Estilo das Linhas Divisórias */
    hr {
        border-color: #1e293b !important;
    }
    
    /* Ajustes para Dispositivos Móveis */
    @media (max-width: 600px) {
        h1 { font-size: 1.8rem !important; }
        .card { height: auto !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MENU LATERAL ---
with st.sidebar:
    # Link direto para o teu logo oficial no GitHub
    logo_url = "https://github.com/terciomoreira/projeto_tmsystems/blob/main/logo.png.jpeg?raw=true"
    st.image(logo_url, use_container_width=True)

    st.markdown("---")
    menu = st.radio(
        "Navegação",
        ["Início", "Sobre a Crearis", "O Nosso Ecossistema", "Contacto"]
    )
    st.markdown("---")
    st.caption("🌌 Crearis | Core Tech & AI")
    st.caption("Sistemas Globais Inteligentes")

# --- 4. PÁGINA: INÍCIO ---
if menu == "Início":
    st.markdown("<br><h1>Inovação Núcleo. Inteligência Sem Fronteiras.</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #9ca3af;'>Desenvolvemos ecossistemas tecnológicos e agentes de Inteligência Artificial para escalar o seu mundo.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>🎙️ Vio — Gestão por Voz</h3><p>O nosso primeiro produto global. Um bot de WhatsApp com IA que transforma áudios em controlo financeiro absoluto.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>🏠 Core AL (Hostbot)</h3><p>Automatização total para Alojamento Local. Atendimento multilingue 24/7 e gestão inteligente de hóspedes.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h3>📊 Custom AI Solutions</h3><p>Engenharia de software sob medida e integração de modelos LLM avançados para empresas.</p></div>', unsafe_allow_html=True)

# --- 5. PÁGINA: SOBRE A CREARIS ---
elif menu == "Sobre a Crearis":
    st.markdown("<br><h1>Moldando o Futuro com Core Tech & AI</h1>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1, 2])
    with col_b:
        st.write("""
        ### Quem Somos
        A **Crearis | Core Tech & AI** é uma software-house focada no desenvolvimento de soluções de nova geração. Combinamos engenharia de infraestrutura robusta (*Core Tech*) com camadas de Inteligência Artificial aplicada.
        
        Nascidos com base fiscal em Portugal e projeção global, os nossos produtos são desenhados para eliminar tarefas repetitivas e devolver o ativo mais precioso que existe: o seu tempo. Do controlo financeiro pessoal à gestão automatizada de propriedades, criamos tecnologia que funciona por si.
        """)
    st.info("🌐 Operação global gerida a partir de Portugal.")

# --- 6. PÁGINA: O NOSSO ECOSSISTEMA ---
elif menu == "O Nosso Ecossistema":
    st.markdown("<br><h1>Produtos Prontos a Escalar</h1>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📱 Vio Finance", "💎 Core AL & Hostbot"])

    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("""
        ### Vio: O Seu Gestor Financeiro por Voz
        A simplicidade de apenas falar com o WhatsApp e ter toda a sua vida financeira organizada por IA.
        
        * **Processamento de Áudio Nativo:** Envia mensagens de voz e a IA regista valores, locais e categorias.
        * **Independência de Apps:** Funciona diretamente no ecossistema global do WhatsApp.
        * **Pronto para o Mercado:** Lançamento internacional com foco em eficiência.
        """)
        st.link_button("Visitar a Página do Vio",
                       "https://vio-app-1.onrender.com/")

    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("""
        ### Core AL (Hostbot): A Revolução do Alojamento Local
        O sistema definitivo para gestores de propriedades que querem escala global com 0% de stress.
        
        * **IA Multilingue:** Atendimento automático aos hóspedes em qualquer idioma, a qualquer hora do dia.
        * **Sincronização Fiscal:** Integração inteligente com exigências de conformidade locais.
        * **Operação Automatizada:** Gestão inteligente de fluxos de check-in.
        """)
        st.info("💡 Solução em fase de integração de produto — Brevemente disponível.")

# --- 7. PÁGINA: CONTACTO ---
elif menu == "Contacto":
    st.markdown("<br><h1>Fale com a Crearis</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col_f1, col_f2, col_f3 = st.columns([0.2, 0.6, 0.2])
    with col_f2:
        with st.form("contacto_crearis"):
            st.text_input("Nome Corporativo / Individual")
            st.text_input("E-mail de Contacto Global")
            st.text_area(
                "Como é que as nossas soluções de IA podem potenciar a sua rotina ou negócio?")
            if st.form_submit_button("Enviar Mensagem"):
                st.balloons()
                st.success(
                    "Mensagem enviada com sucesso! A equipa da Crearis entrará em contacto brevemente.")

# --- 8. RODAPÉ ---
st.divider()
st.markdown("<div style='text-align: center; color: #6b7280; font-size: 0.85rem;'>© 2026 Crearis | Core Tech & AI | Suporte Global | Sede Fiscal: Portugal</div>", unsafe_allow_html=True)
