import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from paragradio.v2025_02 import SpecAn
    return SpecAn, mo


@app.cell
def __(SpecAn):
    sa = SpecAn()
    sa.start()
    return (sa,)


@app.cell
def __(mo):
    cfslider = mo.ui.slider(start=100e6, stop=2.6e9, step=100e3, value=105.5e6, show_value=True, label="Frequency (MHz)")
    cfslider
    return (cfslider,)


@app.cell
def __(mo):
    IFSlider = mo.ui.slider(start=0, stop=40, step=8, value=32, show_value=True, label="IF Gain Slider")
    IFSlider
    return (IFSlider,)


@app.cell
def __(mo):
    BBSlider = mo.ui.slider(start=0, stop=62, step=2, value=40, show_value=True, label="BB Gain Slider")
    BBSlider
    return (BBSlider,)


@app.cell
def __(BBSlider, IFSlider, cfslider, sa):

    sa.set_center_freq(cfslider.value)
    sa.set_if_gain(IFSlider.value)
    sa.set_bb_gain(BBSlider.value)
    # sa.set_samp_rate(18e6)
    return


if __name__ == "__main__":
    app.run()
