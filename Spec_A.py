import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from paragradio.v2025_02 import SpecAnSim
    return SpecAnSim, mo


@app.cell
def __(SpecAnSim):
    simsa = SpecAnSim()
    simsa.start()
    return (simsa,)


@app.cell
def __(cfslider, simsa):
    simsa.set_center_freq(cfslider.value)
    return


@app.cell
def __(mo):
    cfslider = mo.ui.slider(start=92.5e6, stop=94.5e6, step=10e3, label="Frequency (MHz)", show_value=True)
    cfslider
    return (cfslider,)


if __name__ == "__main__":
    app.run()
