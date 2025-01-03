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
    sa.set_center_freq(2.4369e9)
    return (sa,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
