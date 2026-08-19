import streamlit as st
import pandas as pd
from datetime import date

ARCHIVO_DATOS = "transacciones.csv"

categorias=["Comidas", "Transporte", "Salud", "Ocio", "Hogar", "Otros"]


class Transaccion:
    def __init__(self, descripcion, monto, fecha, categoria, tipo):
        self.descripcion = descripcion
        self.monto = monto
        self.fecha = fecha
        self.categoria = categoria
        self.tipo = tipo

    def es_gasto(self):
        return self.tipo == "Gasto"

    def es_ingreso(self):
        return self.tipo == "Ingreso"

    def a_diccionario(self):
        return {
            "descripcion": self.descripcion,
            "monto": self.monto,
            "fecha": self.fecha,
            "categoria": self.categoria,
            "tipo": self.tipo
        }


class Cartera:
    def __init__(self, transacciones=None):
        self.transacciones = transacciones if transacciones is not None else []

    def agregar(self, transaccion):
        self.transacciones.append(transaccion)

    def cantidad(self):
        return len(self.transacciones)

    def __len__(self):
        return len(self.transacciones)

    def __iter__(self):
        return iter(self.transacciones)

    def resumen(self):
        ingresos = sum(t.monto for t in self.transacciones if t.es_ingreso())
        gastos = sum(t.monto for t in self.transacciones if t.es_gasto())
        balance = ingresos - gastos
        cantidad_gastos = sum(1 for t in self.transacciones if t.es_gasto())
        gasto_promedio = gastos / cantidad_gastos if cantidad_gastos > 0 else 0.0
        return {
            "ingresos": ingresos,
            "gastos": gastos,
            "balance": balance,
            "gasto_promedio": gasto_promedio
        }

    def filtrar_por_categoria(self, categoria):
        filtradas = [t for t in self.transacciones if t.categoria == categoria]
        return Cartera(filtradas)

    def filtrar_por_fechas(self, fecha_inicio, fecha_fin):
        filtradas = [t for t in self.transacciones if fecha_inicio <= t.fecha <= fecha_fin]
        return Cartera(filtradas)

    def gastos_por_categoria(self):
        totales = {}
        for t in self.transacciones:
            if t.es_gasto():
                totales[t.categoria] = totales.get(t.categoria, 0) + t.monto
        return totales

    def gastos_por_fecha(self):
        totales = {}
        for t in self.transacciones:
            if t.es_gasto():
                totales[t.fecha] = totales.get(t.fecha, 0) + t.monto
        return totales

    def to_dataframe(self):
        return pd.DataFrame([t.a_diccionario() for t in self.transacciones])

    def guardar_csv(self, ruta=ARCHIVO_DATOS):
        df = self.to_dataframe()
        df.to_csv(ruta, index=False)

    @staticmethod
    def cargar_csv(ruta=ARCHIVO_DATOS):
        try:
            df = pd.read_csv(ruta)
            transacciones = []
            for _, fila in df.iterrows():
                transacciones.append(Transaccion(
                    descripcion=str(fila["descripcion"]),
                    monto=float(fila["monto"]),
                    fecha=date.fromisoformat(str(fila["fecha"])),
                    categoria=str(fila["categoria"]),
                    tipo=str(fila["tipo"])
                ))
            return Cartera(transacciones)
        except Exception:
            return Cartera()


def inicializar_estado():
    if "cartera" not in st.session_state:
        st.session_state.cartera = Cartera.cargar_csv()

def mostrar_formularios():
    with st.sidebar:
        with st.form("nueva_transaccion"):
            descripcion=st.text_input("Descripcion del gasto o ingreso", placeholder='Escribe la descripcion de la operacion')
            monto=st.number_input("monto", step=1.0, min_value=0.0, format="%0.2f")
            fecha=st.date_input("fecha")
            categoria=st.selectbox("categoria", categorias)
            tipo=st.radio("Tipo", ["Ingreso", "Gasto"], horizontal=True)
            enviado=st.form_submit_button("Enviar")

        if enviado:
            st.session_state.cartera.agregar(Transaccion(descripcion, monto, fecha, categoria, tipo))
            st.success("Transaccion agregada con exito")

def importar_csv():
    with st.sidebar.expander("Importar desde un CSV"):
        archivo = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
        if st.button("Importar transacciones"):
            if archivo is None:
                st.warning("Primero sube un archivo CSV")
                return
            try:
                df = pd.read_csv(archivo)
            except Exception:
                st.error("No es un archivo CSV valido")
                return

            columnas_esperadas = {"descripcion", "monto", "fecha", "categoria", "tipo"}
            if not columnas_esperadas.issubset(set(df.columns)):
                faltantes = columnas_esperadas - set(df.columns)
                st.error(f"Faltan columnas: {', '.join(faltantes)}. Columnas esperadas: {', '.join(columnas_esperadas)}")
                return

            for _, fila in df.iterrows():
                st.session_state.cartera.agregar(Transaccion(
                    descripcion=str(fila["descripcion"]),
                    monto=float(fila["monto"]),
                    fecha=date.fromisoformat(str(fila["fecha"])),
                    categoria=str(fila["categoria"]),
                    tipo=str(fila["tipo"])
                ))

            st.success(f"Se importaron {len(df)} transacciones")

def mostrar_resumen():
    cartera = st.session_state.cartera
    if cartera.cantidad() == 0:
        st.info("No hay transacciones registradas")
        return

    r = cartera.resumen()

    def fmt(v):
        return f"${v:,.2f}".rstrip('0').rstrip('.')

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ingresos", fmt(r["ingresos"]))
    col2.metric("Gastos", fmt(r["gastos"]))
    col3.metric("Balance", fmt(r["balance"]))
    col4.metric("Gasto promedio", fmt(r["gasto_promedio"]))

def mostrar_analisis():
    gastos_por_cat = st.session_state.cartera.gastos_por_categoria()
    gastos_por_fecha = st.session_state.cartera.gastos_por_fecha()

    if not gastos_por_cat:
        st.info("No hay gastos registrados")
        return

    df_cat = pd.DataFrame({"Categoria": list(gastos_por_cat.keys()), "Total": list(gastos_por_cat.values())})

    st.subheader("Gastos por categoria (Barras)")
    st.bar_chart(df_cat.set_index("Categoria"))

    df_fecha = pd.DataFrame({"Fecha": list(gastos_por_fecha.keys()), "Total": list(gastos_por_fecha.values())})
    df_fecha = df_fecha.sort_values("Fecha")

    st.subheader("Gastos por fecha (Lineas)")
    st.line_chart(df_fecha.set_index("Fecha"))

def mostrar_transacciones():
    cartera = st.session_state.cartera
    if cartera.cantidad() > 0:
        st.subheader("Transacciones realizadas: ")
        df = cartera.to_dataframe()
        st.dataframe(df)
        csv = df.to_csv(index=False)
        st.download_button("Descargar transacciones", csv, "mis_transacciones.csv", "text/csv")
    else:
        st.info("No hay transacciones")

st.title("Gestor de Finanzas Personales")
st.write("Organiza tus finanzas de la mejor manera")
st.caption("Version 1.0")

inicializar_estado()
mostrar_formularios()
importar_csv()

tab1, tab2, tab3 = st.tabs(["Resumen", "Movimientos", "Analisis"])

with tab1:
    mostrar_resumen()

with tab2:
    mostrar_transacciones()

with tab3:
    mostrar_analisis()

st.session_state.cartera.guardar_csv()
