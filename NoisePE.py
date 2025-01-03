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
    # nt.set_amplitude(1)
    # nt.set_noise_type("uniform")
    sr = 2e6
    # nt.set_samp_rate(6e6)
    nt.start()
    return nt, sr


if __name__ == "__main__":
    app.run()
