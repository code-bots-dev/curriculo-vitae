import streamlit as st
import base64
from datetime import date
import functions

st.set_page_config(page_title="Currículo - Vitor Pereira", layout="wide")

def load_page():
    nome = "Vitor Rafael Ribeiro Pereira"
    contato_email = "vr351876@gmail.com"
    contato_telefone = "(83) 99143-5879"
    nacionalidade = "Brasileiro"
    nascimento = "21/11/1997"
    endereco = "João Pessoa, PB"
    objetivo = ("- Atuar no desenvolvimento e automação de sistemas, aplicando soluções inteligentes em Python, APIs e integração de dados para otimizar processos e aumentar a eficiência operacional."
                "Busco evoluir continuamente na área de tecnologia e inovação, desenvolvendo projetos que envolvam automação de rotinas, agentes inteligentes e análise de dados, "
                "com foco em melhoria de performance e resultados mensuráveis.")  # do PDF. 2

    experiencias = [
        {
            "cargo": "Analista de sistemas JR",
            "empresa": "Unimed João Pessoa",
            "local": "João Pessoa, PB",
            "periodo": "Janeiro 2023 - Atual",
            "atividades": [
                            "Desenvolvimento e integração de sistemas internos e APIs",
                            "Criação e manutenção de chatbots e automações de processos",
                            "Realização de testes funcionais, de performance e de interface",
                            "Análise de desempenho de sistemas CRM e NPS, propondo melhorias",
                            "Suporte técnico e atendimento aos usuários de softwares corporativos",
                            "Participação em projetos de melhoria contínua e implementação de novas funcionalidades",
                            "Documentação de processos, fluxos e soluções técnicas",
                            "Colaboração com equipes multidisciplinares para garantir eficácia das soluções"
                        ]
        },
        {
            "cargo": "Assistente de departamento pessoal",
            "empresa": "Unimed João Pessoa",
            "local": "João Pessoa, PB",
            "periodo": "Janeiro 2018 - Dezembro 2022",
            "atividades": [
                "Auxílio nas atividades de administração de pessoal (admissões, rescisões e benefícios).",
                "Suporte na gestão do ponto eletrônico e folha de pagamento.",
                "Gestão de férias e afastamentos.",
                "Atendimento aos funcionários sobre regras internas e direitos trabalhistas."
            ],
        },
    ]

    formacao = {
        "curso": "Análise e Desenvolvimento de Sistemas",
        "instituicao": "Unipe, João Pessoa, PB",
        "periodo": "Janeiro 2020 - Julho 2022",
        "status": "Concluído",
        "detalhes": [
            "Desenvolvimento e Integração de sistemas.",
            "Desenvolvimento de Chatbots e Automação de processos.",
            "Testes funcionais, análise de performance e participação em reuniões técnicas."
        ],
    }

    habilidades = [
        "**Python** — domínio em desenvolvimento backend, automação de processos e análise de dados.",
        "**Bancos de Dados:** Oracle SQL, PostgreSQL e MongoDB — modelagem, consultas avançadas e integração com aplicações.",
        "**Desenvolvimento de APIs e Integrações de Sistemas** — criação, consumo e documentação de APIs REST.",
        "**Oracle APEX** — desenvolvimento e manutenção de aplicações corporativas.",
        "**TOTVS (RM, Protheus e Datasul)** — integração, automação de rotinas e análise de dados via APIs e banco de dados.",
        "**Postman e Pentaho (PDI)** — testes de integração e desenvolvimento de fluxos de ETL e automações.",
        "**Desenvolvimento de Chatbots e Agentes Inteligentes** — uso de Python e IA para criação de assistentes automatizados.",
        "**Análise de Dados e Business Intelligence (BI)** — criação de dashboards, relatórios e extração de insights.",
        "**Microsoft Office (Avançado)** — automação e integração de planilhas e relatórios com Python."
    ]

    certificacoes = [
        "Formação Completa Inteligência Artificial (2025)",
        "Dominando o Databricks com Spark e Pyspark (2025)",
        "Oracle Apex - Targettrust (2024)",
        "Python Completo - Udemy (2023)",
        "Oracle APEX Básico ao Avançado - Udemy (2022)",
        "SQL e PL/SQL - Udemy (2022)",
        "Curso Java - Udemy (2021)",
        "PowerBI Completo - Udemy (2021)",
        "Formação em Gestor de RH - ABRH (2019)"
    ]

    st.title(f"{nome}")
    col1, col2 = st.columns([2, 1])

    with st.container(border=True):
        st.subheader("Contato e Informações Pessoais")

        # Linha principal com dados
        col1, col2, col3 = st.columns([1.5, 1.2, 1])

        with col1:
            st.markdown(f"📧 **E-mail:** [{contato_email}](mailto:{contato_email})")
            st.markdown(
                f"📱 **Celular / WhatsApp:** [{contato_telefone}](https://wa.me/55{contato_telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')})")

        with col2:
            st.markdown(f"🌎 **Nacionalidade:** {nacionalidade}")
            st.markdown(f"🎂 **Nascimento:** {nascimento} ({functions.calcula_idade(nascimento)} anos)")

        with col3:
            st.markdown(f"📍 **Localização:** {endereco}")
            st.markdown(f"💼 **LinkedIn:** [Vitor Rafael](https://www.linkedin.com/in/vitor-rafael-baba6a173/)")

        whatsapp_numero = "83991435879"
        st.markdown(
            f"""
            <a href="https://wa.me/{whatsapp_numero}" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" 
                     width="40" alt="WhatsApp">
            </a>
            
            <a href="https://www.linkedin.com/in/vitor-rafael-baba6a173/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" 
                     width="33" alt="LinkedIn">
            </a>
            
            <a href="https://github.com/code-bots-dev" target="_blank" style="margin-right:15px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="33" alt="GitHub">
            </a>
            """,
            unsafe_allow_html=True
        )
        st.write("")

    with st.container(border=False):
        st.write("")
        st.write("")
        st.header("🎯 Objetivo Profissional")
        st.write(objetivo)
        st.markdown("---")

        st.header("📝 Resumo / Destaques")
        st.write("- Profissional com sólida experiência em desenvolvimento de sistemas, automação de processos e integração de APIs, atuando na entrega de soluções inteligentes e eficientes que otimizam fluxos de trabalho e reduzem esforços manuais. "
                 "\n\n- Domínio de Python, com foco em automação, análise de dados e integração entre plataformas corporativas. Experiência prática em JavaScript, HTML, CSS e bancos de dados Oracle, PostgreSQL e MongoDB, garantindo aplicações estáveis e bem estruturadas."
                 "\n\n- Atuação em projetos que envolvem chatbots, agentes inteligentes, APIs REST, testes funcionais e suporte técnico especializado, com ênfase em qualidade, desempenho e melhoria contínua."
                 "\n\n- Perfil proativo, analítico e orientado a resultados, com facilidade para compreender processos complexos e transformá-los em soluções automatizadas e escaláveis."
                 "\n\n- Motivado por desafios que envolvam inovação, integração de sistemas e o uso de Inteligência Artificial aplicada à automação corporativa."
        )

    st.markdown("---")
    st.header("💼 Histórico Profissional")
    for exp in experiencias:
        st.subheader(f"{exp['cargo']} — {exp['empresa']}")
        st.write(f"{exp['periodo']} • {exp['local']}")
        for a in exp["atividades"]:
            st.write(f"- {a}")

    st.markdown("---")
    st.header("🎓 Formação Acadêmica")
    st.subheader(f"{formacao['curso']} — {formacao['instituicao']}")
    st.write(f"{formacao['periodo']} • {formacao['status']}")
    for d in formacao["detalhes"]:
        st.write(f"- {d}")

    st.markdown("---")
    st.header("🧠 Habilidades Técnicas")
    for a in habilidades:
        # st.write(" • ".join(habilidades))
        st.write(f"- {a}")

    st.markdown("---")
    st.header("💡 Certificações Técnicas e Profissionais")
    for c in certificacoes:
        st.write(f"- {c}")

    # ----- Exportar para HTML (botão) -----
    st.markdown("---")
    # st.write("*Exportar / Fazer download*")
    def generate_html(nome, email, telefone, objetivo, experiencias, formacao, habilidades, certificacoes):
        html = f"""
        <!doctype html>
        <html>
        <head>
          <meta charset="utf-8">
          <title>Currículo - {nome}</title>
          <style>
            body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 30px auto; line-height:1.45; color:#222 }}
            h1 {{ border-bottom: 2px solid #ddd; padding-bottom:6px }}
            h2 {{ color:#333; margin-top:18px }}
            .meta {{ float:right; text-align:right }}
            .section {{ margin-bottom: 18px }}
            ul {{ margin-top:6px }}
          </style>
        </head>
        <body>
          <h1>{nome}</h1>
          <div class="meta">
            <div>{email}</div>
            <div>{telefone}</div>
          </div>
          <div style="clear:both"></div>
          <h2>Objetivo</h2>
          <p>{objetivo}</p>
          <h2>Histórico Profissional</h2>
        """
        for exp in experiencias:
            html += f"<h3>{exp['cargo']} — {exp['empresa']}</h3>"
            html += f"<p><em>{exp['periodo']} • {exp['local']}</em></p><ul>"
            for a in exp["atividades"]:
                html += f"<li>{a}</li>"
            html += "</ul>"

        html += "<h2>Formação Acadêmica</h2>"
        html += f"<h3>{formacao['curso']} — {formacao['instituicao']}</h3>"
        html += f"<p><em>{formacao['periodo']} • {formacao['status']}</em></p><ul>"
        for d in formacao["detalhes"]:
            html += f"<li>{d}</li>"
        html += "</ul>"

        html += "<h2>Habilidades & Competências</h2>"
        html += f"<p>{', '.join(habilidades)}</p>"

        html += "<h2>Certificações</h2><ul>"
        for c in certificacoes:
            html += f"<li>{c}</li>"
        html += "</ul>"

        html += f"<footer style='margin-top:30px'><small>Gerado em {date.today().isoformat()}</small></footer></body></html>"
        return html

    html_content = generate_html(nome, contato_email, contato_telefone, objetivo, experiencias, formacao, habilidades, certificacoes)

    b64 = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    href = f'<a href="data:text/html;base64,{b64}" download="Curriculo_{nome.replace(" ", "_")}.html">Baixar currículo (HTML)</a>'
    # st.markdown(href, unsafe_allow_html=True)

    # Também exibimos a versão HTML embutida (preview)
    # st.markdown("*Preview (HTML)*")
    # st.components.v1.html(html_content, height=700, scrolling=True)
    #
    # st.markdown("---")
    # st.write("Conteúdo extraído do PDF enviado e usado para preencher este currículo. 4")

load_page()
