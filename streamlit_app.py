import streamlit as st

st.set_page_config(
    page_title="Propuesta Estratégica — Katerine Rengifo",
    page_icon="🌿",
    layout="wide",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #fdf8f3;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
    }

    .hero {
        background: linear-gradient(135deg, #4a7c59 0%, #2d5a3d 100%);
        color: white;
        padding: 3rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2.5rem;
        text-align: center;
    }

    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 2.4rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
        color: white;
    }

    .hero .subtitle {
        font-size: 1.05rem;
        opacity: 0.85;
        margin: 0.3rem 0;
        letter-spacing: 0.3px;
    }

    .hero .colectivo {
        margin-top: 1rem;
        font-size: 0.9rem;
        opacity: 0.7;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .section-card {
        background: white;
        border-radius: 14px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.8rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border-left: 5px solid #4a7c59;
    }

    .section-card.amber {
        border-left-color: #d4a847;
    }

    .section-card.rose {
        border-left-color: #c0636a;
    }

    .section-card.blue {
        border-left-color: #4a7099;
    }

    .section-card.neutral {
        border-left-color: #9e9e9e;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #2d2d2d;
        margin-bottom: 1rem;
    }

    .critical-item {
        background: #fff5f5;
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        margin-bottom: 0.7rem;
        border-left: 3px solid #c0636a;
    }

    .critical-item .ci-title {
        font-weight: 600;
        color: #8b3a3f;
        margin-bottom: 0.2rem;
        font-size: 0.95rem;
    }

    .critical-item .ci-desc {
        color: #5a5a5a;
        font-size: 0.88rem;
        line-height: 1.5;
    }

    .asset-item {
        background: #f3faf5;
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        margin-bottom: 0.7rem;
        border-left: 3px solid #4a7c59;
    }

    .asset-item .ai-emoji {
        font-size: 1.2rem;
        margin-right: 0.4rem;
    }

    .asset-item .ai-title {
        font-weight: 600;
        color: #2d5a3d;
        font-size: 0.95rem;
    }

    .asset-item .ai-desc {
        color: #5a5a5a;
        font-size: 0.88rem;
        line-height: 1.5;
        margin-top: 0.2rem;
    }

    .hypothesis-box {
        background: linear-gradient(135deg, #fdf3dc 0%, #fef9ed 100%);
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        border: 1px solid #e8c97a;
        font-style: italic;
        color: #5a4a1e;
        font-size: 1rem;
        line-height: 1.7;
    }

    .bloque-card {
        background: white;
        border-radius: 14px;
        padding: 1.8rem 2rem;
        margin-bottom: 1.4rem;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
        border-top: 4px solid #4a7c59;
    }

    .bloque-card.amber-top {
        border-top-color: #d4a847;
    }

    .bloque-card.blue-top {
        border-top-color: #4a7099;
    }

    .bloque-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 1rem;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .bloque-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        font-weight: 700;
        color: #2d2d2d;
    }

    .bloque-price {
        background: #4a7c59;
        color: white;
        padding: 0.3rem 0.9rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.95rem;
        white-space: nowrap;
    }

    .bloque-price.amber {
        background: #d4a847;
    }

    .bloque-price.blue {
        background: #4a7099;
    }

    .bloque-hours {
        color: #7a7a7a;
        font-size: 0.88rem;
        margin-bottom: 1rem;
    }

    .badge-recomendado {
        display: inline-block;
        background: #fff3cd;
        color: #856404;
        border: 1px solid #ffc107;
        border-radius: 20px;
        padding: 0.15rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 600;
        margin-left: 0.5rem;
        vertical-align: middle;
    }

    .deliverable-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9rem;
    }

    .deliverable-table th {
        background: #f5f5f5;
        padding: 0.6rem 0.8rem;
        text-align: left;
        font-weight: 600;
        color: #555;
        border-bottom: 2px solid #e0e0e0;
    }

    .deliverable-table td {
        padding: 0.6rem 0.8rem;
        border-bottom: 1px solid #f0f0f0;
        color: #3a3a3a;
        vertical-align: top;
    }

    .deliverable-table tr:last-child td {
        border-bottom: none;
    }

    .deliverable-table td:last-child {
        text-align: center;
        font-weight: 500;
        color: #4a7c59;
        white-space: nowrap;
    }

    .bloque-note {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        font-size: 0.84rem;
        color: #6a6a6a;
        margin-top: 1rem;
        line-height: 1.6;
        border-left: 3px solid #ccc;
    }

    .summary-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.95rem;
    }

    .summary-table th {
        background: #2d5a3d;
        color: white;
        padding: 0.8rem 1rem;
        text-align: left;
    }

    .summary-table td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #e8e8e8;
        color: #3a3a3a;
    }

    .summary-table tr.total-row td {
        background: #f3faf5;
        font-weight: 700;
        color: #2d5a3d;
        font-size: 1rem;
        border-top: 2px solid #4a7c59;
    }

    .mensual-options {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.2rem;
        margin-top: 1.2rem;
    }

    .mensual-card {
        border-radius: 12px;
        padding: 1.4rem;
        background: #f9f9f9;
        border: 2px solid #e0e0e0;
    }

    .mensual-card.recomendada {
        border-color: #4a7c59;
        background: #f3faf5;
    }

    .mensual-card .mc-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #2d2d2d;
        margin-bottom: 0.3rem;
    }

    .mensual-card .mc-price {
        font-size: 1.2rem;
        font-weight: 700;
        color: #4a7c59;
        margin-bottom: 0.8rem;
    }

    .condiciones-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .condiciones-list li {
        padding: 0.5rem 0;
        border-bottom: 1px solid #eeeeee;
        font-size: 0.92rem;
        color: #4a4a4a;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }

    .condiciones-list li:last-child {
        border-bottom: none;
    }

    .condiciones-list li::before {
        content: "→";
        color: #4a7c59;
        font-weight: 700;
        flex-shrink: 0;
    }

    .steps-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.2rem;
        margin-top: 0.5rem;
    }

    .step-card {
        background: white;
        border-radius: 12px;
        padding: 1.3rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.07);
    }

    .step-number {
        width: 40px;
        height: 40px;
        background: #4a7c59;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.1rem;
        margin: 0 auto 0.8rem auto;
    }

    .step-title {
        font-weight: 700;
        color: #2d2d2d;
        margin-bottom: 0.4rem;
        font-size: 0.95rem;
    }

    .step-desc {
        font-size: 0.84rem;
        color: #6a6a6a;
        line-height: 1.5;
    }

    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 2rem;
        border-top: 1px solid #e0e0e0;
        color: #888;
        font-size: 0.85rem;
        line-height: 1.7;
    }

    .footer strong {
        color: #4a7c59;
    }

    @media (max-width: 640px) {
        .mensual-options { grid-template-columns: 1fr; }
        .steps-grid { grid-template-columns: 1fr; }
        .hero h1 { font-size: 1.7rem; }
    }
</style>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Propuesta Estratégica</h1>
    <p class="subtitle">Katerine Rengifo · Psicóloga humanista</p>
    <p class="subtitle">Cali, Colombia</p>
    <p class="colectivo">Co|Creemos Colectivo</p>
</div>
""", unsafe_allow_html=True)


# ── RADIOGRAFÍA EXPRESS ───────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-title">Radiografía Express — Lo que encontramos en la sesión</div>
    <p style="color:#4a4a4a; line-height:1.7; margin:0;">
        Tienes experiencia real, clientes que te valoran y un espacio físico con identidad propia en
        <strong>Casa Entretejidos</strong>. Lo que falta es estructura y visibilidad.
        Tu trabajo existe — pero <strong>no se ve</strong>.
    </p>
</div>
""", unsafe_allow_html=True)


# ── PUNTOS CRÍTICOS ───────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card rose">
    <div class="section-title">Puntos críticos identificados</div>

    <div class="critical-item">
        <div class="ci-title">Invisibilidad digital</div>
        <div class="ci-desc">No tienes presencia en ninguna plataforma. Tu trabajo no existe en internet para quien no te conoce.</div>
    </div>

    <div class="critical-item">
        <div class="ci-title">Dependencia del voz a voz</div>
        <div class="ci-desc">Canal valioso pero frágil. No escala solo y no te permite elegir a quién acompañas.</div>
    </div>

    <div class="critical-item">
        <div class="ci-title">Nicho sin definir</div>
        <div class="ci-desc">No has establecido a quién le hablas ni qué te diferencia como psicóloga humanista.</div>
    </div>

    <div class="critical-item">
        <div class="ci-title">Sin estructura ni sistema</div>
        <div class="ci-desc">Hay intención y claridad interna, pero no hay un camino definido para avanzar.</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── ACTIVOS REALES ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-title">Tus activos reales</div>

    <div class="asset-item">
        <span class="ai-emoji">🤝</span><span class="ai-title">Consultantes actuales</span>
        <div class="ai-desc">Prueba social real. Ya hay personas que confían en tu proceso.</div>
    </div>

    <div class="asset-item">
        <span class="ai-emoji">🏡</span><span class="ai-title">Casa Entretejidos</span>
        <div class="ai-desc">Un espacio físico con identidad. Ancla de credibilidad y comunidad.</div>
    </div>

    <div class="asset-item">
        <span class="ai-emoji">🌿</span><span class="ai-title">Red de socios</span>
        <div class="ai-desc">Posibilidad de colaboración, contenido conjunto y visibilidad cruzada.</div>
    </div>

    <div class="asset-item">
        <span class="ai-emoji">💛</span><span class="ai-title">Enfoque humanista</span>
        <div class="ai-desc">Un diferenciador genuino. Acompañamiento con alma, no psicología clínica fría.</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── HIPÓTESIS ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card amber">
    <div class="section-title">Hipótesis de trabajo</div>
    <div class="hypothesis-box">
        Katerine necesita pasar de existir solo en la mente de sus referidos a existir en un espacio
        digital que la represente — con claridad de nicho, voz propia y una rutina mínima viable de
        contenido que genere visibilidad y confianza.
    </div>
</div>
""", unsafe_allow_html=True)


# ── LA PROPUESTA ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-title" style="font-family:'Georgia',serif; font-size:1.6rem; color:#2d2d2d; margin:2rem 0 1.2rem 0; text-align:center;">
    La propuesta — Tres bloques para arrancar
</div>
""", unsafe_allow_html=True)


# BLOQUE 1
st.markdown("""
<div class="bloque-card">
    <div class="bloque-header">
        <div>
            <span class="bloque-title">Bloque 1 — Identidad y nicho</span>
            <span class="badge-recomendado">⭐ Recomendado</span>
        </div>
        <span class="bloque-price">$240.000</span>
    </div>
    <div class="bloque-hours">6 horas de trabajo estratégico</div>
    <table class="deliverable-table">
        <thead>
            <tr>
                <th>Entregable</th>
                <th style="text-align:center;">Horas</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Sesión de exploración de marca personal</td><td>2h</td></tr>
            <tr><td>Definición de nicho y público objetivo</td><td>2h</td></tr>
            <tr><td>Propuesta de valor + bio profesional</td><td>2h</td></tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)


# BLOQUE 2
st.markdown("""
<div class="bloque-card amber-top">
    <div class="bloque-header">
        <div>
            <span class="bloque-title">Bloque 2 — Presencia mínima viable</span>
            <span class="badge-recomendado">⭐ Recomendado</span>
        </div>
        <span class="bloque-price amber">$200.000</span>
    </div>
    <div class="bloque-hours">5 horas de trabajo estratégico</div>
    <table class="deliverable-table">
        <thead>
            <tr>
                <th>Entregable</th>
                <th style="text-align:center;">Horas</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Auditoría y estrategia de perfil Instagram</td><td>1h</td></tr>
            <tr><td>Bio, foto de perfil y highlights definidos</td><td>2h</td></tr>
            <tr><td>Post ancla (quién soy + qué hago)</td><td>2h</td></tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)


# BLOQUE 3
st.markdown("""
<div class="bloque-card blue-top">
    <div class="bloque-header">
        <div>
            <span class="bloque-title">Bloque 3 — Sistema de contenido</span>
        </div>
        <span class="bloque-price blue">$280.000</span>
    </div>
    <div class="bloque-hours">7 horas de trabajo estratégico</div>
    <table class="deliverable-table">
        <thead>
            <tr>
                <th>Entregable</th>
                <th style="text-align:center;">Horas</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Definición de pilares de contenido</td><td>2h</td></tr>
            <tr><td>Plan de contenido mes 1 — 8 piezas definidas en texto</td><td>3h</td></tr>
            <tr><td>Sesión de acompañamiento para arrancar</td><td>2h</td></tr>
        </tbody>
    </table>
    <div class="bloque-note">
        <strong>Importante:</strong> El plan de contenido incluye definición estratégica de cada pieza —
        tema, formato, copy orientativo y calendario. No incluye producción gráfica ni ejecución visual.
        Las piezas las produce Katerine o quien ella designe.
    </div>
</div>
""", unsafe_allow_html=True)


# ── RESUMEN ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-title">Resumen — Bloques 1 + 2 + 3</div>
    <table class="summary-table">
        <thead>
            <tr><th>Bloque</th><th style="text-align:right;">Valor</th></tr>
        </thead>
        <tbody>
            <tr><td>Bloque 1 — Identidad y nicho</td><td style="text-align:right;">$240.000</td></tr>
            <tr><td>Bloque 2 — Presencia mínima viable</td><td style="text-align:right;">$200.000</td></tr>
            <tr><td>Bloque 3 — Sistema de contenido</td><td style="text-align:right;">$280.000</td></tr>
            <tr class="total-row"><td>Total</td><td style="text-align:right;">$720.000</td></tr>
        </tbody>
    </table>
    <p style="margin:1rem 0 0 0; font-size:0.88rem; color:#777; text-align:center;">
        18 horas de trabajo estratégico
    </p>
</div>
""", unsafe_allow_html=True)


# ── BLOQUE 4 ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card blue">
    <div class="section-title">Bloque 4 — Acompañamiento mensual</div>
    <p style="color:#4a4a4a; font-size:0.92rem; line-height:1.6; margin-bottom:1.2rem;">
        Disponible después de completar los <strong>Bloques 1 y 2</strong>. Una vez tienes identidad y presencia,
        este bloque te acompaña mes a mes — con sesiones de trabajo, contenido publicado y seguimiento real.
        <br><strong>Compromiso mínimo: 3 meses.</strong>
    </p>

    <div class="mensual-options">
        <div class="mensual-card">
            <div class="mc-title">Opción Liviana</div>
            <div class="mc-price">$200.000<span style="font-size:0.8rem; font-weight:400; color:#666;">/mes · 5 horas</span></div>
            <table class="deliverable-table" style="font-size:0.84rem;">
                <thead><tr><th>Entregable</th><th style="text-align:center;">Horas</th></tr></thead>
                <tbody>
                    <tr><td>2 sesiones de trabajo estratégico (1h c/u)</td><td>2h</td></tr>
                    <tr><td>Revisión de hasta 4 piezas de contenido</td><td>2h</td></tr>
                    <tr><td>Orientación entre sesiones</td><td>1h</td></tr>
                </tbody>
            </table>
        </div>

        <div class="mensual-card recomendada">
            <div class="mc-title">Opción Estándar <span class="badge-recomendado">⭐ Recomendada</span></div>
            <div class="mc-price">$360.000<span style="font-size:0.8rem; font-weight:400; color:#666;">/mes · 9 horas</span></div>
            <table class="deliverable-table" style="font-size:0.84rem;">
                <thead><tr><th>Entregable</th><th style="text-align:center;">Horas</th></tr></thead>
                <tbody>
                    <tr><td>4 piezas completas (copy + diseño + programación)</td><td>7h</td></tr>
                    <tr><td>2 sesiones de trabajo estratégico (1h c/u)</td><td>2h</td></tr>
                </tbody>
            </table>
            <div class="bloque-note" style="margin-top:0.8rem; font-size:0.82rem;">
                Las 4 piezas mensuales se producen con un sistema de plantillas diseñadas a la medida de Katerine —
                identidad visual consistente y agilidad en la ejecución. Incluye copy, diseño gráfico y programación.
                Katerine solo aprueba.
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── CONDICIONES ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card neutral">
    <div class="section-title">Condiciones del acompañamiento mensual</div>
    <ul class="condiciones-list">
        <li>Requisito previo: Bloques 1 y 2 completados</li>
        <li>Duración mínima: 3 meses</li>
        <li>Modalidad: Presencial · Cali</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# ── PRÓXIMOS PASOS ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-title">Próximos pasos</div>
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-title">Elige tu bloque</div>
            <div class="step-desc">Dinos por cuál o cuáles quieres arrancar. Puedes empezar con uno y agregar los demás después.</div>
        </div>
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-title">Acordamos y arrancamos</div>
            <div class="step-desc">Definimos fechas, confirmamos el acuerdo por escrito y agendamos la primera sesión de trabajo.</div>
        </div>
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-title">Tú te muestras</div>
            <div class="step-desc">Empiezas a existir digitalmente con claridad, estructura y una voz que te representa de verdad.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>Co|Creemos Colectivo</strong><br>
    Estrategia, estructura y alma para construir negocio desde adentro<br>
    Cali, Colombia
</div>
""", unsafe_allow_html=True)
