import streamlit as st

st.set_page_config(page_title="Precificadora Base - Eventos e Festas", layout="centered")

st.title("🎉 Precificadora Base - Eventos e Festas")
st.markdown("Ferramenta do Hub Encontro D’Água ✨")
st.markdown("Crie preços mais justos e sustentáveis para o seu trabalho com festas, lembrancinhas, decoração, buffet e muito mais!")

# ========== MATERIAIS ==========
st.header("🎨 Materiais usados")
materiais = []
for i in range(1, 11):
    nome = st.text_input(f"Material {i} - Nome", key=f"nome_{i}")
    preco_total = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"preco_{i}")
    porcentagem = st.slider(f"Porcentagem usada por produto (%)", 0, 100, 0, key=f"porcentagem_{i}")

    if nome and preco_total > 0 and porcentagem > 0:
        custo = (porcentagem / 100) * preco_total
        materiais.append((nome, custo))

# ========== TEMPO E PRODUÇÃO ==========
st.header("⏱️ Tempo e Produção")
tempo_total = st.number_input("Tempo total para produzir (minutos)", min_value=1)
qtd_produzida = st.number_input("Quantidade produzida nesse tempo", min_value=1)
tempo_unitario = tempo_total / qtd_produzida if qtd_produzida else 1

# ========== OUTROS CUSTOS ==========
st.header("📦 Outros Custos")
tempo_valor = st.number_input("Quanto vale seu tempo por unidade? (R$)", min_value=0.0)
embalagem = st.number_input("Custo da embalagem (R$)", min_value=0.0)
transporte = st.number_input("Custo de transporte por unidade (R$)", min_value=0.0)

# ========== MARGEM DE LUCRO ==========
st.header("📈 Margem de Lucro")
lucro = st.slider("Margem de lucro desejada (%)", 0, 200, 30)

# ========== RESULTADO ==========
if st.button("📊 Calcular"):
    custo_materiais = sum([c for _, c in materiais])
    custo_total = custo_materiais + tempo_valor + transporte + embalagem
    preco_sugerido = custo_total * (1 + lucro / 100)

    st.success(f"💰 Custo por unidade: R$ {custo_total:.2f}")
    st.success(f"💸 Preço sugerido com lucro: R$ {preco_sugerido:.2f}")

    preco_final = st.number_input("Preço que você pretende cobrar (R$)", min_value=0.0)
    if preco_final:
        lucro_real = preco_final - custo_total
        st.info(f"💡 Lucro real por unidade: R$ {lucro_real:.2f}")

# ========== MENSAGENS FINAIS ==========

st.markdown("---")
st.subheader("📌 Lembrete importante:")
st.markdown("""
Valor não é só o preço que se cobra.  
É o cuidado com o tempo, os materiais, a criatividade, o esforço e a experiência que você entrega.  
Essa calculadora existe pra **te ajudar a honrar seu trabalho e precificar com consciência, justiça e sustentabilidade**.

Tudo que é feito com amor, merece ser valorizado com dignidade. 💛
""")

st.markdown("---")
st.subheader("🌊 Sobre o Hub Encontro D’Água")
st.markdown("""
Somos um espaço digital que une **tecnologia, ética e propósito**.  
Criamos agentes de IA e automações com alma para ajudar mães, artistas e pequenos negócios a crescerem com leveza e autonomia.  
Aqui, tecnologia é cuidado. É tempo devolvido. É sistema circular.  
👉 Siga a gente: **@encontrodagua.hub** 💧
""")

st.markdown("---")
st.subheader("♻️ Nosso compromisso com a sustentabilidade")
st.markdown("""
Essa ferramenta faz parte do nosso compromisso com a **sustentabilidade, impacto social e regeneração**.

Acreditamos numa tecnologia feita para apoiar — e não excluir. Por isso, oferecemos esta ferramenta de forma **acessível e inclusiva**, como parte do nosso movimento por uma **economia circular e solidária**.

Se você quiser e puder apoiar o Hub, existem duas formas:
- 💬 Indique para outra mãe, artesã ou empreendedora!
- 💛 Contribua com qualquer valor via Pix: **encontrodaguahub@gmail.com**

Sua ajuda nos permite continuar criando ferramentas que cuidam. 🌱
""")

st.markdown("---")
st.subheader("✨ Avaliação e Feedback")
st.markdown("[⭐ Avalie ou envie sugestões clicando aqui](https://tally.so/r/wbGRAy)")

# (também após o bloco de avaliação)

st.markdown("---")
st.subheader("🔧 Precisa de uma versão personalizada?")
st.markdown("""
Faz algo diferente de lembrancinha ou buffet?  
Quer uma calculadora que se encaixe melhor no seu tipo de produto?

👉 [Solicite aqui sua versão personalizada](https://tally.so/r/SEULINKPERSONALIZADO)
""")

