import streamlit as st

opcion = st.sidebar.selectbox(
    "Elige una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2",
    "Ejercicio 3", "Ejercicio 4"]
)

if opcion == "Home":
    st.title("**APLICACIÓN EN STREAMLIT**")
    st.image("imagen.png")

    st.write("**Nombre completo**: Claudia Carim Huayhua Bellido")
    st.write("**Nombre del módulo**: Phyton for Analytics")
    st.write("**Información del estudiante**: Estudiante de último ciclo de la carrera de Estadística Informática en la UNALM y prácticante en Interbank")
    st.write("**2026**")
    st.write("**Descripción del proyecto**: Desarrolo de una aplicación que integre conceptos aprendidos en el módulo")

    st.write("**Tecnologías usadas: Python y Streamlit**")

# EJERCICIO 1 ################################

if opcion == "Ejercicio 1":
    st.markdown("## Ejercicio 1: Flujo de Caja")

    st.markdown("""
    Este ejercicio permite registrar ingresos y gastos.
    puedes ingresar movimientos que hallas realizado y visualizar:
    - Lista de movimientos
    - Total de ingresos
    - Total de gastos
    - Saldo final

    Finalmente, podrás tener el calculo del flujo de caja, si está a favor o en contra.
    """)



    #### Entrada a la lista vacía
    descripcion = st.text_input("Descripción")
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    dinero = st.number_input("Dinero", min_value = 0.0)
    
    #para q no se borre lo ingresado
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

##cada click se guarda todo en la lista
    if st.button("Agregar"):
        if descripcion != "" and dinero > 0:
            st.session_state.movimientos.append({
            "Descripción": descripcion,
            "Tipo": tipo,
            "Dinero": dinero
        })
    #ponerlo en una tabla
    import pandas as pd
    df = pd.DataFrame(st.session_state.movimientos)
    st.dataframe(df)

    #Calculo de ingresos
    Ingresos = sum( d["Dinero"] for d in st.session_state.movimientos
    if d["Tipo"]=="Ingreso")
    #calculo de gastos
    Gastos = sum(d["Dinero"] for d in st.session_state.movimientos
    if d["Tipo"] == "Gasto")

    # Calcular con cuanto saldo nos quedamos

    Saldo = Ingresos - Gastos

    st.metric("Total Ingresos", Ingresos)
    st.metric("Total Gastos", Gastos)
    st.metric("Saldo Final", Saldo)

    if Saldo > 0:
        st.success("Flujo de caja a favor")
    elif Saldo < 0:
        st.error("Flujo de caja en contra")

    ## por errores
    if len(st.session_state.movimientos) > 0:
        df = pd.DataFrame(st.session_state.movimientos)
        ##st.dataframe(df)
    else:
        st.write("No hay movimientos registrados")


### EJERCICIO 2 ############################

if opcion == "Ejercicio 2":
    st.markdown("## Ejercicio 2: Registro de Productos")

    st.markdown("""
    Este ejercicio registra productos de una tienda utilizando arrays de NumPy.
    Cada registro tiene nombre, categoría, precio, cantidad y total.
    """)


    import numpy as np
    import pandas as pd

    ## crear arrays
    if "nombres" not in st.session_state:
        st.session_state.nombres = np.array([])

    if "categorias" not in st.session_state:
        st.session_state.categorias = np.array([])

    if "precios" not in st.session_state:
        st.session_state.precios = np.array([])

    if "cantidades" not in st.session_state:
        st.session_state.cantidades = np.array([])

    if "totales" not in st.session_state:
        st.session_state.totales = np.array([])

    ## creando las entradas

    nombre = st.text_input("Producto")
    categoria = st.selectbox("Categoría", ["Ropa","Tecnología", "Calzado", "Mascotas", "Juguetes", "Hogar"])
    precio = st.number_input("Precio", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=1)

    if st.button("Agregar"):
        total = precio * cantidad

        st.session_state.nombres = np.append(st.session_state.nombres, nombre)
        st.session_state.categorias = np.append(st.session_state.categorias, categoria)
        st.session_state.precios = np.append(st.session_state.precios, precio)
        st.session_state.cantidades = np.append(st.session_state.cantidades, cantidad)
        st.session_state.totales = np.append(st.session_state.totales, total)

#creando tabla
#import pandas as pd

    if len(st.session_state.nombres) > 0:
        df = pd.DataFrame({
            "Producto": st.session_state.nombres,
            "Categoría": st.session_state.categorias,
            "Precio": st.session_state.precios,
            "Cantidad": st.session_state.cantidades,
            "Total": st.session_state.totales
        })
        st.dataframe(df)
    else:
        st.write("No hay registros")



######### EJERCICIO 3 #########
if opcion == "Ejercicio 3":
    from libreria_funciones_proyecto1 import calcular_metricas_clasificacion

    st.markdown("## Ejercicio 3: Métricas de Clasificación")

    st.markdown("""
    Ingrese valores reales y predicciones para calcular:
    - Precisión
    - Recall
    - F1-score

    ¿Qué significan los valores?

    En este ejercicio trabajamos con clasificación binaria:

    - **1** → Clase positiva (ej: fraude, enfermedad, aprobado)
    - **0** → Clase negativa (ej: no fraude, sano, desaprobado)

    ### Ejemplo:

    Valores reales:  
    `1,0,1,1`

    Predicciones:  
    `1,1,1,0`
    """)


    st.markdown("### Por favor ingrese los valores")

    y_true_input = st.text_input("Valores reales (ej: 1,0,1,1)")
    y_pred_input = st.text_input("Predicciones (ej: 1,1,1,0)")

    if "historial" not in st.session_state:
        st.session_state.historial = []

    if st.button("Calcular"):
        y_true = [int(x) for x in y_true_input.split(",")]
        y_pred = [int(x) for x in y_pred_input.split(",")]
        if len(y_true) != len(y_pred):
            st.error("Las listas deben tener el mismo tamaño")
        else:
            tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
            fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
            fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)
            st.markdown("### 📊 Parámetros calculados")
            st.write("True Positives (TP):", tp)
            st.write("False Positives (FP):", fp)
            st.write("False Negatives (FN):", fn)

            resultado = calcular_metricas_clasificacion(tp, fp, fn)

            #st.write("TP:", tp, "FP:", fp, "FN:", fn)
            #st.write(resultado)

            #guardar resultado

            st.session_state.historial.append({
                "TP": tp,
                "FP": fp,
                "FN": fn,
                "Precision": resultado["precision"],
                "Recall": resultado["recall"],
                "F1": resultado["f1_score"]
            })
    import pandas as pd
    if len(st.session_state.historial) > 0:
        df = pd.DataFrame(st.session_state.historial)
        st.dataframe(df)

###### pregunta 5

if opcion == "Ejercicio 4":

    from libreria_clases_proyecto1 import Paciente
    import streamlit as st
    import pandas as pd

    # memoria
    if "pacientes" not in st.session_state:
        st.session_state.pacientes = []

    st.markdown("## Registro de Pacientes")

    #  CREAR 
    with st.form("form_crear"):

        nombre = st.text_input("Nombre")
        peso = st.number_input("Peso (kg)", min_value=0.0)
        altura = st.number_input("Altura (m)", min_value=0.0)

        submit_crear = st.form_submit_button("Agregar Paciente")

        if submit_crear:
            if nombre != "":
                nuevo = Paciente(nombre, peso, altura)
                st.session_state.pacientes.append(nuevo)
                st.success("Paciente agregado")
            else:
                st.error("Ingresa un nombre")

    # LEER 
    st.markdown("### Lista de pacientes")

    if len(st.session_state.pacientes) > 0:
        datos = [p.resumen() for p in st.session_state.pacientes]
        df = pd.DataFrame(datos)
        st.dataframe(df)
    else:
        st.info("No hay pacientes registrados")

    # solo si hay datos
    if len(st.session_state.pacientes) > 0:

        nombres = [p.nombre for p in st.session_state.pacientes]

        #  ELIMINAR 
        with st.form("form_eliminar"):

            eliminar = st.selectbox("Eliminar paciente", nombres, key="eliminar_select")
            submit_eliminar = st.form_submit_button("Eliminar")

            if submit_eliminar:
                st.session_state.pacientes = [
                    p for p in st.session_state.pacientes if p.nombre != eliminar
                ]
                st.success("Paciente eliminado")
                st.rerun()
        #  ACTUALIZAR 
        with st.form("form_actualizar"):

            actualizar = st.selectbox("Seleccionar paciente", nombres, key="actualizar_select")

            nuevo_peso = st.number_input("Nuevo peso", min_value=0.0)
            nueva_altura = st.number_input("Nueva altura", min_value=0.0)

            submit_actualizar = st.form_submit_button("Actualizar")

            if submit_actualizar:
                for p in st.session_state.pacientes:
                    if p.nombre == actualizar:
                        p.peso_kg = nuevo_peso
                        p.altura_m = nueva_altura
                        st.success("Paciente actualizado correctamente")
                        st.rerun()