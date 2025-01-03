import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from paragradio.v2025_02 import PSK_Tx_loop
    import numpy as np
    return PSK_Tx_loop, mo, np


@app.cell
def __(PSK_Tx_loop, np):
    phaser = PSK_Tx_loop(modulation="BPSK")
    phaser.start()
    data = np.array([1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1])
    phaser.set_data(data)
    # phaser.set_amplitude(1)
    phaser.set_if_gain(32)
    return data, phaser


@app.cell
def __():
    # data = np.array([1, 0, 1, 1])
    # dq = PSK_Tx_loop(modulation="BPSK")
    # dq.set_data(data)
    # # dq.set_amplitude(1)
    # dq.start()


    return


@app.cell
def __():
    # dq.set_if_gain(46)
    return


if __name__ == "__main__":
    app.run()
