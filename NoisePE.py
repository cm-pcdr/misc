import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from paragradio.v2025_02 import Noise_Tx
    return Noise_Tx, mo


@app.cell
def __(Noise_Tx):
    nt = Noise_Tx()
    nt.start()
    return (nt,)


@app.cell
def __(nt):
    nt.set_amplitude(50)
    nt.set_noise_type("uniform")
    sr = 6e6
    nt.set_samp_rate(sr)
    return (sr,)


@app.cell
def __(mo):
    cfslider = mo.ui.slider(start=2.42e9, stop=2.429e9, step=1e6, value=2.425e9, label="Center Frequency Slider", show_value=True)
    cfslider
    return (cfslider,)


@app.cell
def __(mo):
    IFSlider = mo.ui.slider(start=0, stop=40, step=8, value=40, show_value=True, label="IF Gain Slider")
    IFSlider
    return (IFSlider,)


@app.cell
def __(mo, sr):
    Cutoff = mo.ui.slider(start=2e3, stop=sr/2, step=1e3, show_value=True, label="Cutoff Slider")
    Cutoff
    return (Cutoff,)


@app.cell
def __(mo, sr):
    FTWSlider = mo.ui.slider(start=2e3, stop=sr/2, step=1e3, show_value=True, label="Filter Transition Width Slider")
    FTWSlider
    return (FTWSlider,)


@app.cell
def __(Cutoff, FTWSlider, IFSlider, cfslider, nt):
    nt.set_center_freq(cfslider.value)
    nt.set_if_gain(IFSlider.value)
    nt.set_filter_cutoff_freq(Cutoff.value)
    nt.set_filter_transition_width(FTWSlider.value)
    return


if __name__ == "__main__":
    app.run()
