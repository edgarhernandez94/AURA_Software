import pylsl
import numpy as np
import pandas as pd
import pickle
import serial
import time
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

arduino = serial.Serial(port='COM13', baudrate=9600, timeout=.1)

print("looking for an EEG stream...")
brain_stream = pylsl.resolve_stream("name", "AURA_Power")

brain_inlet = pylsl.StreamInlet(brain_stream[0])
brain_inlet.open_stream()

global sample

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def conteo():
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("0")
    time.sleep(1)

def calibration():

    label = "train"

    rest_df = pd.DataFrame()
    move_df = pd.DataFrame()

    print("RELAX TRAINING IN 5 SECONDS")
    conteo()

    ################################# training rest
    timeout = True
    start = time.time()

    while timeout:
        end = time.time()
        end2 = end - start
        if (end2 > 10):
            timeout = False

        sample, timestamp = brain_inlet.pull_sample()
        print(sample)
        rest_df = pd.concat([rest_df, pd.DataFrame(sample).T])

    rest_df.reset_index()
    rest_df["Event"] = 0

    print(rest_df.shape)

    print("Entrenamiento de intencion de movimiento en 5 segundos")
    conteo()

    ################################# training move
    timeout = True
    start = time.time()

    while timeout:
        end = time.time()
        end2 = end - start
        if (end2 > 10):
            timeout = False

        sample, timestamp = brain_inlet.pull_sample()
        print(sample)
        move_df = pd.concat([move_df, pd.DataFrame(sample).T])

    move_df.reset_index()
    move_df["Event"] = 1

    print("END OF TRAINING")

    print("AI TRAINING INIT")
    selected_data = pd.concat([rest_df, move_df])
    selected_data.to_csv('full_data_personas_nuevas.csv')

    X = selected_data.iloc[1:, :-1].values
    y = selected_data.iloc[1:, -1].values

    sc_x = StandardScaler()
    X = sc_x.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    lr_model_3 = LogisticRegression()
    lr_model_3.fit(X_train, y_train)
    print("AI TRAINING END")
    lr_y_pred_3 = lr_model_3.predict(X_test)

    print("AI ACCURACY (%): ", accuracy_score(y_test, lr_y_pred_3) * 100)

    print("Desea continuar con el control (y) o reiniciar el entrenamiento (n)? (y / n):")
    respuesta = input()

    if respuesta == "y":
        label = "ininew"
        counter_1 = 0

        while True:
            sample, timestamp = brain_inlet.pull_sample()

            if counter_1 == 700:
                write_read("1")
                counter_1 = 0
                print("Tiempo de relajacion: 5 segundos.")
                conteo()
                write_read("2y")
                break

            if label == "ininew":
                intention = lr_model_3.predict(sc_x.transform(pd.DataFrame(sample).values.T))
                if intention== 1:
                    counter_1 = counter_1 + 1
            else:
                if counter_1 > 0:
                    counter_1 = counter_1 - 1
                else:
                    counter_1 = 0

            print(counter_1)

        time.sleep(5)
        print("Inicia nuevamente el monitoreo")
 
calibration()