import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from paragradio.v2025_02 import PSK_Tx_loop
    return PSK_Tx_loop, mo


@app.cell
def __(PSK_Tx_loop):
    psk = PSK_Tx_loop(modulation="DQPSK")
    psk.start()
    return (psk,)


@app.cell
def __(psk):
    data = [1, 0, 1, 1]
    psk.set_data(data)
    psk.set_amplitude(0.8)
    sr = 4e6
    return data, sr


@app.cell
def __(mo):
    cfslider = mo.ui.slider(start=2.501e9, stop=2.505e9, step=1e6, value=2.503e9, label="Center Frequency Slider", show_value=True)
    return (cfslider,)


@app.cell
def __(cfslider):
    cfslider, f"{cfslider.value/1e9} GHz"
    return


@app.cell
def __(mo):
    IFSlider = mo.ui.slider(start=0, stop=40, step=8, value=32, show_value=True, label="IF Gain Slider")
    IFSlider
    return (IFSlider,)


@app.cell
def __(IFSlider, cfslider, psk):
    psk.set_center_freq(cfslider.value)
    psk.set_if_gain(IFSlider.value)
    return


if __name__ == "__main__":
    app.run()
