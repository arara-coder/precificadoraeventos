import streamlit as st

st.set_page_config(page_title="Calculadora para Festas & Eventos", layout="centered")

st.title("🎉 Calculadora de Preço - Festas e Eventos")
st.markdown("Desenvolvida com afeto pelo Hub Encontro D’Água 💧")

st.markdown("Calcule o preço ideal para seus produtos de festa — lembrancinhas, decoração, doces e mais — com cuidado, justiça e valorização 💛")

# ========== Materiais ==========
st.header("🎨 Materiais utilizados")
materiais = []

for i in range(1, 4):
    nome = st.text_input(f"Material {i}", key=f"mat_nome_{i}")
    preco = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"mat_preco_{i}")
    porcentagem = st.slider(f"Porcentagem usada (%)", 0, 100, 0, key=f"mat_porcentagem_{i}")
    if nome and preco > 0 and porcentagem > 0:
        custo = (porcentagem / 100) * preco
        materiais.append((nome, custo))

with st.expander("➕ Adicionar mais materiais"):
    for i in range(4, 11):
        nome = st.text_input(f"Material {i}", key=f"mat_nome_{i}")
        preco = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"mat_preco_{i}")
        porcentagem = st.slider(f"Porcentagem usada (%)", 0, 100, 0, key=f"mat_porcentagem_{i}")
        if nome and preco > 0 and porcentagem > 0:
            custo = (porcentagem / 100) * preco
            materiais.append((nome, custo))

# ========== Tempo, Transporte e Produção ==========
st.header("⏱️ Tempo e Transporte")

tempo_total = st.number_input("Tempo total para produzir tudo (minutos)", min_value=1)
transporte_total = st.number_input("Custo total com transporte (R$)", min_value=0.0)
qtd_total = st.number_input("Quantidade total produzida", min_value=1)

tempo_por_unidade = tempo_total / qtd_total
transporte_por_unidade = transporte_total / qtd_total
tempo_valor = st.number_input("Quanto vale seu tempo por minuto? (R$)", min_value=0.0)

# ========== Embalagem e Lucro ==========
st.header("📦 Embalagem e Lucro")

embalagem = st.number_input("Custo da embalagem (por unidade) (R$)", min_value=0.0)
lucro = st.slider("Margem de lucro desejada (%)", 0, 200, 30)

# ========== Cálculo Final ==========
if st.button("📊 Calcular"):
    custo_materiais = sum([c for _, c in materiais])
    custo_unitario = custo_materiais + (tempo_por_unidade * tempo_valor) + transporte_por_unidade + embalagem
    preco_sugerido = custo_unitario * (1 + lucro / 100)

    st.success(f"💰 Custo por unidade: R$ {custo_unitario:.2f}")
    st.success(f"💸 Preço sugerido com lucro: R$ {preco_sugerido:.2f}")

    preco_final = st.number_input("Quanto você pretende cobrar por unidade? (R$)", min_value=0.0)
    if preco_final:
        lucro_real = preco_final - custo_unitario
        st.info(f"💡 Lucro real por unidade: R$ {lucro_real:.2f}")

# ========== Informações adicionais ==========
with st.expander("💛 Sobre valor, propósito e o Hub"):
    st.subheader("📌 Lembrete importante:")
    st.markdown("""
    Valor não é só o preço que se cobra.  
    É o cuidado com o tempo, os materiais, a criatividade, o esforço e a experiência que você entrega.  
    Essa calculadora foi criada para **te ajudar a reconhecer e honrar seu trabalho com justiça e sustentabilidade**.

    Tudo que é feito com amor, merece ser valorizado com dignidade. 💛
    """)

    st.subheader("🌊 Sobre o Hub Encontro D’Água")
    st.markdown("""
    Somos um espaço digital que une **tecnologia, ética e propósito**.  
    Criamos ferramentas com alma para apoiar mães, artistas e pequenos negócios.  
    Aqui, tecnologia é cuidado. É tempo devolvido. É sistema circular.  
    👉 [@encontrodagua.hub](https://instagram.com/encontrodagua.hub)
    """)

    st.subheader("♻️ Nosso compromisso com a sustentabilidade")
    st.markdown("""
    Esta ferramenta faz parte do nosso compromisso com a **sustentabilidade, impacto social e regeneração**.

    Se você quiser e puder apoiar o Hub, existem duas formas:  
    💬 Indique para outra mãe ou empreendedora!  
    💛 Contribua com qualquer valor via Pix: **encontrodaguahub@gmail.com**
    """)

# ========== Extras ==========
st.markdown("---")
st.markdown("✨ [Avalie a calculadora ou envie sugestões](https://tally.so/r/wbGRAy)")
st.markdown("🔧 [Solicite uma versão personalizada para o seu negócio](https://tally.so/r/SEULINKAQUI)")
st.markdown("💬 [Fale com a Mazô no WhatsApp](https://wa.me/SEUNUMEROAQUI)")
