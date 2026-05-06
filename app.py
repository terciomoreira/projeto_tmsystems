import streamlit as st
import os

# Configurações de Página
st.set_page_config(page_title="TM Systems | IA & Automação",
                   page_icon="🤖", layout="wide")

# --- ESTILO CSS PREMIUM (PT-PT) ---
st.markdown("""
    <style>
    .main { background: linear-gradient(180deg, #f0f4f8 0%, #ffffff 300px); }
    h1, h2 { color: #002347; text-align: center; }
    .card {
        padding: 20px; border-radius: 15px; background-color: #ffffff;
        border-left: 5px solid #00d4ff; box-shadow: 0px 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    /* Estilo do Menu Lateral */
    [data-testid="stSidebar"] { background-color: #002347; }
    [data-testid="stSidebar"] * { color: white !important; }
    /* Ajuste para Telemóveis */
    @media (max-width: 600px) {
        h1 { font-size: 1.8rem !important; }
        .card { height: auto !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    st.title("TM Systems")
    st.markdown("---")
    menu = st.radio(
        "Navegação",
        ["Início", "Sobre a Empresa", "Soluções", "Contacto"]
    )
    st.markdown("---")
    st.caption("Engenharia de Processos & IA")

# --- PÁGINA: INÍCIO ---
if menu == "Início":
    st.markdown("<br><h1>Converta o seu atendimento numa máquina de vendas 24/7.</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #555;'>Soluções de automação inteligente desenhadas para o mercado nacional e europeu.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>🤖 Agentes IA</h3><p>Atendimento autónomo que qualifica leads e agenda reuniões em tempo real.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>⚙️ Integrações</h3><p>Ligamos o seu CRM, WhatsApp e Email num fluxo de trabalho sem falhas.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h3>📊 Dashboards</h3><p>Monitorização de performance e KPIs estratégicos para decisões rápidas.</p></div>', unsafe_allow_html=True)

# --- PÁGINA: SOBRE A EMPRESA ---
elif menu == "Sobre a Empresa":
    st.title("A Nossa Identidade")
    col_a, col_b = st.columns([1, 1.5])
    with col_b:
        st.write("""
        ### Quem é a TM Systems?
        A **TM Systems** não é apenas uma consultora tecnológica; criada por Tércio de Souza Moreira, programador e empreendedor sabe bem como focar e atender as necessidades do cliente, somos arquitetos de eficiência operacional. Sediada em Portugal, a nossa empresa nasceu para colmatar a lacuna entre a tecnologia de ponta e a realidade prática dos negócios.
        
        Acreditamos que o capital humano deve ser investido em estratégia e criatividade, não em tarefas repetitivas. Por isso, desenvolvemos sistemas que "pensam" e executam processos de forma autónoma.
        
        **Os nossos pilares:**
        *   **Engenharia de Processos:** Analisamos o seu fluxo atual antes de automatizar.
        *   **IA Ética e Segura:** Implementamos soluções que protegem os dados dos seus clientes.
        *   **Foco no ROI:** Cada automação é desenhada para reduzir custos e aumentar a faturação.
        """)
    st.success(
        "Focamos em Albufeira, Porto e Lisboa, com capacidade de implementação em toda a União Europeia.")

# --- PÁGINA: SOLUÇÕES ---
elif menu == "Soluções":
    st.title("Especialidades Tecnológicas")
    tab1, tab2 = st.tabs(["Atendimento Inteligente", "Ecossistema de Gestão"])
    with tab1:
        st.write("""
        *   **Chatbots de Nova Geração:** Agentes que utilizam Processamento de Linguagem Natural para interagir como humanos.
        *   **Agendamento Automático:** Integração direta com Google Calendar e Outlook para clínicas e serviços.
        """)
    with tab2:
        st.write("""
        *   **Sincronização de CRM:** Mantenha o HubSpot, Salesforce ou Pipedrive sempre atualizados via WhatsApp.
        *   **Automação de Faturação:** Emissão de documentos e lembretes de pagamento sem intervenção manual.
        """)

# --- PÁGINA: CONTACTO ---
elif menu == "Contacto":
    st.title("Inicie a sua Transformação")
    col_f1, col_f2, col_f3 = st.columns([0.2, 0.6, 0.2])
    with col_f2:
        with st.form("contacto_pt"):
            st.text_input("Nome do Responsável")
            st.text_input("E-mail Profissional")
            st.text_input("Telemóvel / WhatsApp")
            st.text_area("Descreva o processo que pretende automatizar")
            if st.form_submit_button("Solicitar Diagnóstico Gratuito"):
                st.balloons()
                st.success(
                    "Recebemos o seu pedido. A nossa equipa entrará em contacto num prazo de 24 horas.")

# --- RODAPÉ ---
st.divider()
st.caption("© 2026 TM Systems | tmsystems.pt | Portugal")
