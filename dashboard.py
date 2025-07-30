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

    if "Plausibiliteit (%)" in results_df.columns:
        plaus_df = results_df[results_df["Plausibiliteit (%)"] != "n.v.t."]
        if not plaus_df.empty:
            st.markdown("### Plausibiliteit per kolom")
            fig3 = px.bar(plaus_df, x="Kolom", y="Plausibiliteit (%)", color="Plausibiliteit (%)",
                          color_continuous_scale="Oranges")
            st.plotly_chart(fig3, use_container_width=True)

    if "Consistentie (%)" in results_df.columns:
        cons_df = results_df[results_df["Consistentie (%)"] != "n.v.t."]
        if not cons_df.empty:
            st.markdown("### Consistentie per kolom")
            fig4 = px.bar(cons_df, x="Kolom", y="Consistentie (%)", color="Consistentie (%)",
                          color_continuous_scale="Purples")
            st.plotly_chart(fig4, use_container_width=True)

    if "Begrijpelijkheid (%)" in results_df.columns:
        begrip_df = results_df[results_df["Begrijpelijkheid (%)"] != "n.v.t."]
        if not begrip_df.empty:
            st.markdown("### Begrijpelijkheid per kolom")
            fig5 = px.bar(begrip_df, x="Kolom", y="Begrijpelijkheid (%)", color="Begrijpelijkheid (%)",
                          color_continuous_scale="Teal")
            st.plotly_chart(fig5, use_container_width=True)

    st.download_button("Download DQ-resultaten (CSV)", results_df.to_csv(index=False), "dq_result.csv")

    st.markdown("## 🧩 DQ-dimensies: legenda en uitleg")
    st.markdown("""
**📦 Compleetheid**: zijn verplichte velden ingevuld?  
**🔢 Uniciteit**: hoe uniek zijn de waarden per kolom?  
**🔤 Validiteit**: voldoet de waarde aan het juiste format of domein?  
**🤔 Plausibiliteit**: zijn de waarden logisch binnen de context?  
**🗣️ Begrijpelijkheid**: zijn de waarden duidelijk en ondubbelzinnig?  
**🔁 Consistentie**: klopt de samenhang tussen velden?
""")

