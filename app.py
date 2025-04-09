import streamlit as st

st.set_page_config(page_title="Precificadora Base - Eventos & Festas", layout="centered")

st.title("🎉 Precificadora Base - Eventos e Festas")
st.markdown("Ferramenta do Hub Encontro D’Água para mães criativas e empreendedoras ✨")

st.header("📦 Materiais usados")
materiais = []
for i in range(1, 11):
    nome = st.text_input(f"Material {i} - Nome", key=f"nome_{i}")
    preco_total = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"preco_{i}")
    porcentagem = st.slider(f"Porcentagem usada por peça/produto (%)", 0, 100, 0, key=f"porcentagem_{i}")

    if nome and preco_total > 0 and porcentagem > 0:
        custo = (porcentagem / 100) * preco_total
        materiais.append((nome, custo))

st.header("⏱️ Tempo e produção")
tempo_total = st.number_input("Tempo total para produção (minutos)", min_value=1)
qtd = st.number_input("Quantidade produzida nesse tempo", min_value=1)
tempo_unit = tempo_total / qtd if qtd else 1

tempo_valor = st.number_input("Quanto vale seu tempo por unidade? (R$)", min_value=0.0)
transporte = st.number_input("Custo de transporte por unidade (R$)", min_value=0.0)
embalagem = st.number_input("Custo da embalagem (R$)", min_value=0.0)

lucro = st.slider("Margem de lucro desejada (%)", 0, 200, 30)

if st.button("📊 Calcular"):
    custo_materiais = sum([c for _, c in materiais])
    custo_total = custo_materiais + transporte + tempo_valor + embalagem
    preco_sugerido = custo_total * (1 + lucro / 100)

    st.success(f"Custo por unidade: R$ {custo_total:.2f}")
    st.success(f"Preço sugerido com lucro: R$ {preco_sugerido:.2f}")

    preco_final = st.number_input("Preço que você pretende cobrar (R$)", min_value=0.0)
    if preco_final:
        lucro_real = preco_final - custo_total
        st.info(f"Lucro real por unidade: R$ {lucro_real:.2f}")

st.markdown("---")
st.markdown("📌 Lembrete: valor não é só preço. Seu trabalho tem tempo, criatividade, carinho. Essa calculadora existe pra te apoiar e **valorizar seu fazer.**")
st.markdown("💛 Apoie o projeto: Pix para **contato@encontrodagua.com** ou indique para alguém do seu círculo 🌱")
st.markdown("[⭐ Avalie a calculadora ou sugira melhorias](https://tally.so/r/wbGRAy)")
