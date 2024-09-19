import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


def Inegi_heatmap():
    df = pd.read_csv("conjunto_de_datos_natalidad_2021.csv")

    df_jalisco = df[df['ent_ocurr'] == 14].copy()

    df_jalisco.loc[:, 'edad_madn_cat'] = pd.cut(df_jalisco['edad_madn'], bins=[0, 20, 30, 40, 50, 60, 100],
                                                labels=['0-20', '21-30', '31-40', '41-50', '51-60', '60+'])
    df_jalisco.loc[:, 'edad_padn_cat'] = pd.cut(df_jalisco['edad_padn'], bins=[0, 20, 30, 40, 50, 60, 100],
                                                labels=['0-20', '21-30', '31-40', '41-50', '51-60', '60+'])

    df_jalisco['info'] = (
            'Edad de la Madre: ' + df_jalisco['edad_madn'].astype(str) + '<br>' +
            'Edad del Padre: ' + df_jalisco['edad_padn'].astype(str) + '<br>' +
            'Hijos Vivos: ' + df_jalisco['hijos_vivo'].astype(str)
    )

    fig = px.density_heatmap(
        df_jalisco,
        x='edad_madn_cat',
        y='edad_padn_cat',
        z='hijos_vivo',
        hover_name='info',
        labels={'edad_madn_cat': 'Edad de la Madre', 'edad_padn_cat': 'Edad del Padre', 'hijos_vivo': 'Hijos Vivos'},
        color_continuous_scale="Viridis",
    )

    fig.update_layout(
        title="Mapa de calor Jalisco",
        xaxis_title="Edad de la Madre",
        yaxis_title="Edad del Padre",
    )

    fig.show()


def normalizacion():
    df = pd.read_csv("diabetes.txt", sep='\t')
    df = df.apply(pd.to_numeric, errors='coerce')

    last_column = df.iloc[:, -1]
    df_to_normalize = df.iloc[:, :-1]

    scaler = StandardScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df_to_normalize), columns=df_to_normalize.columns)

    df_final = pd.concat([df_normalized, last_column], axis=1)

    df_final.to_csv('diabetes_normalized.csv', index=False)

    print("Datos normalizados guardados en 'diabetes_normalized.csv' ")