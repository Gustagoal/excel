import pandas as pd
import streamlit as st
from io import BytesIO

st.title("Juntar duas planilhas Excel")

# Upload das planilhas
planilha_enviar = st.file_uploader("Insira a primeira planilha", type=["xlsx", "xls"])
planilha_enviar2 = st.file_uploader("Insira a segunda planilha", type=["xlsx", "xls"])

if planilha_enviar and planilha_enviar2:
    # Lê as planilhas
    planilha1 = pd.read_excel(planilha_enviar)
    planilha2 = pd.read_excel(planilha_enviar2)

    # Exibe prévias
    st.write("📄 Primeira planilha:")
    st.dataframe(planilha1)

    st.write("📄 Segunda planilha:")
    st.dataframe(planilha2)

    # Faz o merge
    try:
        planilha_unica = pd.merge(planilha1, planilha2, how="inner", on="ID_Categoria")
        st.success("✅ Planilhas unidas com sucesso!")
        st.dataframe(planilha_unica)

        # Converter para Excel em memória
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            planilha_unica.to_excel(writer, index=False, sheet_name="Resultado")
        dados_excel = output.getvalue()

        # Botão para download
        st.download_button(
            label="📥 Baixar planilha unida",
            data=dados_excel,
            file_name="planilha_unida.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"❌ Erro ao juntar: {e}")
else:
    st.info("Envie as duas planilhas para começar.")
