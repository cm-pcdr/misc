import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from paragradio.v2025_02 import WBFM_Rx
    return WBFM_Rx, mo


@app.cell
def __(WBFM_Rx):
    fmrx = WBFM_Rx()
    fmrx.start()
    return (fmrx,)


@app.cell
def __(mo):
    IFSlider = mo.ui.slider(start=0, stop=40, step=8, value=32, show_value=True, label="IF Gain Slider")
    IFSlider
    return (IFSlider,)


@app.cell
def __(mo):
    cfslider = mo.ui.slider(start=88e6, stop=108e6, step=100e3, value=105.5e6)
    cfslider
    return (cfslider,)


@app.cell
def __(mo):
    radiobuttons = mo.ui.radio({"Use Slider": 0, "WGAC 101.9FM": 101.9e6, "WFXA 103.1 FM": 103.1e6, "WBBQ 104.3 FM" : 104.3e6, "WLUB 105.7 FM" : 105.7e6})
    radiobuttons
    return (radiobuttons,)


@app.cell
def __(IFSlider, cfslider, fmrx):
    fmrx.set_center_freq(cfslider.value)
    fmrx.set_if_gain(IFSlider.value)
    # fmrx.set_hw_bb_filt(2.75e6)
    # fmrx.set_samp_rate(8e6)
    return


if __name__ == "__main__":
    app.run()
