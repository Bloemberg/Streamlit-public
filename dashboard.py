import streamlit as st
import plotly.express as px

def show_dashboard(results_df):
    st.subheader("📊 DQ Analyse Resultaten")
    st.dataframe(results_df)

    st.markdown("### Compleetheid per kolom")
    fig = px.bar(results_df, x="Kolom", y="Compleetheid (%)", color="Compleetheid (%)",
                 color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)

    if "Validiteit (%)" in results_df.columns:
        valid_df = results_df[results_df["Validiteit (%)"] != "n.v.t."]
        if not valid_df.empty:
            st.markdown("### Validiteit per kolom")
            fig2 = px.bar(valid_df, x="Kolom", y="Validiteit (%)", color="Validiteit (%)",
                          color_continuous_scale="Greens")
            st.plotly_chart(fig2, use_container_width=True)

    st.download_button("Download DQ-resultaten (CSV)", results_df.to_csv(index=False), "dq_result.csv")

    st.markdown("## 🧩 DQ-dimensies: legenda en uitleg")
    st.markdown("""
**✔️ Juistheid**: komt de waarde overeen met de werkelijkheid?  
**📦 Compleetheid**: zijn verplichte velden ingevuld?  
**🔤 Validiteit**: voldoet de waarde aan het juiste format of domein?  
**🔁 Consistentie**: klopt de samenhang tussen velden?  
**🕒 Actualiteit**: hoe actueel zijn de gegevens?  
**🗣️ Begrijpelijkheid**: zijn de waarden duidelijk en ondubbelzinnig?  
**🤔 Plausibiliteit**: zijn de waarden logisch binnen de context?  
**🧭 Traceerbaarheid**: is de herkomst van gegevens zichtbaar?  
**🎯 Precisie**: is het detailniveau van de data passend voor het doel?
""")
